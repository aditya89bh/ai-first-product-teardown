"""Validation tooling for the AI-First Product Teardown research library.

This package provides machine-readable validation of the structured records that back the
library: product metadata, evidence records and scoring records. It exists so that the
integrity rules described in ``docs/`` and ``frameworks/`` are enforced mechanically, not
just by convention.

The public API is intentionally small:

- :class:`~product_intelligence.validation.RecordKind` -- the kinds of record we validate.
- :func:`~product_intelligence.validation.validate_file` -- validate one record file.
- :func:`~product_intelligence.validation.validate_mapping` -- validate an in-memory mapping.
- :class:`~product_intelligence.validation.ValidationResult` -- the outcome of a validation.
"""

from __future__ import annotations

from product_intelligence.validation import (
    RecordKind,
    ValidationResult,
    validate_file,
    validate_mapping,
)

__all__ = [
    "RecordKind",
    "ValidationResult",
    "validate_file",
    "validate_mapping",
]

__version__ = "0.1.0"
