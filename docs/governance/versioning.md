# Teardown Versioning and Update Policy

Products change; so must teardowns. Versioning makes those changes legible: a reader can see
what state of a product a teardown describes, when it was last updated, and what changed
between versions. This policy defines how teardown versions are numbered, when they change,
and how updates are handled.

## Versioning scheme

Each teardown carries a semantic-style version `MAJOR.MINOR.PATCH`:

- **MAJOR** — the [unit of analysis](../methodology/unit-of-analysis.md) has materially
  changed (new product version, redesign, pricing overhaul, model swap that alters
  behaviour). A major bump means "this now describes a different thing".
- **MINOR** — substantive new findings, added dimensions of coverage, or re-observation that
  changes conclusions, without the unit itself changing.
- **PATCH** — corrections, clarifications, added caveats, confidence adjustments, or evidence
  refreshes that do not change conclusions.

Every teardown also records: `observation_window`, `last_updated`, and `review_by`.

## When to bump

- A **material product change** → MAJOR, usually producing a new observation window and often
  a new teardown record superseding the old.
- **New evidence that changes a conclusion** → MINOR.
- A **correction or caveat** from the [corrections process](corrections-and-disputes.md) →
  PATCH (or MINOR if a conclusion changes).
- A **scheduled re-review** that confirms findings still hold → PATCH with an updated
  `review_by`, so readers see it was re-checked.

## Update discipline

- **No silent edits.** Any change to a published teardown bumps the version and appears in
  its changelog. We never alter a finding while leaving the version and date untouched.
- **Preserve history.** Superseded conclusions remain visible in the changelog; readers can
  see how our understanding evolved. History is not rewritten.
- **Re-observe, do not assume.** An update that claims current behaviour must rest on
  evidence within the recency window (see [recency](../methodology/recency-policy.md)); we do
  not "refresh" a date without refreshing the evidence.

## Handling major changes to a product

When a product changes enough to invalidate the unit of analysis:

1. The existing teardown is frozen as a dated historical record of the prior state.
2. A new MAJOR version (or a new teardown that supersedes the old) describes the current
   state, with its own evidence and observation window.
3. The relationship between old and new versions is recorded, so the history of the product
   as we studied it stays intact.

## Changelog requirements

Each teardown's changelog entry states: the new version, the date, the type of change
(MAJOR/MINOR/PATCH), a short description, and — for conclusion changes — the evidence that
drove it.

## Principle

A teardown is a dated snapshot with a visible history, not a living document that quietly
rewrites itself. Versioning is how we stay honest about *when* something was true and *how*
our understanding changed.
