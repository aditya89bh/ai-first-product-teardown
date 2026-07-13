"""Core validation logic for structured research records.

Records are stored as YAML or JSON and validated against JSON Schema definitions kept in the
repository's ``schemas/`` directory. Each :class:`RecordKind` maps to exactly one schema.

The module is deliberately free of side effects at import time and resolves the repository
root by walking upward from a known location, so it works both from an editable install and
from a checkout.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator


class RecordKind(Enum):
    """A kind of structured record, paired with the schema that validates it."""

    PRODUCT_METADATA = "product-metadata"
    EVIDENCE_RECORD = "evidence-record"
    SCORING_RECORD = "scoring-record"

    @property
    def schema_filename(self) -> str:
        """Return the schema file name for this record kind."""
        return f"{self.value}.schema.json"


@dataclass(frozen=True)
class ValidationResult:
    """The outcome of validating a single record.

    Attributes:
        kind: The record kind that was validated against.
        source: A human-readable description of what was validated (file path or ``"<mapping>"``).
        errors: Human-readable validation error messages; empty when the record is valid.
    """

    kind: RecordKind
    source: str
    errors: tuple[str, ...]

    @property
    def ok(self) -> bool:
        """Return ``True`` when the record passed validation."""
        return not self.errors


class SchemaError(RuntimeError):
    """Raised when a schema cannot be located or loaded."""


class RecordLoadError(RuntimeError):
    """Raised when a record file cannot be read or parsed."""


def find_repo_root(start: Path | None = None) -> Path:
    """Locate the repository root by walking upward looking for ``pyproject.toml``.

    Args:
        start: Directory to begin the search from. Defaults to this file's location.

    Returns:
        The first ancestor directory (inclusive of ``start``) containing ``pyproject.toml``.

    Raises:
        SchemaError: If no ancestor contains ``pyproject.toml``.
    """
    origin = (start or Path(__file__)).resolve()
    for candidate in (origin, *origin.parents):
        if (candidate / "pyproject.toml").is_file():
            return candidate
    raise SchemaError("could not locate repository root (no pyproject.toml found)")


def schemas_dir(root: Path | None = None) -> Path:
    """Return the directory holding JSON Schema definitions."""
    return (root or find_repo_root()) / "schemas"


def load_schema(kind: RecordKind, root: Path | None = None) -> dict[str, Any]:
    """Load and return the JSON Schema mapping for a record kind.

    Raises:
        SchemaError: If the schema file is missing or is not valid JSON.
    """
    path = schemas_dir(root) / kind.schema_filename
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:  # pragma: no cover - filesystem errors are environment-specific
        raise SchemaError(f"cannot read schema {path}: {exc}") from exc
    try:
        loaded: Any = json.loads(text)
    except json.JSONDecodeError as exc:
        raise SchemaError(f"schema {path} is not valid JSON: {exc}") from exc
    if not isinstance(loaded, dict):
        raise SchemaError(f"schema {path} must be a JSON object")
    return loaded


def load_record(path: Path) -> dict[str, Any]:
    """Load a record from a ``.yaml``/``.yml`` or ``.json`` file into a mapping.

    Raises:
        RecordLoadError: If the file cannot be read, parsed, or is not a mapping.
    """
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise RecordLoadError(f"cannot read record {path}: {exc}") from exc

    suffix = path.suffix.lower()
    try:
        if suffix in {".yaml", ".yml"}:
            loaded: Any = yaml.safe_load(text)
        elif suffix == ".json":
            loaded = json.loads(text)
        else:
            raise RecordLoadError(f"unsupported record extension {path.suffix!r} for {path}")
    except (yaml.YAMLError, json.JSONDecodeError) as exc:
        raise RecordLoadError(f"cannot parse record {path}: {exc}") from exc

    if not isinstance(loaded, dict):
        raise RecordLoadError(f"record {path} must be a mapping at the top level")
    return loaded


def _format_error_path(absolute_path: Any) -> str:
    """Render a jsonschema error path like ``scores[0].level`` for readable messages."""
    parts: list[str] = []
    for element in absolute_path:
        if isinstance(element, int):
            parts.append(f"[{element}]")
        elif parts:
            parts.append(f".{element}")
        else:
            parts.append(str(element))
    return "".join(parts) or "<root>"


def validate_mapping(
    data: dict[str, Any],
    kind: RecordKind,
    *,
    source: str = "<mapping>",
    root: Path | None = None,
) -> ValidationResult:
    """Validate an in-memory mapping against the schema for ``kind``.

    All schema violations are collected (not just the first), sorted for stable output, and
    returned as human-readable messages.
    """
    schema = load_schema(kind, root)
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(data), key=lambda err: list(err.absolute_path))
    messages = tuple(
        f"{_format_error_path(error.absolute_path)}: {error.message}" for error in errors
    )
    return ValidationResult(kind=kind, source=source, errors=messages)


def validate_file(
    path: Path,
    kind: RecordKind,
    *,
    root: Path | None = None,
) -> ValidationResult:
    """Load a record file and validate it against the schema for ``kind``.

    Load or parse failures are returned as a failing :class:`ValidationResult` rather than
    raised, so that a batch audit can report every problematic file in one pass.
    """
    try:
        data = load_record(path)
    except RecordLoadError as exc:
        return ValidationResult(kind=kind, source=str(path), errors=(str(exc),))
    return validate_mapping(data, kind, source=str(path), root=root)
