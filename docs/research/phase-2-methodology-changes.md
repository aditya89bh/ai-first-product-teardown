# Phase 2 Methodology Changes

This log records every methodology change made as a result of Phase 2, with its justification
and the stress-test finding it addresses. Changes are made **only where Phase 2 evidence
demonstrated a real need**. Phase 1 assumptions are not silently rewritten: substantive
additions are marked as dated **Phase 2 addenda** in the affected documents, leaving the
original reasoning intact and visible.

## Principle applied

- **Additive, not destructive.** No Phase 1 document was rewritten; clarifications are appended
  as clearly-labelled addenda.
- **Evidence-gated.** Each change cites the stress-test finding
  (`phase-2-methodology-stress-test.md`) that motivated it.
- **Deferred where uncertain.** Where a change would be premature, it is recorded as a Phase 3
  candidate rather than made now.

## Changes made in Phase 2

### C1 — Evidence-directness clarification (addresses F2)
- **Change:** added a dated Phase 2 addendum to
  [`docs/methodology/evidence-hierarchy.md`](../methodology/evidence-hierarchy.md) stating that
  a primary/E2 source that is the vendor's own documentation is **vendor self-report**, and that
  confidence must attach to the *specific claim* — "High that a feature is documented" is not
  "High that the behaviour occurs".
- **Justification:** F2 was the largest over-claiming risk; the distinction had to be maintained
  by hand throughout the pilot. Making it explicit reduces future error.

### C2 — Plan/region scoping reminder (addresses F5, F6)
- **Change:** the addendum also reinforces that findings are scoped to a **plan** and **region**
  and must never be merged across them (e.g. ChatGPT $20 US vs ₹1,999 INR).
- **Justification:** region-localised pricing nearly produced a false contradiction; explicit
  scoping prevents it.

### C3 — "Not rated over negative" reinforcement (addresses F7)
- **Change:** documented in the stress test and enforced by the new evidence audit (commit 48):
  thin documentation yields `Not rated`/`Speculative`, never a low score. No rule changed — this
  restates and now *mechanically checks* an existing Phase 1 rule.
- **Justification:** the temptation to convert gaps into negatives recurred; a check makes the
  existing rule enforceable.

## Changes deliberately NOT made (recorded for discipline)

- **No change to the six frameworks' substance.** They held; deepening is Phase 3 work.
- **No change to the confidence rubric's levels.** The four levels sufficed; only the
  *attachment* of confidence to a claim needed clarifying (C1).
- **No new comparison rules.** The Phase 1 comparison principles held; F6 was handled by
  explicit per-claim scope statements, not a rule change.

## Schema and tooling changes (separate commits)

The schema and tooling needs (F1, F3, F5, F8) are implemented in the schema/validator/audit
commits that follow this one, because they are code changes rather than methodology text:

- Evidence-record schema gains optional Phase 2 fields (commit 46).
- Tests cover the new fields (commit 47).
- An evidence-quality audit reports gaps, missing metadata and unsupported claims (commit 48).

## Deferred to Phase 3 (candidates, not commitments)

- A structured `basis` field on scores ("documented" vs "observed") (F8).
- A first-class evidence-gap record type distinct from evidence records (F3), if the prose gap
  register proves insufficient at scale.
