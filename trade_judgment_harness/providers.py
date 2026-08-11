import json
import os
import subprocess
import time
import urllib.error
import urllib.request

from .errors import ConfigurationError, ProviderError


def _parse_json_text(text):
    if isinstance(text, dict):
        return text
    if isinstance(text, list):
        pieces = []
        for item in text:
            if isinstance(item, dict) and "text" in item:
                pieces.append(item["text"])
            elif isinstance(item, str):
                pieces.append(item)
        text = "".join(pieces)
    if not isinstance(text, str):
        raise ProviderError("Provider response did not contain text or JSON")
    stripped = text.strip()
    if stripped.startswith("```"):
        lines = stripped.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        stripped = "\n".join(lines).strip()
    try:
        value = json.loads(stripped)
    except json.JSONDecodeError as error:
        raise ProviderError("Provider returned invalid JSON: {}".format(error))
    if not isinstance(value, dict):
        raise ProviderError("Provider JSON must be an object")
    return value


class BaseProvider:
    name = "base"

    def generate(self, purpose, system_prompt, payload, schema_name, schema):
        raise NotImplementedError


class OpenAICompatibleProvider(BaseProvider):
    name = "openai_compatible"

    def __init__(self, provider_config):
        self.config = provider_config
        self.base_url = provider_config.get("base_url", "https://api.openai.com/v1").rstrip("/")
        self.endpoint = provider_config.get("endpoint", "/chat/completions")
        model = provider_config.get("model") or os.environ.get(provider_config.get("model_env", ""), "")
        if not model:
            raise ConfigurationError(
                "No model configured. Set provider.model or environment variable {}".format(
                    provider_config.get("model_env", "TRADE_HARNESS_MODEL")
                )
            )
        self.model = model
        key_env = provider_config.get("api_key_env", "OPENAI_API_KEY")
        self.api_key = os.environ.get(key_env, "")
        if not self.api_key:
            raise ConfigurationError("Missing API key environment variable {}".format(key_env))
        self.timeout = int(provider_config.get("timeout_seconds", 120))
        self.retries = max(1, int(provider_config.get("retries", 2)))

    def generate(self, purpose, system_prompt, payload, schema_name, schema):
        body = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": json.dumps(payload, ensure_ascii=False, sort_keys=True)},
            ],
        }
        if self.config.get("strict_json_schema", True):
            clean_schema = dict(schema)
            clean_schema.pop("$schema", None)
            clean_schema.pop("$id", None)
            body["response_format"] = {
                "type": "json_schema",
                "json_schema": {
                    "name": schema_name.replace("-", "_").replace(".", "_")[:64],
                    "strict": True,
                    "schema": clean_schema,
                },
            }
        data = json.dumps(body, ensure_ascii=False).encode("utf-8")
        request = urllib.request.Request(
            self.base_url + self.endpoint,
            data=data,
            method="POST",
            headers={
                "Authorization": "Bearer {}".format(self.api_key),
                "Content-Type": "application/json",
            },
        )
        last_error = None
        for attempt in range(self.retries):
            try:
                with urllib.request.urlopen(request, timeout=self.timeout) as response:
                    result = json.loads(response.read().decode("utf-8"))
                choices = result.get("choices") or []
                if not choices:
                    raise ProviderError("Provider returned no choices")
                message = choices[0].get("message", {})
                if message.get("refusal"):
                    raise ProviderError("Model refused the request: {}".format(message["refusal"]))
                return _parse_json_text(message.get("content"))
            except urllib.error.HTTPError as error:
                detail = error.read().decode("utf-8", errors="replace")[:2000]
                last_error = ProviderError("Provider HTTP {}: {}".format(error.code, detail))
                if error.code < 500 and error.code != 429:
                    break
            except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, ProviderError) as error:
                last_error = error if isinstance(error, ProviderError) else ProviderError(str(error))
            if attempt + 1 < self.retries:
                time.sleep(min(2 ** attempt, 8))
        raise ProviderError(str(last_error or "Unknown provider error"))


class CommandProvider(BaseProvider):
    name = "command"

    def __init__(self, provider_config):
        command = provider_config.get("command")
        if not isinstance(command, list) or not command:
            raise ConfigurationError("Command provider requires provider.command as a non-empty JSON array")
        self.command = [str(item) for item in command]
        self.timeout = int(provider_config.get("timeout_seconds", 120))

    def generate(self, purpose, system_prompt, payload, schema_name, schema):
        request = {
            "purpose": purpose,
            "system_prompt": system_prompt,
            "payload": payload,
            "schema_name": schema_name,
            "schema": schema,
        }
        try:
            process = subprocess.run(
                self.command,
                input=json.dumps(request, ensure_ascii=False),
                text=True,
                capture_output=True,
                timeout=self.timeout,
                check=False,
            )
        except (OSError, subprocess.TimeoutExpired) as error:
            raise ProviderError("Command provider failed: {}".format(error))
        if process.returncode != 0:
            raise ProviderError(
                "Command provider exited {}: {}".format(process.returncode, process.stderr[-2000:])
            )
        return _parse_json_text(process.stdout)


class ReplayProvider(BaseProvider):
    """Deterministic provider for demos and regression tests."""

    name = "replay"

    def __init__(self, replay):
        self.route = replay.get("route")
        self.turns = list(replay.get("turns", []))
        self.calls = []

    @classmethod
    def from_file(cls, path):
        with open(path, "r", encoding="utf-8") as handle:
            return cls(json.load(handle))

    def generate(self, purpose, system_prompt, payload, schema_name, schema):
        self.calls.append(purpose)
        if purpose == "route":
            if self.route is None:
                raise ProviderError("Replay file has no route result")
            return json.loads(json.dumps(self.route))
        if not self.turns:
            raise ProviderError("Replay provider has no remaining decision turns")
        return json.loads(json.dumps(self.turns.pop(0)))


def create_provider(config, replay_path=None):
    if replay_path:
        return ReplayProvider.from_file(replay_path)
    provider_config = config.get("provider", {})
    provider_type = provider_config.get("type", "openai_compatible")
    if provider_type == "openai_compatible":
        return OpenAICompatibleProvider(provider_config)
    if provider_type == "command":
        return CommandProvider(provider_config)
    raise ConfigurationError("Unknown provider type: {}".format(provider_type))
