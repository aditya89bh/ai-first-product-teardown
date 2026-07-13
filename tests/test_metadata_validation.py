"""Tests for product-metadata validation: valid records pass, invalid records fail clearly."""

from __future__ import annotations

from typing import Any

from product_intelligence import RecordKind, validate_mapping


def test_valid_metadata_passes(valid_metadata: dict[str, Any]) -> None:
    result = validate_mapping(valid_metadata, RecordKind.PRODUCT_METADATA)
    assert result.ok, result.errors
    assert result.errors == ()


def test_missing_required_field_fails(valid_metadata: dict[str, Any]) -> None:
    del valid_metadata["product_name"]
    result = validate_mapping(valid_metadata, RecordKind.PRODUCT_METADATA)
    assert not result.ok
    assert any("product_name" in message for message in result.errors)


def test_bad_slug_pattern_fails(valid_metadata: dict[str, Any]) -> None:
    valid_metadata["product_slug"] = "Acme Assistant"  # spaces and capitals are not allowed
    result = validate_mapping(valid_metadata, RecordKind.PRODUCT_METADATA)
    assert not result.ok
    assert any("product_slug" in message for message in result.errors)


def test_bad_version_pattern_fails(valid_metadata: dict[str, Any]) -> None:
    valid_metadata["teardown_version"] = "1.0"  # must be MAJOR.MINOR.PATCH
    result = validate_mapping(valid_metadata, RecordKind.PRODUCT_METADATA)
    assert not result.ok
    assert any("teardown_version" in message for message in result.errors)


def test_unknown_status_fails(valid_metadata: dict[str, Any]) -> None:
    valid_metadata["status"] = "published"  # not in the enum
    result = validate_mapping(valid_metadata, RecordKind.PRODUCT_METADATA)
    assert not result.ok
    assert any("status" in message for message in result.errors)


def test_additional_property_fails(valid_metadata: dict[str, Any]) -> None:
    valid_metadata["overall_score"] = 7  # composite scores are forbidden; schema is closed
    result = validate_mapping(valid_metadata, RecordKind.PRODUCT_METADATA)
    assert not result.ok


def test_incomplete_unit_of_analysis_fails(valid_metadata: dict[str, Any]) -> None:
    del valid_metadata["unit_of_analysis"]["surface"]
    result = validate_mapping(valid_metadata, RecordKind.PRODUCT_METADATA)
    assert not result.ok
    assert any("surface" in message for message in result.errors)


def test_empty_authors_fails(valid_metadata: dict[str, Any]) -> None:
    valid_metadata["authors"] = []
    result = validate_mapping(valid_metadata, RecordKind.PRODUCT_METADATA)
    assert not result.ok
    assert any("authors" in message for message in result.errors)


def test_invalid_dimension_fails(valid_metadata: dict[str, Any]) -> None:
    valid_metadata["dimensions_covered"] = ["ux", "pricing"]  # 'pricing' is not a dimension
    result = validate_mapping(valid_metadata, RecordKind.PRODUCT_METADATA)
    assert not result.ok
