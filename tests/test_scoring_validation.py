"""Tests for scoring-record validation, focusing on the no-false-precision guarantees."""

from __future__ import annotations

from typing import Any

from product_intelligence import RecordKind, validate_mapping


def test_valid_scoring_passes(valid_scoring: dict[str, Any]) -> None:
    result = validate_mapping(valid_scoring, RecordKind.SCORING_RECORD)
    assert result.ok, result.errors


def test_numeric_level_is_rejected(valid_scoring: dict[str, Any]) -> None:
    # Numeric scores are false precision and must be impossible to record.
    valid_scoring["scores"][0]["level"] = 7
    result = validate_mapping(valid_scoring, RecordKind.SCORING_RECORD)
    assert not result.ok
    assert any("level" in message for message in result.errors)


def test_out_of_scale_level_is_rejected(valid_scoring: dict[str, Any]) -> None:
    valid_scoring["scores"][0]["level"] = "Excellent"  # not in the ordinal scale
    result = validate_mapping(valid_scoring, RecordKind.SCORING_RECORD)
    assert not result.ok


def test_high_confidence_requires_triangulation(valid_scoring: dict[str, Any]) -> None:
    # A single evidence record cannot support High confidence.
    valid_scoring["scores"][0]["confidence"] = "High"
    valid_scoring["scores"][0]["evidence_refs"] = ["only-one-source"]
    result = validate_mapping(valid_scoring, RecordKind.SCORING_RECORD)
    assert not result.ok
    assert any("evidence_refs" in message for message in result.errors)


def test_high_confidence_with_two_sources_passes(valid_scoring: dict[str, Any]) -> None:
    valid_scoring["scores"][0]["confidence"] = "High"
    valid_scoring["scores"][0]["evidence_refs"] = ["source-a", "source-b"]
    result = validate_mapping(valid_scoring, RecordKind.SCORING_RECORD)
    assert result.ok, result.errors


def test_not_rated_requires_speculative_confidence(valid_scoring: dict[str, Any]) -> None:
    valid_scoring["scores"][0]["level"] = "Not rated"
    valid_scoring["scores"][0]["confidence"] = "Moderate"  # must be Speculative
    result = validate_mapping(valid_scoring, RecordKind.SCORING_RECORD)
    assert not result.ok


def test_score_without_evidence_fails(valid_scoring: dict[str, Any]) -> None:
    valid_scoring["scores"][0]["evidence_refs"] = []
    result = validate_mapping(valid_scoring, RecordKind.SCORING_RECORD)
    assert not result.ok
    assert any("evidence_refs" in message for message in result.errors)


def test_empty_scores_list_fails(valid_scoring: dict[str, Any]) -> None:
    valid_scoring["scores"] = []
    result = validate_mapping(valid_scoring, RecordKind.SCORING_RECORD)
    assert not result.ok


def test_composite_score_field_is_rejected(valid_scoring: dict[str, Any]) -> None:
    # An aggregate/overall field is forbidden; the schema is closed.
    valid_scoring["overall"] = "Strong"
    result = validate_mapping(valid_scoring, RecordKind.SCORING_RECORD)
    assert not result.ok
