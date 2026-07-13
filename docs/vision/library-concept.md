# The Product Intelligence Library Concept

## Definition

A **Product Intelligence Library** is a structured, evidence-first archive that studies
products as *systems of behaviour and value*, rather than as feature lists. Each entry is
built from graded evidence, follows a shared analytical method, and is stored in both
human-readable and machine-readable form so it can be searched, compared and validated.

"Product intelligence" here means *disciplined knowledge about how a product behaves and
why it matters* — closer to field research than to product reviewing.

## The three layers

The library is organised as three layers, from most durable to most volatile:

1. **Method layer** (`docs/`, `frameworks/`, `schemas/`, `templates/`).
   The vocabulary, evidence standards and analytical frameworks. Changes slowly and
   deliberately. This is the intellectual asset.
2. **Analysis layer** (`library/`).
   Teardowns and comparisons produced by applying the method. Changes as products change;
   versioned and dated.
3. **Evidence layer** (`evidence/`).
   The graded, sourced records that every claim in the analysis layer points to. This is
   what makes the analysis checkable.

A conclusion in the analysis layer is only as strong as the evidence layer beneath it and
the method layer above it. Keeping the three separate is what lets a reader audit any
claim back to its source.

## Design commitments

- **Atomic records.** One evidence record captures one claim from one source. One teardown
  covers one product. Small units are easier to verify, cite and correct.
- **Comparability by construction.** Because every teardown uses the same six dimensions
  and templates, cross-product comparison is a lookup, not a re-interpretation.
- **Separation of concerns.** Facts, inferences and hypotheses live in labelled sections
  everywhere, so a reader always knows which they are reading.
- **Dual audience.** Markdown serves human readers; JSON/YAML plus schemas serve tooling
  and future search. Neither is an afterthought.

## Why "library" rather than "database" or "blog"

- A **blog** optimises for freshness and voice; it does not accumulate into a checkable
  whole.
- A **database** optimises for structure but tends to strip out reasoning and nuance.
- A **library** keeps the reasoning, the evidence and the structure together, and is
  designed to be *consulted* over years by many readers with different needs.

## Relationship to the rest of the repository

This concept is the organising idea the whole repository serves. The
[vision](vision.md) states why it exists; the [methodology](../methodology/) states how
entries are produced; the [frameworks](../../frameworks/) supply the analytical lenses;
and the [schemas](../../schemas/) and [templates](../../templates/) enforce the structure
that makes the library durable and searchable.
