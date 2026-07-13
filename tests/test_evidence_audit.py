"""Tests for the evidence-quality audit."""

from __future__ import annotations

from pathlib import Path

import yaml

from product_intelligence.evidence_audit import (
    ERROR,
    WARNING,
    audit_product,
    run_evidence_audit,
)


def _write_evidence(path: Path, record_id: str, **overrides: object) -> None:
    record: dict[str, object] = {
        "id": record_id,
        "type": "primary",
        "evidence_tier": "E2",
        "title": "t",
        "origin": "https://example.com",
        "accessed_date": "2026-07-13",
        "claim_support": "supports x",
        "synthetic": False,
    }
    record.update(overrides)
    path.write_text(yaml.safe_dump(record), encoding="utf-8")


def _build_product(root: Path, product: str) -> Path:
    ev = root / "evidence" / product
    ev.mkdir(parents=True)
    (root / "library" / "products" / product).mkdir(parents=True)
    return ev


def test_real_repository_evidence_audit_has_no_errors() -> None:
    findings = run_evidence_audit()
    errors = [f for f in findings if f.severity == ERROR]
    assert errors == [], [f.message for f in errors]


def test_broken_reference_is_an_error(tmp_path: Path) -> None:
    ev = _build_product(tmp_path, "chatgpt")
    _write_evidence(ev / "cg-a.yaml", "cg-a")
    # Teardown cites an id that does not exist.
    (tmp_path / "library" / "products" / "chatgpt" / "teardown.md").write_text(
        "See (ev: cg-a) and (ev: cg-missing).", encoding="utf-8"
    )
    findings = audit_product(tmp_path, "chatgpt")
    codes = {(f.code, f.severity) for f in findings}
    assert ("broken-evidence-ref", ERROR) in codes


def test_orphan_record_is_a_warning(tmp_path: Path) -> None:
    ev = _build_product(tmp_path, "claude")
    _write_evidence(ev / "cl-a.yaml", "cl-a")
    _write_evidence(ev / "cl-orphan.yaml", "cl-orphan")
    (tmp_path / "library" / "products" / "claude" / "teardown.md").write_text(
        "Only (ev: cl-a) is cited.", encoding="utf-8"
    )
    findings = audit_product(tmp_path, "claude")
    orphans = [f for f in findings if f.code == "orphan-evidence"]
    assert any("cl-orphan" in f.message and f.severity == WARNING for f in orphans)


def test_high_confidence_single_ref_flagged(tmp_path: Path) -> None:
    ev = _build_product(tmp_path, "perplexity")
    _write_evidence(ev / "px-a.yaml", "px-a")
    (tmp_path / "library" / "products" / "perplexity" / "teardown.md").write_text(
        "(ev: px-a)", encoding="utf-8"
    )
    scores = {
        "product_slug": "perplexity",
        "teardown_version": "0.1.0",
        "scored_on": "2026-07-13",
        "scores": [
            {
                "dimension": "trust",
                "sub_area": "x",
                "level": "Strong",
                "confidence": "High",
                "rationale": "r",
                "evidence_refs": ["px-a"],
            }
        ],
    }
    (tmp_path / "library" / "products" / "perplexity" / "scores.yaml").write_text(
        yaml.safe_dump(scores), encoding="utf-8"
    )
    findings = audit_product(tmp_path, "perplexity")
    assert any(f.code == "insufficient-triangulation" and f.severity == ERROR for f in findings)


def test_missing_directness_is_a_warning(tmp_path: Path) -> None:
    ev = _build_product(tmp_path, "chatgpt")
    _write_evidence(ev / "cg-a.yaml", "cg-a")  # no evidence_directness field
    (tmp_path / "library" / "products" / "chatgpt" / "teardown.md").write_text(
        "(ev: cg-a)", encoding="utf-8"
    )
    findings = audit_product(tmp_path, "chatgpt")
    assert any(f.code == "missing-structured-directness" for f in findings)
