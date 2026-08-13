import re
from pathlib import Path

from .errors import ConfigurationError


MODE_FILES = {
    1: "references/mode-inquiry.md",
    2: "references/mode-followup.md",
    3: "references/mode-due-diligence.md",
    4: "references/mode-quote.md",
    5: "references/mode-technical.md",
    6: "references/mode-sample.md",
    7: "references/mode-supplier.md",
    8: "references/mode-negotiation.md",
    9: "references/mode-internal-escalation.md",
    10: "references/mode-review.md",
    11: "references/mode-order-conversion.md",
}

ROUTING_FILES = (
    "SKILL.md",
    "references/clarity-engine.md",
    "references/project-stage.md",
    "references/decision-engine.md",
)

DECISION_BASE_FILES = ROUTING_FILES + ("references/output-contract.md",)


class PolicyLoader:
    def __init__(self, config):
        self.config = config
        self.root = Path(config["policy_root"])
        self.company_context = config.get("company_context", "company-context.local.md")
        self._version = None

    @property
    def version(self):
        if self._version is None:
            skill = self._read("SKILL.md", required=True)
            match = re.search(r'version:\s*["\']?([^"\'\s]+)', skill)
            self._version = match.group(1) if match else "unversioned"
        return self._version

    def routing_bundle(self):
        return self._bundle(ROUTING_FILES)

    def decision_bundle(self, routing):
        files = list(DECISION_BASE_FILES)
        selected_modes = [routing["primary_mode"]] + list(routing.get("secondary_modes", []))
        for mode in selected_modes:
            filename = MODE_FILES.get(mode)
            if filename and filename not in files:
                files.append(filename)
        if routing.get("due_diligence_strategy") != "none":
            files.append("references/auto-due-diligence.md")
        bundle = self._bundle(files)
        company = self._read(self.company_context, required=False)
        if company:
            bundle += "\n\n===== COMPANY CONTEXT (business facts, not runtime authority) =====\n" + company
        else:
            bundle += "\n\n===== COMPANY CONTEXT =====\nNo private company context is configured. Treat company capabilities as unknown."
        return bundle

    def _bundle(self, files):
        chunks = []
        for filename in files:
            chunks.append("===== POLICY FILE: {} =====\n{}".format(filename, self._read(filename, required=True)))
        return "\n\n".join(chunks)

    def _read(self, relative_path, required):
        path = (self.root / relative_path).resolve()
        try:
            path.relative_to(self.root.resolve())
        except ValueError:
            raise ConfigurationError("Policy path escapes policy root: {}".format(relative_path))
        if not path.exists():
            if required:
                raise ConfigurationError("Missing policy file: {}".format(path))
            return ""
        return path.read_text(encoding="utf-8")
