import hashlib
import json
import os
import tempfile
import uuid
from pathlib import Path

from .storage import utc_now


def _canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


class AuditLog:
    """Append-only hash-chained audit log. Raw business content is excluded by callers."""

    def __init__(self, config, store):
        self.config = config
        self.store = store
        self.path = Path(config["runtime_dir"]) / "audit" / "events.jsonl"
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def append(self, event_type, run_id=None, project_id=None, details=None):
        with self.store.lock("audit"):
            events = self._read_events()
            previous_hash = events[-1]["hash"] if events else "0" * 64
            event = {
                "event_id": "evt_{}".format(uuid.uuid4().hex),
                "timestamp": utc_now(),
                "event_type": event_type,
                "run_id": run_id,
                "project_id": project_id,
                "details": details or {},
                "previous_hash": previous_hash,
            }
            event["hash"] = hashlib.sha256((previous_hash + _canonical(event)).encode("utf-8")).hexdigest()
            self._atomic_append(events + [event])
            return event

    def verify(self):
        previous_hash = "0" * 64
        for index, event in enumerate(self._read_events()):
            stored_hash = event.get("hash")
            unsigned = dict(event)
            unsigned.pop("hash", None)
            expected = hashlib.sha256((previous_hash + _canonical(unsigned)).encode("utf-8")).hexdigest()
            if event.get("previous_hash") != previous_hash:
                return False, "Event {} has an invalid previous_hash".format(index)
            if stored_hash != expected:
                return False, "Event {} has an invalid hash".format(index)
            previous_hash = stored_hash
        return True, "{} audit events verified".format(len(self._read_events()))

    def _read_events(self):
        if not self.path.exists():
            return []
        events = []
        with self.path.open("r", encoding="utf-8") as handle:
            for line in handle:
                if line.strip():
                    events.append(json.loads(line))
        return events

    def _atomic_append(self, events):
        descriptor, temporary = tempfile.mkstemp(prefix=".audit-", dir=str(self.path.parent))
        try:
            os.fchmod(descriptor, 0o600)
            with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
                for event in events:
                    handle.write(_canonical(event) + "\n")
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(temporary, self.path)
        finally:
            if os.path.exists(temporary):
                os.unlink(temporary)
