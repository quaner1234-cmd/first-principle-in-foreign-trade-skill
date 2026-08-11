import json
import tempfile
import unittest
from pathlib import Path

from trade_judgment_harness.config import load_config
from trade_judgment_harness.errors import DomainValidationError, ToolError
from trade_judgment_harness.providers import ReplayProvider
from trade_judgment_harness.runner import HarnessRunner
from trade_judgment_harness.validators import DomainValidator


ROOT = Path(__file__).resolve().parents[1]


def route():
    return {
        "project_stage": "qualified_inquiry",
        "stage_basis": "Product, quantity and quote request supplied.",
        "momentum": "positive",
        "momentum_basis": "The buyer supplied concrete information.",
        "primary_mode": 4,
        "secondary_modes": [1],
        "buyer_identity_evidence": "insufficient",
        "due_diligence_strategy": "unable",
        "requires_context_question": False,
        "context_question": None,
    }


def decision():
    return {
        "summary": "Clarify the fabric variables, then quote.",
        "project_stage": "qualified_inquiry",
        "stage_basis": "Product, quantity and quote request supplied.",
        "momentum": "positive",
        "momentum_basis": "The buyer supplied concrete information.",
        "primary_mode": 4,
        "disposition": "progress",
        "facts": [
            {
                "claim": "The buyer requests 500 jackets.",
                "source_type": "user_input",
                "source_ref": "input:current",
                "observed_at": None,
                "expires_at": None,
                "sensitivity": "internal",
            }
        ],
        "inferences": [
            {
                "claim": "Reliable costing still needs fabric variables.",
                "basis_source_refs": ["input:current"],
                "verification_status": "candidate",
            }
        ],
        "unknowns": [
            {
                "description": "Fabric specification",
                "resolution_path": "customer",
                "blocker_status": "soft_blocking",
                "owner": "Customer",
                "low_cost_path": True,
                "decision_impact": "Changes material cost",
            }
        ],
        "proactive_clarifications": ["Check whether a similar construction already exists."],
        "next_actions": [
            {
                "description": "Ask for the price-driving fabric variables.",
                "owner": "Sales",
                "risk": "draft",
                "approval_required": False,
                "idempotency_key": None,
            }
        ],
        "parallel_actions": [],
        "can_say": [],
        "cannot_promise": ["Final FOB price"],
        "stop_conditions": ["The buyer refuses all low-friction clarification paths for a sustained period."],
        "customer_reply": None,
    }


def final_turn():
    return {"status": "final", "tool_requests": [], "decision": decision()}


class FlakyProvider(ReplayProvider):
    name = "flaky"

    def __init__(self, replay):
        super().__init__(replay)
        self.failed_once = False

    def generate(self, purpose, system_prompt, payload, schema_name, schema):
        if purpose == "decide" and not self.failed_once:
            from trade_judgment_harness.errors import ProviderError

            self.failed_once = True
            raise ProviderError("temporary model outage")
        return super().generate(purpose, system_prompt, payload, schema_name, schema)


