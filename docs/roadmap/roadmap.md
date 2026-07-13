# Roadmap

This roadmap describes how the library grows from foundation to a mature, searchable
research institution. It targets approximately **500 meaningful commits** across six phases.
Commit counts are planning estimates, not quotas: no phase should manufacture filler
commits to hit a number. One meaningful, reviewable task equals one commit throughout.

## Principles that hold across all phases

- Method changes are slow and documented; analysis changes are versioned and dated.
- No teardown ships without graded evidence and a reproducibility note.
- Every phase ends with a full validation run (tests, lint, types, schema validation).

## Phase 1 — Foundation *(this phase, ~50 commits)*

Establish repository identity, research methodology, governance, analytical framework
foundations, structured-data templates, machine-readable schemas, validation tooling and
CI. **No product teardowns are produced in this phase.**

Exit criteria: `pytest`, `ruff check .` and `mypy src` all pass; all schemas and sample
records validate; documentation cross-links resolve; CI is green.

## Phase 2 — First teardowns and method hardening *(~90 commits)*

Produce the first small set of full product teardowns end to end, using the Phase 1
method. Treat these as stress tests: every place the method proves awkward becomes a
documented method fix. Build the evidence corpus these teardowns depend on.

Exit criteria: several complete, validated teardowns; a documented list of method changes
their production forced; evidence records fully linked and validated.

## Phase 3 — Framework deepening *(~110 commits)*

Deepen each of the six analytical frameworks from foundation to detailed rubric, informed
by what Phase 2 revealed. Add sub-dimensions, worked indicators, and clearer scoring
guidance while continuing to prevent false precision.

Exit criteria: each framework has detailed, evidenced guidance and at least one teardown
exercising every sub-dimension.

## Phase 4 — Comparison and synthesis *(~90 commits)*

Build cross-product comparisons and thematic syntheses on top of the teardown corpus.
Formalise comparison principles into repeatable comparison records. Surface patterns and
anti-patterns that only appear across products.

Exit criteria: validated comparison records; synthesis documents that cite only existing,
graded evidence.

## Phase 5 — Tooling, search and machine-readable access *(~110 commits)*

Build the reader-facing surface deferred from Phase 1: search, indexing, and a way to
browse the library by product, dimension or evidence grade. Harden the tooling into a
maintainable application.

Exit criteria: a working search/browse surface backed by the validated records; tooling
under test and CI.

## Phase 6 — Maintenance, governance at scale, and community *(~50 commits)*

Operationalise corrections, disputes, versioning and contributor onboarding at scale.
Establish review cadences and archival of deprecated teardowns. Turn governance documents
into running processes.

Exit criteria: a documented, exercised maintenance cadence; an active corrections/dispute
process; contributor pathways proven by real contributions.

## Sequencing rationale

Method precedes analysis, analysis precedes comparison, and comparison precedes the reader
product. Building in this order means each layer rests on a validated one beneath it, and
the most durable assets (method and evidence) are built before the most volatile ones
(specific teardowns and UI).
