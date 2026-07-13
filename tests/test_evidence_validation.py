"""Tests for evidence-record validation, including the observation/unit_ref conditional rule."""

from __future__ import annotations

from typing import Any

from product_intelligence import RecordKind, validate_mapping


def test_valid_evidence_passes(valid_evidence: dict[str, Any]) -> None:
    result = validate_mapping(valid_evidence, RecordKind.EVIDENCE_RECORD)
    assert result.ok, result.errors


def test_unknown_tier_fails(valid_evidence: dict[str, Any]) -> None:
    valid_evidence["evidence_tier"] = "E9"  # tiers run E1..E5 only
    result = validate_mapping(valid_evidence, RecordKind.EVIDENCE_RECORD)
    assert not result.ok
    assert any("evidence_tier" in message for message in result.errors)


def test_unknown_type_fails(valid_evidence: dict[str, Any]) -> None:
    valid_evidence["type"] = "tweet"  # not an accepted source type
    result = validate_mapping(valid_evidence, RecordKind.EVIDENCE_RECORD)
    assert not result.ok
    assert any("type" in message for message in result.errors)


def test_observation_requires_unit_ref(valid_evidence: dict[str, Any]) -> None:
    # An observation with a null unit_ref is not reproducible and must fail.
    valid_evidence["unit_ref"] = None
    result = validate_mapping(valid_evidence, RecordKind.EVIDENCE_RECORD)
    assert not result.ok
    assert any("unit_ref" in message for message in result.errors)


def test_non_observation_allows_null_unit_ref(valid_evidence: dict[str, Any]) -> None:
    # A primary source has no unit of analysis; null unit_ref is acceptable.
    valid_evidence["type"] = "primary"
    valid_evidence["evidence_tier"] = "E2"
    valid_evidence["origin"] = "https://example.com/docs (synthetic)"
    valid_evidence["unit_ref"] = None
    result = validate_mapping(valid_evidence, RecordKind.EVIDENCE_RECORD)
    assert result.ok, result.errors


def test_missing_claim_support_fails(valid_evidence: dict[str, Any]) -> None:
    del valid_evidence["claim_support"]
    result = validate_mapping(valid_evidence, RecordKind.EVIDENCE_RECORD)
    assert not result.ok
    assert any("claim_support" in message for message in result.errors)


def test_bad_id_pattern_fails(valid_evidence: dict[str, Any]) -> None:
    valid_evidence["id"] = "Acme Clarify 2026"  # must be kebab-case
    result = validate_mapping(valid_evidence, RecordKind.EVIDENCE_RECORD)
    assert not result.ok
    assert any("id" in message for message in result.errors)


def test_synthetic_must_be_boolean(valid_evidence: dict[str, Any]) -> None:
    valid_evidence["synthetic"] = "yes"  # must be a boolean
    result = validate_mapping(valid_evidence, RecordKind.EVIDENCE_RECORD)
    assert not result.ok
