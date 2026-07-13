"""Evidence-quality audit for the research library.

Where :mod:`product_intelligence.audit` checks that each record is *schema-valid*, this module
checks the *health of the evidence graph* across a product's teardown: that cited evidence
exists, that records are actually used, that high-confidence scores are triangulated, and that
Phase 2 provenance metadata is present.

It is intentionally advisory-aware: broken/contradictory references are **errors** (non-zero
exit), while missing-provenance and staleness are **warnings** (reported, exit still zero) so
the audit is informative without blocking on the legacy `notes`-convention records.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from product_intelligence.validation import find_repo_root, load_record

# Matches evidence citations in teardown prose, e.g. "(ev: cg-memory-delete)" or
# "ev: cg-a, cg-b". Captures the id list text after the marker for further splitting.
_EV_MARKER = re.compile(r"ev:\s*([a-z0-9][a-z0-9,\s-]*)")
_ID = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")

ERROR = "error"
WARNING = "warning"
INFO = "info"


@dataclass(frozen=True)
class AuditFinding:
    """A single evidence-quality finding."""

    severity: str
    code: str
    product: str
    message: str


def _evidence_dir(root: Path) -> Path:
    return root / "evidence"


def _products(root: Path) -> list[str]:
    base = _evidence_dir(root)
    if not base.is_dir():
        return []
    return sorted(p.name for p in base.iterdir() if p.is_dir())


def _load_evidence_ids(root: Path, product: str) -> dict[str, dict[str, Any]]:
    """Return {evidence_id: record} for a product, keyed by the record's own id."""
    records: dict[str, dict[str, Any]] = {}
    for path in sorted((_evidence_dir(root) / product).glob("*.yaml")):
        record = load_record(path)
        record_id = str(record.get("id", path.stem))
        records[record_id] = record
    return records


def _teardown_refs(root: Path, product: str) -> set[str]:
    """Extract evidence ids cited in a product's teardown.md prose."""
    teardown = root / "library" / "products" / product / "teardown.md"
    if not teardown.is_file():
        return set()
    text = teardown.read_text(encoding="utf-8")
    refs: set[str] = set()
    for marker in _EV_MARKER.findall(text):
        refs.update(_ID.findall(marker))
    return refs


def _score_refs(root: Path, product: str) -> tuple[set[str], list[AuditFinding]]:
    """Extract evidence ids cited in scores.yaml and check triangulation invariants."""
    refs: set[str] = set()
    findings: list[AuditFinding] = []
    scores_path = root / "library" / "products" / product / "scores.yaml"
    if not scores_path.is_file():
        return refs, findings
    record = load_record(scores_path)
    scores = record.get("scores", [])
    if not isinstance(scores, list):
        return refs, findings
    for entry in scores:
        if not isinstance(entry, dict):
            continue
        entry_refs = entry.get("evidence_refs", []) or []
        if isinstance(entry_refs, list):
            refs.update(str(r) for r in entry_refs)
        if entry.get("confidence") == "High" and len(entry_refs) < 2:
            findings.append(
                AuditFinding(
                    ERROR,
                    "insufficient-triangulation",
                    product,
                    f"score '{entry.get('sub_area')}' is High confidence with "
                    f"{len(entry_refs)} evidence ref(s); triangulation needs >= 2.",
                )
            )
    return refs, findings


def audit_product(root: Path, product: str) -> list[AuditFinding]:
    """Run all evidence-quality checks for one product."""
    findings: list[AuditFinding] = []
    records = _load_evidence_ids(root, product)
    known_ids = set(records)

    teardown_refs = _teardown_refs(root, product)
    score_refs, score_findings = _score_refs(root, product)
    findings.extend(score_findings)
    cited = teardown_refs | score_refs

    # Broken references: cited somewhere but no matching evidence file.
    for ref in sorted(cited - known_ids):
        findings.append(
            AuditFinding(ERROR, "broken-evidence-ref", product, f"cited id '{ref}' has no record.")
        )

    # Orphan records: a record exists but is cited nowhere.
    for record_id in sorted(known_ids - cited):
        findings.append(
            AuditFinding(
                WARNING, "orphan-evidence", product, f"record '{record_id}' is cited nowhere."
            )
        )

    for record_id, record in sorted(records.items()):
        # Product-identifier consistency: id prefix should match the directory.
        prefix = record_id.split("-", 1)[0]
        expected = {"chatgpt": "cg", "claude": "cl", "perplexity": "px"}.get(product)
        if expected is not None and prefix != expected:
            findings.append(
                AuditFinding(
                    WARNING,
                    "inconsistent-id-prefix",
                    product,
                    f"'{record_id}' does not use the '{expected}-' prefix for {product}.",
                )
            )
        # Required provenance the schema guarantees; re-checked defensively.
        if not record.get("accessed_date"):
            findings.append(
                AuditFinding(
                    ERROR, "missing-access-date", product, f"'{record_id}' lacks accessed_date."
                )
            )
        if not record.get("type"):
            findings.append(
                AuditFinding(
                    ERROR, "missing-source-type", product, f"'{record_id}' lacks a source type."
                )
            )
        # Advisory: structured Phase 2 provenance not yet backfilled.
        if record.get("evidence_directness") is None:
            findings.append(
                AuditFinding(
                    WARNING,
                    "missing-structured-directness",
                    product,
                    f"'{record_id}' has no structured evidence_directness (legacy notes).",
                )
            )
        # Informational: expiry-sensitive records should be re-checked at review time.
        note = str(record.get("notes") or "")
        if record.get("expiry_sensitive") or "expiry_sensitive=true" in note:
            findings.append(
                AuditFinding(
                    INFO, "expiry-sensitive", product, f"'{record_id}' is expiry-sensitive."
                )
            )
    return findings


def run_evidence_audit(root: Path | None = None) -> list[AuditFinding]:
    """Audit every product and return all findings."""
    resolved = root or find_repo_root()
    findings: list[AuditFinding] = []
    for product in _products(resolved):
        findings.extend(audit_product(resolved, product))
    return findings


def render_report(findings: list[AuditFinding]) -> str:
    """Render a grouped, counted plain-text report."""
    order = {ERROR: 0, WARNING: 1, INFO: 2}
    lines: list[str] = []
    for finding in sorted(findings, key=lambda f: (order.get(f.severity, 9), f.product, f.code)):
        lines.append(
            f"[{finding.severity.upper():7}] {finding.product}: {finding.code} — {finding.message}"
        )
    errors = sum(1 for f in findings if f.severity == ERROR)
    warnings = sum(1 for f in findings if f.severity == WARNING)
    infos = sum(1 for f in findings if f.severity == INFO)
    lines.append("")
    lines.append(f"Evidence audit: {errors} error(s), {warnings} warning(s), {infos} info.")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    """Entry point for ``pi-evidence-audit``. Exit code is non-zero only on errors."""
    _ = argv
    findings = run_evidence_audit()
    print(render_report(findings))
    return 1 if any(f.severity == ERROR for f in findings) else 0


if __name__ == "__main__":  # pragma: no cover - exercised via the console script
    import sys

    sys.exit(main(sys.argv[1:]))
