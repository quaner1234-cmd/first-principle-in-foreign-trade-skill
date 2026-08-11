import copy
import json
from pathlib import Path

from .errors import ConfigurationError


ALLOWED_PERMISSIONS = {"allow", "approval", "manual", "deny"}


def _merge(base, override):
    result = copy.deepcopy(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(result.get(key), dict):
            result[key] = _merge(result[key], value)
        else:
            result[key] = copy.deepcopy(value)
    return result


def _read_json(path):
    with Path(path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_config(config_path=None, cwd=None):
    base_dir = Path(cwd or Path.cwd()).resolve()
    example_path = base_dir / "harness.config.example.json"
    if not example_path.exists():
        raise ConfigurationError("Missing harness.config.example.json in {}".format(base_dir))
    config = _read_json(example_path)

    selected = Path(config_path).resolve() if config_path else base_dir / "harness.config.local.json"
    if selected.exists():
        config = _merge(config, _read_json(selected))

    config["_base_dir"] = str(base_dir)
    config["_config_path"] = str(selected)
    config["policy_root"] = str((base_dir / config.get("policy_root", ".")).resolve())
    config["runtime_dir"] = str((base_dir / config.get("runtime_dir", ".trade-harness")).resolve())
    config["schema_root"] = str((base_dir / "schemas").resolve())

    for tool_name, permission in config.get("permissions", {}).items():
        if permission not in ALLOWED_PERMISSIONS:
            raise ConfigurationError(
                "Permission for {} must be one of {}".format(tool_name, sorted(ALLOWED_PERMISSIONS))
            )
    limits = config.get("limits", {})
    if int(limits.get("max_turns", 0)) < 1:
        raise ConfigurationError("limits.max_turns must be at least 1")
    return config


def initialize_local_files(base_dir):
    root = Path(base_dir).resolve()
    created = []
    local_config = root / "harness.config.local.json"
    if not local_config.exists():
        local_config.write_text(
            (root / "harness.config.example.json").read_text(encoding="utf-8"),
            encoding="utf-8",
        )
        created.append(str(local_config))
    local_config.chmod(0o600)

    company_context = root / "company-context.local.md"
    if not company_context.exists():
        company_context.write_text(
            (root / "company-context.template.md").read_text(encoding="utf-8"),
            encoding="utf-8",
        )
        created.append(str(company_context))
    company_context.chmod(0o600)

    config = load_config(str(local_config), root)
    runtime = Path(config["runtime_dir"])
    for child in ("projects", "runs", "audit", "notes", "locks"):
        (runtime / child).mkdir(parents=True, exist_ok=True)
    return created, config
