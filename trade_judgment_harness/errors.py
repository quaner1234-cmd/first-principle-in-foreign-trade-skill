class HarnessError(Exception):
    """Base runtime error."""


class ConfigurationError(HarnessError):
    """Invalid or missing harness configuration."""


class SchemaValidationError(HarnessError):
    def __init__(self, errors):
        self.errors = list(errors)
        super().__init__("; ".join(self.errors))


class DomainValidationError(HarnessError):
    def __init__(self, errors):
        self.errors = list(errors)
        super().__init__("; ".join(self.errors))


class ProviderError(HarnessError):
    """Model provider failed or returned unusable data."""


class RunLimitError(HarnessError):
    """The configured model-turn budget was exhausted."""


class StateConflictError(HarnessError):
    """Optimistic state revision did not match."""


class ToolError(HarnessError):
    """Tool input, policy, or execution error."""


class ApprovalRequired(HarnessError):
    """A tool call is waiting for explicit human approval."""
