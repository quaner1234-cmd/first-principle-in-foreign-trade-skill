import json
import re
from pathlib import Path

from .errors import SchemaValidationError


def load_schema(schema_root, name):
    path = Path(schema_root) / name
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


class JSONSchemaValidator:
    """Small dependency-free validator for the schema features used by the harness."""

    def validate(self, instance, schema):
        errors = []
        self._check(instance, schema, "$", schema, errors)
        if errors:
            raise SchemaValidationError(errors)
        return instance

    def errors(self, instance, schema):
        errors = []
        self._check(instance, schema, "$", schema, errors)
        return errors

    def _check(self, value, schema, path, root, errors):
        if "$ref" in schema:
            target = self._resolve_ref(schema["$ref"], root)
            self._check(value, target, path, root, errors)
            return

        if "anyOf" in schema:
            matches = 0
            for option in schema["anyOf"]:
                candidate_errors = []
                self._check(value, option, path, root, candidate_errors)
                if not candidate_errors:
                    matches += 1
            if matches == 0:
                errors.append("{}: does not match any allowed schema".format(path))
            return

        if "oneOf" in schema:
            matches = 0
            for option in schema["oneOf"]:
                candidate_errors = []
                self._check(value, option, path, root, candidate_errors)
                if not candidate_errors:
                    matches += 1
            if matches != 1:
                errors.append("{}: must match exactly one schema".format(path))
            return

        if "allOf" in schema:
            for option in schema["allOf"]:
                self._check(value, option, path, root, errors)

        expected_type = schema.get("type")
        if expected_type is not None and not self._is_type(value, expected_type):
            errors.append("{}: expected type {}, got {}".format(path, expected_type, type(value).__name__))
            return

        if "const" in schema and value != schema["const"]:
            errors.append("{}: expected constant {!r}".format(path, schema["const"]))

        if "enum" in schema and value not in schema["enum"]:
            errors.append("{}: value {!r} is not allowed".format(path, value))

        if isinstance(value, dict):
            required = schema.get("required", [])
            for key in required:
                if key not in value:
                    errors.append("{}: missing required property {!r}".format(path, key))
            properties = schema.get("properties", {})
            for key, child in value.items():
                child_path = "{}.{}".format(path, key)
                if key in properties:
                    self._check(child, properties[key], child_path, root, errors)
                elif schema.get("additionalProperties") is False:
                    errors.append("{}: unexpected property".format(child_path))
                elif isinstance(schema.get("additionalProperties"), dict):
                    self._check(child, schema["additionalProperties"], child_path, root, errors)

        if isinstance(value, list):
            if len(value) < schema.get("minItems", 0):
                errors.append("{}: expected at least {} items".format(path, schema["minItems"]))
            if "maxItems" in schema and len(value) > schema["maxItems"]:
                errors.append("{}: expected at most {} items".format(path, schema["maxItems"]))
            if schema.get("uniqueItems"):
                canonical = [json.dumps(item, ensure_ascii=False, sort_keys=True) for item in value]
                if len(canonical) != len(set(canonical)):
                    errors.append("{}: items must be unique".format(path))
            item_schema = schema.get("items")
            if item_schema:
                for index, child in enumerate(value):
                    self._check(child, item_schema, "{}[{}]".format(path, index), root, errors)

        if isinstance(value, str):
            if len(value) < schema.get("minLength", 0):
                errors.append("{}: string is too short".format(path))
            if "maxLength" in schema and len(value) > schema["maxLength"]:
                errors.append("{}: string is too long".format(path))
            if "pattern" in schema and re.search(schema["pattern"], value) is None:
                errors.append("{}: string does not match required pattern".format(path))

        if isinstance(value, (int, float)) and not isinstance(value, bool):
            if "minimum" in schema and value < schema["minimum"]:
                errors.append("{}: value is below minimum {}".format(path, schema["minimum"]))
            if "maximum" in schema and value > schema["maximum"]:
                errors.append("{}: value is above maximum {}".format(path, schema["maximum"]))

    def _resolve_ref(self, reference, root):
        if not reference.startswith("#/"):
            raise ValueError("Only local JSON Schema references are supported: {}".format(reference))
        node = root
        for part in reference[2:].split("/"):
            key = part.replace("~1", "/").replace("~0", "~")
            node = node[key]
        return node

    @staticmethod
    def _is_type(value, expected):
        if isinstance(expected, list):
            return any(JSONSchemaValidator._is_type(value, item) for item in expected)
        mapping = {
            "object": lambda item: isinstance(item, dict),
            "array": lambda item: isinstance(item, list),
            "string": lambda item: isinstance(item, str),
            "integer": lambda item: isinstance(item, int) and not isinstance(item, bool),
            "number": lambda item: isinstance(item, (int, float)) and not isinstance(item, bool),
            "boolean": lambda item: isinstance(item, bool),
            "null": lambda item: item is None,
        }
        return mapping.get(expected, lambda item: True)(value)