class HarnessTestCase(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.config = load_config(cwd=ROOT)
        self.config["runtime_dir"] = str(Path(self.temporary.name) / ".trade-harness")

    def test_complete_run_updates_project_and_audit(self):
        provider = ReplayProvider({"route": route(), "turns": [final_turn()]})
        runner = HarnessRunner(self.config, provider)
        run = runner.start("project-001", "Customer requests 500 jackets and a quote.")
        self.assertEqual("completed", run["status"])
        project = runner.store.load_project("project-001")
        self.assertEqual(1, project["revision"])
        self.assertEqual("qualified_inquiry", project["stage"])
        ok, message = runner.audit.verify()
        self.assertTrue(ok, message)

    def test_manual_tool_pause_and_resume(self):
        needs_research = {
            "status": "needs_tools",
            "tool_requests": [
                {
                    "call_id": "research_1",
                    "tool_name": "public_research",
                    "arguments": {"query": "Example buyer identity"},
                    "reason": "Buyer identity evidence is insufficient.",
                }
            ],
            "decision": None,
        }
        provider = ReplayProvider({"route": route(), "turns": [needs_research, final_turn()]})
        runner = HarnessRunner(self.config, provider)
        paused = runner.start("project-002", "Customer requests 500 jackets and a quote.")
        self.assertEqual("waiting_tool_result", paused["status"])
        runner.add_tool_result(
            paused["run_id"],
            "research_1",
            {
                "summary": "No searchable identity was supplied.",
                "facts": [],
                "not_found": ["No company or buyer identity could be checked."],
                "attachments": [],
            },
            "tester",
        )
        completed = runner.resume(paused["run_id"])
        self.assertEqual("completed", completed["status"])

    def test_provider_failure_can_resume_from_checkpoint(self):
        provider = FlakyProvider({"route": route(), "turns": [final_turn()]})
        runner = HarnessRunner(self.config, provider)
        failed = runner.start("project-recovery", "Customer requests 500 jackets and a quote.")
        self.assertEqual("failed_recoverable", failed["status"])
        self.assertIsNotNone(failed["routing"])
        completed = runner.resume(failed["run_id"])
        self.assertEqual("completed", completed["status"])

    def test_approval_tool_is_idempotent(self):
        note_turn = {
            "status": "needs_tools",
            "tool_requests": [
                {
                    "call_id": "note_1",
                    "tool_name": "write_runtime_note",
                    "arguments": {"title": "Internal check", "content": "Confirm fabric feasibility."},
                    "reason": "Persist an internal checkpoint.",
                }
            ],
            "decision": None,
        }
        provider = ReplayProvider({"route": route(), "turns": [note_turn, final_turn()]})
        runner = HarnessRunner(self.config, provider)
        paused = runner.start("project-003", "Customer requests 500 jackets and a quote.")
        self.assertEqual("waiting_approval", paused["status"])
        runner.approve_tool(paused["run_id"], "note_1", "Alex", "Safe local note")
        completed = runner.resume(paused["run_id"])
        self.assertEqual("completed", completed["status"])
        result = completed["tool_results"]["note_1"]
        note_path = Path(result["output"]["path"])
        self.assertTrue(note_path.exists())
        before = note_path.read_text(encoding="utf-8")
        # Re-processing the same call id must not duplicate the side effect.
        replay = runner.tools.process_requests(completed, [note_turn["tool_requests"][0]])
        self.assertEqual([], replay)
        self.assertEqual(before, note_path.read_text(encoding="utf-8"))

    def test_denied_external_send_becomes_tool_error_not_side_effect(self):
        send_turn = {
            "status": "needs_tools",
            "tool_requests": [
                {
                    "call_id": "send_1",
                    "tool_name": "send_external_message",
                    "arguments": {"to": "buyer@example.com", "body": "Hello"},
                    "reason": "Send the reply.",
                }
            ],
            "decision": None,
        }
        provider = ReplayProvider({"route": route(), "turns": [send_turn, final_turn()]})
        runner = HarnessRunner(self.config, provider)
        completed = runner.start("project-004", "Customer requests 500 jackets and a quote.")
        self.assertEqual("completed", completed["status"])
        self.assertFalse(completed["tool_results"]["send_1"]["ok"])

    def test_hard_blocker_dimensions_are_enforced(self):
        value = decision()
        value["unknowns"][0]["blocker_status"] = "hard_blocking"
        value["unknowns"][0]["resolution_path"] = "customer"
        with self.assertRaises(DomainValidationError):
            DomainValidator().validate_turn(
                {"status": "final", "tool_requests": [], "decision": value},
                route(),
                {"facts": []},
                False,
            )

    def test_file_tool_blocks_git_and_secret_paths(self):
        provider = ReplayProvider({"route": route(), "turns": [final_turn()]})
        runner = HarnessRunner(self.config, provider)
        with self.assertRaises(ToolError):
            runner.tools._safe_policy_path(".git/config")
        with self.assertRaises(ToolError):
            runner.tools._safe_policy_path("harness.config.local.json")


if __name__ == "__main__":
    unittest.main()
