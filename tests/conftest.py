"""Shared fixtures for the validation test suite.

The fixtures build minimal, schema-valid records as Python mappings. Tests then mutate copies
to exercise specific validation rules, keeping each test focused on one behaviour.
"""

from __future__ import annotations

from typing import Any

import pytest


@pytest.fixture
def valid_metadata() -> dict[str, Any]:
    """A minimal product-metadata record that satisfies the schema. Synthetic data."""
    return {
        "product_name": "Acme Assistant (synthetic)",
        "product_slug": "acme-assistant",
        "teardown_version": "0.1.0",
        "status": "active",
        "unit_of_analysis": {
            "edition": "free web tier",
            "surface": "web app",
            "version_identifier": "build observed 2026-07-01",
            "account_context": "fresh account, memory enabled",
        },
        "observation_window": {"start": "2026-07-01", "end": "2026-07-10"},
        "last_updated": "2026-07-10",
        "review_by": "2026-10-10",
        "authors": ["researcher-one"],
        "conflicts_of_interest": "none",
        "dimensions_covered": ["ux", "memory"],
    }


@pytest.fixture
def valid_evidence() -> dict[str, Any]:
    """A minimal evidence record (first-hand observation) that satisfies the schema."""
    return {
        "id": "acme-clarify-2026-07-02",
        "type": "observation",
        "evidence_tier": "E1",
        "title": "Clarifying question observed on empty input (synthetic)",
        "origin": "first-hand observation",
        "published_date": None,
        "accessed_date": "2026-07-02",
        "archived_ref": None,
        "unit_ref": "acme-assistant-free-web-2026-07",
        "claim_support": "Shows a clarifying question in 5 of 5 runs; not other tiers. (synthetic)",
        "tags": ["ux"],
        "synthetic": True,
        "notes": None,
    }


@pytest.fixture
def valid_scoring() -> dict[str, Any]:
    """A minimal scoring record that satisfies the schema. Synthetic data."""
    return {
        "product_slug": "acme-assistant",
        "teardown_version": "0.1.0",
        "scored_on": "2026-07-10",
        "scores": [
            {
                "dimension": "ux",
                "sub_area": "error recovery and repair",
                "level": "Adequate",
                "confidence": "Moderate",
                "rationale": "Recovery worked but required manual retry. (synthetic)",
                "evidence_refs": ["acme-clarify-2026-07-02"],
            }
        ],
    }
