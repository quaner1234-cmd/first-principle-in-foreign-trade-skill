import json
import os
import re
import tempfile
from pathlib import Path

from .errors import ToolError
from .schema import JSONSchemaValidator, load_schema
from .storage import utc_now


TOOL_CATALOG = {
    "read_project_file": {
        "risk": "read",
        "default_permission": "allow",
        "description": "Read one UTF-8 text file inside the configured policy/project root.",
    },
    "search_project_files": {
        "risk": "read",
        "default_permission": "allow",
        "description": "Literal text search over files inside the configured policy/project root.",
    },
    "write_runtime_note": {
        "risk": "write",
        "default_permission": "approval",
        "description": "Write an idempotent note inside the private runtime directory after approval.",
    },
    "public_research": {
        "risk": "read",
        "default_permission": "manual",
        "description": "Request public research. A human or connector must return sourced results.",
    },
    "internal_verification": {
        "risk": "external",
        "default_permission": "manual",
        "description": "Request confirmation from an authorized internal owner.",
    },
    "supplier_inquiry": {
        "risk": "external",
        "default_permission": "manual",
        "description": "Request a supplier-side fact. The runtime does not send automatically.",
    },
    "technical_test": {
        "risk": "external",
        "default_permission": "manual",
        "description": "Request real-world testing and wait for the result.",
    },
    "send_external_message": {
        "risk": "external",
        "default_permission": "deny",
        "description": "Send an external message. Disabled in the core runtime.",
    },
}

FORBIDDEN_PARTS = {".git", ".trade-harness", "__pycache__", "node_modules"}
FORBIDDEN_NAMES = {"credentials.json", "secrets.json", "harness.config.local.json"}
FORBIDDEN_SUFFIXES = {".pem", ".key", ".p12", ".pfx"}


