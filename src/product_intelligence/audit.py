"""Discover and validate every structured record in the repository.

This module powers the ``pi-validate`` command and the CI audit. It walks the repository's
data directories, maps each file to a :class:`~product_intelligence.validation.RecordKind`
by location and name convention, validates it, and reports the results.

Conventions (Phase 1):

- Evidence records: any ``.yaml`` / ``.yml`` / ``.json`` file under ``evidence/``.
- Product metadata: files named ``metadata.{yaml,yml,json}`` under ``library/``.
- Scoring records: files named ``scores.{yaml,yml,json}`` under ``library/``.

During Phase 1 these directories hold no records yet, so a clean audit reports success with
zero records checked. That is the expected, correct outcome and keeps CI meaningful before
any teardown exists.
"""

from __future__ import annotations

import sys
from collections.abc import Iterable, Sequence
from pathlib import Path

from product_intelligence.validation import (
    RecordKind,
    ValidationResult,
    find_repo_root,
    validate_file,
)

_RECORD_EXTENSIONS = (".yaml", ".yml", ".json")
_METADATA_STEMS = frozenset({"metadata"})
_SCORING_STEMS = frozenset({"scores"})


def _iter_data_files(directory: Path) -> Iterable[Path]:
    """Yield record files under ``directory`` in sorted order, ignoring dotfiles."""
    if not directory.is_dir():
        return
    for path in sorted(directory.rglob("*")):
        if not path.is_file():
            continue
        if path.name.startswith("."):
            continue
        if path.suffix.lower() in _RECORD_EXTENSIONS:
            yield path


def discover_records(root: Path) -> list[tuple[Path, RecordKind]]:
    """Return every discoverable record paired with its :class:`RecordKind`.

    Files under ``library/`` that are neither metadata nor scoring records by name are
    ignored, so that narrative files can live alongside structured data without tripping the
    audit.
    """
    discovered: list[tuple[Path, RecordKind]] = []

    for path in _iter_data_files(root / "evidence"):
        discovered.append((path, RecordKind.EVIDENCE_RECORD))

    for path in _iter_data_files(root / "library"):
        stem = path.stem.lower()
        if stem in _METADATA_STEMS:
            discovered.append((path, RecordKind.PRODUCT_METADATA))
        elif stem in _SCORING_STEMS:
            discovered.append((path, RecordKind.SCORING_RECORD))

    return discovered


def run_audit(root: Path | None = None) -> list[ValidationResult]:
    """Validate every discoverable record and return the results in a stable order."""
    resolved_root = root or find_repo_root()
    return [
        validate_file(path, kind, root=resolved_root)
        for path, kind in discover_records(resolved_root)
    ]


def _render_report(results: Sequence[ValidationResult]) -> str:
    """Render a plain-text audit report."""
    lines: list[str] = []
    failures = [result for result in results if not result.ok]

    for result in results:
        status = "PASS" if result.ok else "FAIL"
        lines.append(f"[{status}] {result.kind.value}: {result.source}")
        for message in result.errors:
            lines.append(f"         - {message}")

    lines.append("")
    lines.append(
        f"Audited {len(results)} record(s): "
        f"{len(results) - len(failures)} passed, {len(failures)} failed."
    )
    if not results:
        lines.append("No structured records found yet (expected during Phase 1).")
    return "\n".join(lines)


def main(argv: Sequence[str] | None = None) -> int:
    """Entry point for the ``pi-validate`` command.

    Returns a process exit code: ``0`` when all discovered records validate, ``1`` otherwise.
    """
    _ = argv  # No options in Phase 1; reserved for future flags.
    results = run_audit()
    report = _render_report(results)
    print(report)
    return 0 if all(result.ok for result in results) else 1


if __name__ == "__main__":  # pragma: no cover - exercised via the console script
    sys.exit(main(sys.argv[1:]))
