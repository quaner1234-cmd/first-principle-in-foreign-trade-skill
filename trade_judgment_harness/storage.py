import contextlib
import fcntl
import hashlib
import json
import os
import re
import tempfile
import uuid
from datetime import datetime, timezone
from pathlib import Path

from .errors import HarnessError, StateConflictError
from .schema import JSONSchemaValidator, load_schema


SAFE_PROJECT_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$")
SAFE_RUN_ID = re.compile(r"^run_[A-Za-z0-9_-]+$")


def utc_now():
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def sha256_text(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def new_run_id():
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S")
    return "run_{}_{}".format(timestamp, uuid.uuid4().hex[:10])


def atomic_write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    descriptor, temporary = tempfile.mkstemp(prefix=".tmp-", suffix=".json", dir=str(path.parent))
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


class StateStore:
    def __init__(self, config):
        self.config = config
        self.root = Path(config["runtime_dir"])
        self.projects_dir = self.root / "projects"
        self.runs_dir = self.root / "runs"
        self.locks_dir = self.root / "locks"
        for path in (self.root, self.projects_dir, self.runs_dir, self.locks_dir):
            path.mkdir(parents=True, exist_ok=True)
            try:
                path.chmod(0o700)
            except OSError:
                pass
        schema_root = config["schema_root"]
        self.project_schema = load_schema(schema_root, "project-state.schema.json")
        self.run_schema = load_schema(schema_root, "run-state.schema.json")
        self.validator = JSONSchemaValidator()

    @contextlib.contextmanager
    def lock(self, name):
        safe_name = re.sub(r"[^A-Za-z0-9_.-]", "_", name)
        lock_path = self.locks_dir / (safe_name + ".lock")
        with lock_path.open("a+", encoding="utf-8") as handle:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
            try:
                yield
            finally:
                fcntl.flock(handle.fileno(), fcntl.LOCK_UN)

    def ensure_project(self, project_id, title, customer_ref, policy_version):
        self._validate_project_id(project_id)
        path = self._project_path(project_id)
        with self.lock("project-{}".format(project_id)):
            if path.exists():
                return self._read(path)
            now = utc_now()
            project = {
                "schema_version": "1.0",
                "project_id": project_id,
                "title": title or project_id,
                "customer_ref": customer_ref or "",
                "stage": "unknown",
                "momentum": "unknown",
                "facts": [],
                "inferences": [],
                "unknowns": [],
                "commitments": [],
                "pending_actions": [],
                "decision_history": [],
                "last_run_id": None,
                "policy_version": policy_version,
                "revision": 0,
                "created_at": now,
                "updated_at": now,
            }
            self.validator.validate(project, self.project_schema)
            atomic_write_json(path, project)
            return project

    def load_project(self, project_id):
        self._validate_project_id(project_id)
        path = self._project_path(project_id)
        if not path.exists():
            raise HarnessError("Project does not exist: {}".format(project_id))
        project = self._read(path)
        self.validator.validate(project, self.project_schema)
        return project

    def update_project_from_decision(self, project_id, run_id, decision, policy_version, expected_revision):
        self._validate_project_id(project_id)
        with self.lock("project-{}".format(project_id)):
            project = self.load_project(project_id)
            if project["revision"] != expected_revision:
                raise StateConflictError(
                    "Project {} changed from revision {} to {}".format(
                        project_id, expected_revision, project["revision"]
                    )
                )
            now = utc_now()
            project["stage"] = decision["project_stage"]
            project["momentum"] = decision["momentum"]
            project["facts"] = self._merge_records(
                project["facts"], self._tag_records(decision["facts"], "fact", run_id, now)
            )
            project["inferences"] = self._tag_records(decision["inferences"], "inference", run_id, now)
            project["unknowns"] = self._tag_records(decision["unknowns"], "unknown", run_id, now)
            project["commitments"] = self._tag_records(decision["can_say"], "commitment", run_id, now)
            project["pending_actions"] = self._tag_actions(
                decision["next_actions"] + decision["parallel_actions"], run_id, now
            )
            if run_id not in project["decision_history"]:
                project["decision_history"].append(run_id)
            project["last_run_id"] = run_id
            project["policy_version"] = policy_version
            project["revision"] += 1
            project["updated_at"] = now
            self.validator.validate(project, self.project_schema)
            atomic_write_json(self._project_path(project_id), project)
            return project

    def create_run(self, run):
        self._validate_run_id(run["run_id"])
        path = self._run_path(run["run_id"])
        with self.lock("run-{}".format(run["run_id"])):
            if path.exists():
                raise StateConflictError("Run already exists: {}".format(run["run_id"]))
            self.validator.validate(run, self.run_schema)
            atomic_write_json(path, run)

    def save_run(self, run):
        self._validate_run_id(run["run_id"])
        run["updated_at"] = utc_now()
        self.validator.validate(run, self.run_schema)
        with self.lock("run-{}".format(run["run_id"])):
            atomic_write_json(self._run_path(run["run_id"]), run)

    def load_run(self, run_id):
        self._validate_run_id(run_id)
        path = self._run_path(run_id)
        if not path.exists():
            raise HarnessError("Run does not exist: {}".format(run_id))
        run = self._read(path)
        self.validator.validate(run, self.run_schema)
        return run

    def _project_path(self, project_id):
        return self.projects_dir / (project_id + ".json")

    def _run_path(self, run_id):
        return self.runs_dir / (run_id + ".json")

    @staticmethod
    def _read(path):
        with Path(path).open("r", encoding="utf-8") as handle:
            return json.load(handle)

    @staticmethod
    def _tag_records(records, prefix, run_id, now):
        tagged = []
        for record in records:
            item = dict(record)
            fingerprint = sha256_text(json.dumps(record, ensure_ascii=False, sort_keys=True))[:16]
            item["record_id"] = "{}_{}".format(prefix, fingerprint)
            item["run_id"] = run_id
            item["recorded_at"] = now
            tagged.append(item)
        return tagged

    @staticmethod
    def _merge_records(existing, incoming):
        merged = {item["record_id"]: item for item in existing}
        for item in incoming:
            merged[item["record_id"]] = item
        return list(merged.values())

    @staticmethod
    def _tag_actions(actions, run_id, now):
        tagged = []
        for index, action in enumerate(actions):
            item = dict(action)
            fingerprint = sha256_text(
                "{}:{}:{}".format(run_id, index, json.dumps(action, ensure_ascii=False, sort_keys=True))
            )[:16]
            item["action_id"] = "action_{}".format(fingerprint)
            item["run_id"] = run_id
            item["status"] = "proposed"
            item["recorded_at"] = now
            tagged.append(item)
        return tagged

    @staticmethod
    def _validate_project_id(project_id):
        if SAFE_PROJECT_ID.match(project_id or "") is None:
            raise HarnessError("Invalid project id: {!r}".format(project_id))

    @staticmethod
    def _validate_run_id(run_id):
        if SAFE_RUN_ID.match(run_id or "") is None:
            raise HarnessError("Invalid run id: {!r}".format(run_id))
