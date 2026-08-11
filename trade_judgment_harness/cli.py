import argparse
import json
import sys
from pathlib import Path

from .audit import AuditLog
from .config import initialize_local_files, load_config
from .errors import HarnessError
from .policy import PolicyLoader
from .providers import create_provider
from .render import render_decision, render_run_status
from .runner import HarnessRunner
from .schema import load_schema
from .storage import StateStore


def build_parser():
    parser = argparse.ArgumentParser(
        prog="trade-harness",
        description="Trade Judgment durable runtime harness",
    )
    parser.add_argument("--config", help="Path to harness.config.local.json")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("init", help="Create private local config, company context, and runtime directories")

    doctor = subparsers.add_parser("doctor", help="Validate local configuration, policy, and schemas")
    doctor.add_argument("--check-provider", action="store_true", help="Also validate provider credentials/config")

    run = subparsers.add_parser("run", help="Start a new durable project run")
    run.add_argument("--project", required=True, help="Stable project id, e.g. nordcommute-001")
    run.add_argument("--input", required=True, help="UTF-8 input file, or - for stdin")
    run.add_argument("--title", help="Project title")
    run.add_argument("--customer", default="", help="Customer reference; avoid secrets")
    run.add_argument("--customer-reply", action="store_true", help="Explicitly allow a reply draft")
    run.add_argument("--replay", help="Deterministic replay JSON instead of a live model")

    resume = subparsers.add_parser("resume", help="Resume a paused or recoverable run")
    resume.add_argument("--run", required=True, dest="run_id")
    resume.add_argument("--replay", help="Deterministic replay JSON instead of a live model")

    status = subparsers.add_parser("status", help="Show one run status")
    status.add_argument("--run", required=True, dest="run_id")

    project = subparsers.add_parser("project", help="Show structured project state")
    project.add_argument("--project", required=True, dest="project_id")

    render = subparsers.add_parser("render", help="Render a completed decision as readable Markdown")
    render.add_argument("--run", required=True, dest="run_id")

    tool_result = subparsers.add_parser("tool-result", help="Supply a sourced result for a manual tool call")
    tool_result.add_argument("--run", required=True, dest="run_id")
    tool_result.add_argument("--call", required=True, dest="call_id")
    tool_result.add_argument("--file", required=True, help="JSON/text result file, or - for stdin")
    tool_result.add_argument("--by", required=True, help="Person or connector supplying the result")

    approve = subparsers.add_parser("approve-tool", help="Approve one pending side-effecting tool call")
    approve.add_argument("--run", required=True, dest="run_id")
    approve.add_argument("--call", required=True, dest="call_id")
    approve.add_argument("--by", required=True)
    approve.add_argument("--reason", default="")

    reject = subparsers.add_parser("reject-tool", help="Reject one pending tool call")
    reject.add_argument("--run", required=True, dest="run_id")
    reject.add_argument("--call", required=True, dest="call_id")
    reject.add_argument("--by", required=True)
    reject.add_argument("--reason", default="")

    subparsers.add_parser("audit-verify", help="Verify the local hash-chained audit log")
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "init":
            created, config = initialize_local_files(Path.cwd())
            if created:
                print("Created:")
                for path in created:
                    print("- {}".format(path))
            else:
                print("Local harness files already exist; nothing overwritten.")
            print("Runtime directory: {}".format(config["runtime_dir"]))
            return 0

        config = load_config(args.config, Path.cwd())
        if args.command == "doctor":
            return _doctor(config, args.check_provider)

        store = StateStore(config)
        audit = AuditLog(config, store)

        if args.command == "status":
            print(render_run_status(store.load_run(args.run_id)), end="")
            return 0
        if args.command == "project":
            print(json.dumps(store.load_project(args.project_id), ensure_ascii=False, indent=2, sort_keys=True))
            return 0
        if args.command == "render":
            run = store.load_run(args.run_id)
            if not run.get("decision"):
                raise HarnessError("Run has no final decision; current status is {}".format(run["status"]))
            print(render_decision(run["decision"], run["run_id"]), end="")
            return 0
        if args.command == "audit-verify":
            ok, message = audit.verify()
            print(message)
            return 0 if ok else 1

        if args.command in ("run", "resume"):
            provider = create_provider(config, getattr(args, "replay", None))
            runner = HarnessRunner(config, provider)
            if args.command == "run":
                input_text = _read_input(args.input)
                run = runner.start(
                    args.project,
                    input_text,
                    title=args.title,
                    customer_ref=args.customer,
                    metadata={"customer_reply_requested": bool(args.customer_reply)},
                )
            else:
                run = runner.resume(args.run_id)
            _print_run(run)
            return 1 if run["status"] in ("failed", "failed_recoverable") else 0

        # Approval and manual result commands do not instantiate a live model.
        runner = HarnessRunner(config, _NoopProvider())
        if args.command == "tool-result":
            raw = _read_input(args.file)
            try:
                value = json.loads(raw)
            except json.JSONDecodeError:
                value = {"summary": raw.strip(), "facts": [], "not_found": [], "attachments": []}
            run = runner.add_tool_result(args.run_id, args.call_id, value, args.by)
            print(render_run_status(run), end="")
            print("Result stored. Run `trade-harness resume --run {}`.".format(args.run_id))
            return 0
        if args.command == "approve-tool":
            run = runner.approve_tool(args.run_id, args.call_id, args.by, args.reason)
            print(render_run_status(run), end="")
            print("Approval stored. Run `trade-harness resume --run {}`.".format(args.run_id))
            return 0
        if args.command == "reject-tool":
            run = runner.reject_tool(args.run_id, args.call_id, args.by, args.reason)
            print(render_run_status(run), end="")
            print("Rejection stored. Run `trade-harness resume --run {}`.".format(args.run_id))
            return 0
        parser.error("Unknown command")
    except (HarnessError, OSError, ValueError, json.JSONDecodeError) as error:
        print("error: {}".format(error), file=sys.stderr)
        return 1


def _doctor(config, check_provider):
    policy = PolicyLoader(config)
    print("Policy root: {}".format(config["policy_root"]))
    print("Policy version: {}".format(policy.version))
    policy.routing_bundle()
    schema_root = config["schema_root"]
    for name in (
        "route-result.schema.json",
        "agent-turn.schema.json",
        "project-state.schema.json",
        "run-state.schema.json",
        "manual-tool-result.schema.json",
    ):
        schema = load_schema(schema_root, name)
        if not isinstance(schema, dict):
            raise HarnessError("Invalid schema: {}".format(name))
        print("Schema OK: {}".format(name))
    company = Path(config["policy_root"]) / config.get("company_context", "company-context.local.md")
    print("Company context: {}".format("configured" if company.exists() else "missing (capabilities remain unknown)"))
    print("Runtime directory: {}".format(config["runtime_dir"]))
    if check_provider:
        provider = create_provider(config)
        print("Provider config OK: {}".format(provider.name))
    print("Doctor: OK")
    return 0


def _read_input(path_value):
    if path_value == "-":
        return sys.stdin.read()
    return Path(path_value).read_text(encoding="utf-8")


def _print_run(run):
    if run.get("decision"):
        print(render_decision(run["decision"], run["run_id"]), end="")
    else:
        print(render_run_status(run), end="")
        if run["pending_tool_calls"]:
            print("Use tool-result / approve-tool / reject-tool, then resume the run.")


class _NoopProvider:
    name = "no_model_required"

    def generate(self, purpose, system_prompt, payload, schema_name, schema):
        raise HarnessError("This command does not invoke a model")


if __name__ == "__main__":
    raise SystemExit(main())
