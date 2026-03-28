from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from jsonschema import Draft7Validator


@dataclass(slots=True)
class ValidationResult:
    is_valid: bool
    errors: list[str]


class ResumeValidator:
    def __init__(self, schema: dict[str, Any]) -> None:
        self._validator = Draft7Validator(schema)

    def validate(self, payload: dict[str, Any]) -> ValidationResult:
        errors = sorted(self._validator.iter_errors(payload), key=lambda error: list(error.path))
        messages = [f"{list(error.path)} {error.message}" for error in errors]
        return ValidationResult(is_valid=not messages, errors=messages)


def local_schema_guardrails() -> dict[str, Any]:
    return {
        "type": "object",
        "required": ["basics", "work"],
        "properties": {
            "basics": {"type": "object"},
            "work": {"type": "array"},
            "education": {"type": "array"},
            "skills": {"type": "array"},
            "certificates": {"type": "array"},
            "meta": {"type": "object"},
        },
    }