class ToolRegistry:
    def __init__(self, config, store, audit):
        self.config = config
        self.store = store
        self.audit = audit
        self.policy_root = Path(config["policy_root"]).resolve()
        self.runtime_root = Path(config["runtime_dir"]).resolve()
        self.max_file_bytes = int(config.get("limits", {}).get("max_file_bytes", 1000000))
        self.max_results = int(config.get("limits", {}).get("max_search_results", 50))
        self.max_tool_output = int(config.get("limits", {}).get("max_tool_output_chars", 30000))
        self.manual_result_schema = load_schema(config["schema_root"], "manual-tool-result.schema.json")
        self.schema_validator = JSONSchemaValidator()

    def descriptions(self):
        result = []
        for name, definition in TOOL_CATALOG.items():
            result.append(
                {
                    "name": name,
                    "risk": definition["risk"],
                    "permission": self.permission_for(name),
                    "description": definition["description"],
                }
            )
        return result

    def permission_for(self, name):
        definition = TOOL_CATALOG.get(name)
        if not definition:
            return "deny"
        return self.config.get("permissions", {}).get(name, definition["default_permission"])

    def process_requests(self, run, requests):
        pending = []
        for request in requests:
            call_id = request["call_id"]
            if call_id in run["tool_results"]:
                continue
            name = request["tool_name"]
            if name not in TOOL_CATALOG:
                run["tool_results"][call_id] = self._result(False, name, error="Unknown tool")
                continue
            permission = self.permission_for(name)
            if permission == "deny":
                run["tool_results"][call_id] = self._result(
                    False, name, error="Tool denied by runtime policy"
                )
                self.audit.append(
                    "tool_denied", run["run_id"], run["project_id"], {"call_id": call_id, "tool": name}
                )
                continue
            if permission == "manual":
                pending.append(self._pending(request, "manual_result"))
                continue
            if permission == "approval":
                approval = run["approvals"].get(call_id)
                if not approval:
                    pending.append(self._pending(request, "approval"))
                    continue
                if approval["status"] == "rejected":
                    run["tool_results"][call_id] = self._result(
                        False, name, error="Rejected by {}: {}".format(
                            approval.get("by", "human"), approval.get("reason", "no reason supplied")
                        )
                    )
                    continue
            run["tool_results"][call_id] = self._execute(run, request)
        run["pending_tool_calls"] = pending
        return pending

    def add_manual_result(self, run, call_id, result, supplied_by):
        pending = {item["call_id"]: item for item in run.get("pending_tool_calls", [])}
        if call_id not in pending or pending[call_id]["wait_type"] != "manual_result":
            raise ToolError("Tool call {} is not waiting for a manual result".format(call_id))
        payload = result if isinstance(result, dict) else {"content": str(result)}
        validation_errors = self.schema_validator.errors(payload, self.manual_result_schema)
        if validation_errors:
            raise ToolError("Manual tool result failed schema validation: {}".format("; ".join(validation_errors)))
        encoded = json.dumps(payload, ensure_ascii=False)
        if len(encoded) > self.max_tool_output:
            raise ToolError("Manual tool result exceeds configured size limit")
        run["tool_results"][call_id] = {
            "ok": True,
            "tool_name": pending[call_id]["tool_name"],
            "output": payload,
            "error": None,
            "completed_at": utc_now(),
            "supplied_by": supplied_by,
        }
        run["pending_tool_calls"] = [item for item in run["pending_tool_calls"] if item["call_id"] != call_id]
        self.audit.append(
            "manual_tool_result_added",
            run["run_id"],
            run["project_id"],
            {"call_id": call_id, "tool": pending[call_id]["tool_name"], "supplied_by": supplied_by},
        )

    def decide_approval(self, run, call_id, approved, decided_by, reason):
        pending = {item["call_id"]: item for item in run.get("pending_tool_calls", [])}
        if call_id not in pending or pending[call_id]["wait_type"] != "approval":
            raise ToolError("Tool call {} is not waiting for approval".format(call_id))
        run["approvals"][call_id] = {
            "status": "approved" if approved else "rejected",
            "by": decided_by,
            "reason": reason or "",
            "decided_at": utc_now(),
        }
        self.audit.append(
            "tool_approved" if approved else "tool_rejected",
            run["run_id"],
            run["project_id"],
            {"call_id": call_id, "tool": pending[call_id]["tool_name"], "by": decided_by},
        )

    def _execute(self, run, request):
        name = request["tool_name"]
        call_id = request["call_id"]
        try:
            if name == "read_project_file":
                output = self._read_file(request["arguments"])
            elif name == "search_project_files":
                output = self._search_files(request["arguments"])
            elif name == "write_runtime_note":
                output = self._write_note(run["project_id"], call_id, request["arguments"])
            else:
                raise ToolError("Tool {} requires a manual adapter result".format(name))
            result = self._result(True, name, output=output)
            self.audit.append(
                "tool_executed", run["run_id"], run["project_id"], {"call_id": call_id, "tool": name}
            )
            return result
        except Exception as error:
            self.audit.append(
                "tool_failed",
                run["run_id"],
                run["project_id"],
                {"call_id": call_id, "tool": name, "error_type": type(error).__name__},
            )
            return self._result(False, name, error=str(error))

    def _read_file(self, arguments):
        path_value = arguments.get("path")
        if not isinstance(path_value, str) or not path_value:
            raise ToolError("read_project_file requires string argument 'path'")
        path = self._safe_policy_path(path_value)
        if not path.is_file():
            raise ToolError("File does not exist: {}".format(path_value))
        if path.stat().st_size > self.max_file_bytes:
            raise ToolError("File exceeds configured size limit")
        return {"path": str(path.relative_to(self.policy_root)), "content": path.read_text(encoding="utf-8")}

    def _search_files(self, arguments):
        query = arguments.get("query")
        glob = arguments.get("glob", "**/*")
        requested = arguments.get("max_results", self.max_results)
        if not isinstance(query, str) or not query:
            raise ToolError("search_project_files requires string argument 'query'")
        if not isinstance(glob, str) or not glob:
            raise ToolError("search_project_files argument 'glob' must be a string")
        if Path(glob).is_absolute() or ".." in Path(glob).parts:
            raise ToolError("search_project_files glob must stay inside the project root")
        if not isinstance(requested, int) or isinstance(requested, bool):
            raise ToolError("search_project_files argument 'max_results' must be an integer")
        limit = min(max(1, requested), self.max_results)
        matches = []
        for path in self.policy_root.glob(glob):
            if len(matches) >= limit:
                break
            if not path.is_file() or self._is_forbidden_path(path) or self.runtime_root in path.parents:
                continue
            try:
                if path.stat().st_size > self.max_file_bytes:
                    continue
                for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                    if query.casefold() in line.casefold():
                        matches.append(
                            {
                                "path": str(path.relative_to(self.policy_root)),
                                "line": line_number,
                                "text": line[:500],
                            }
                        )
                        if len(matches) >= limit:
                            break
            except (OSError, UnicodeDecodeError):
                continue
        return {"query": query, "matches": matches}

    def _write_note(self, project_id, call_id, arguments):
        title = arguments.get("title")
        content = arguments.get("content")
        if not isinstance(title, str) or not title.strip():
            raise ToolError("write_runtime_note requires string argument 'title'")
        if not isinstance(content, str) or not content.strip():
            raise ToolError("write_runtime_note requires string argument 'content'")
        note_dir = self.runtime_root / "notes" / project_id
        note_dir.mkdir(parents=True, exist_ok=True)
        path = note_dir / (re.sub(r"[^A-Za-z0-9_.-]", "_", call_id) + ".md")
        if path.exists():
            return {"path": str(path), "idempotent_replay": True}
        payload = "# {}\n\n{}\n".format(title.strip(), content.strip())
        descriptor, temporary = tempfile.mkstemp(prefix=".note-", dir=str(note_dir))
        try:
            os.fchmod(descriptor, 0o600)
            with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
                handle.write(payload)
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(temporary, path)
        finally:
            if os.path.exists(temporary):
                os.unlink(temporary)
        return {"path": str(path), "idempotent_replay": False}

    def _safe_policy_path(self, value):
        path = (self.policy_root / value).resolve()
        try:
            path.relative_to(self.policy_root)
        except ValueError:
            raise ToolError("Path escapes the configured project root")
        if self._is_forbidden_path(path):
            raise ToolError("Runtime policy blocks access to sensitive or internal path: {}".format(value))
        return path

    def _is_forbidden_path(self, path):
        try:
            relative = path.resolve().relative_to(self.policy_root)
        except ValueError:
            return True
        if any(part in FORBIDDEN_PARTS for part in relative.parts):
            return True
        name = relative.name
        if name in FORBIDDEN_NAMES or name == ".env" or name.startswith(".env."):
            return True
        if relative.suffix.lower() in FORBIDDEN_SUFFIXES:
            return True
        return False

    @staticmethod
    def _pending(request, wait_type):
        item = dict(request)
        item["wait_type"] = wait_type
        item["requested_at"] = utc_now()
        return item

    @staticmethod
    def _result(ok, tool_name, output=None, error=None):
        return {
            "ok": bool(ok),
            "tool_name": tool_name,
            "output": output,
            "error": error,
            "completed_at": utc_now(),
            "supplied_by": "runtime",
        }
