"""Tests for record discovery, file loading, and the repository audit."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest

from product_intelligence import RecordKind, validate_file
from product_intelligence.audit import discover_records, run_audit
from product_intelligence.validation import (
    RecordLoadError,
    find_repo_root,
    load_record,
)


def test_find_repo_root_locates_pyproject() -> None:
    root = find_repo_root()
    assert (root / "pyproject.toml").is_file()
    assert (root / "schemas").is_dir()


def test_repository_audit_passes() -> None:
    # The real repository must always validate: in Phase 1 that means zero records, all ok.
    results = run_audit()
    assert all(result.ok for result in results), [r.errors for r in results if not r.ok]


def test_load_record_reads_yaml(tmp_path: Path, valid_evidence: dict[str, Any]) -> None:
    import yaml

    path = tmp_path / "record.yaml"
    path.write_text(yaml.safe_dump(valid_evidence), encoding="utf-8")
    loaded = load_record(path)
    assert loaded["id"] == valid_evidence["id"]


def test_load_record_reads_json(tmp_path: Path, valid_evidence: dict[str, Any]) -> None:
    path = tmp_path / "record.json"
    path.write_text(json.dumps(valid_evidence), encoding="utf-8")
    loaded = load_record(path)
    assert loaded["id"] == valid_evidence["id"]


def test_load_record_rejects_unknown_extension(tmp_path: Path) -> None:
    path = tmp_path / "record.txt"
    path.write_text("id: x", encoding="utf-8")
    with pytest.raises(RecordLoadError):
        load_record(path)


def test_load_record_rejects_non_mapping(tmp_path: Path) -> None:
    path = tmp_path / "record.yaml"
    path.write_text("- just\n- a\n- list\n", encoding="utf-8")
    with pytest.raises(RecordLoadError):
        load_record(path)


def test_validate_file_reports_invalid_record(
    tmp_path: Path, valid_evidence: dict[str, Any]
) -> None:
    import yaml

    valid_evidence["evidence_tier"] = "E9"  # invalid tier
    path = tmp_path / "bad.yaml"
    path.write_text(yaml.safe_dump(valid_evidence), encoding="utf-8")
    result = validate_file(path, RecordKind.EVIDENCE_RECORD)
    assert not result.ok
    assert result.source == str(path)


def test_discover_records_maps_by_location(tmp_path: Path) -> None:
    # Build a throwaway repo-shaped tree and confirm files map to the right record kinds.
    (tmp_path / "evidence" / "acme").mkdir(parents=True)
    (tmp_path / "library" / "products" / "acme").mkdir(parents=True)
    (tmp_path / "evidence" / "acme" / "ev.yaml").write_text("id: x", encoding="utf-8")
    (tmp_path / "library" / "products" / "acme" / "metadata.yaml").write_text("a: 1", "utf-8")
    (tmp_path / "library" / "products" / "acme" / "scores.yaml").write_text("a: 1", "utf-8")
    (tmp_path / "library" / "products" / "acme" / "teardown.md").write_text("# x", "utf-8")

    kinds = {path.name: kind for path, kind in discover_records(tmp_path)}
    assert kinds["ev.yaml"] is RecordKind.EVIDENCE_RECORD
    assert kinds["metadata.yaml"] is RecordKind.PRODUCT_METADATA
    assert kinds["scores.yaml"] is RecordKind.SCORING_RECORD
    assert "teardown.md" not in kinds  # narrative files are ignored
