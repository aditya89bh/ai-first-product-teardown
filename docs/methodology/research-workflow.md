# Product Teardown Research Workflow

This document defines the end-to-end workflow for producing one teardown. It is the spine
of the methodology: every other methodology document sharpens one step described here. The
workflow is deliberately linear with explicit gates, so that quality is enforced at each
stage rather than inspected only at the end.

Every teardown must be able to answer these seven questions by the time it ships. The
workflow is organised to make each answerable:

1. What is being analysed?
2. Why does it matter?
3. What evidence is required?
4. How is the evidence evaluated?
5. What can be concluded?
6. What cannot be concluded?
7. How can another researcher reproduce or challenge the analysis?

## Stage 0 — Candidate and scope

- Confirm the product meets the [inclusion criteria](inclusion-criteria.md) and clears the
  [prioritisation criteria](selection-criteria.md).
- Fix the [unit of analysis](unit-of-analysis.md): the specific product, edition, surface
  and version window under study.
- Open a teardown record from the [template](../../templates/) and declare any
  [conflicts of interest](../governance/bias-and-conflicts.md).

**Gate:** scope is written down and unambiguous before any analysis begins.

## Stage 1 — Evidence collection

- Gather sources against the [acceptable-sources](source-types.md) rules.
- Record each source as an evidence record using the
  [evidence template](../../templates/) and the
  [citation standard](citation-standard.md).
- Grade each item on the [evidence hierarchy](evidence-hierarchy.md) and note its date
  against the [recency policy](recency-policy.md).

**Gate:** every claim to be made downstream has at least one graded, dated evidence record.

## Stage 2 — Observation

- Where possible, generate **first-hand observations** by using the product directly, and
  record them as observations (not facts about intent).
- Keep observations descriptive: what happened, under what conditions, how reproducibly.
- Label any synthetic or illustrative example explicitly as synthetic.

**Gate:** observations are separated from interpretation and are reproducible as described.

## Stage 3 — Analysis across the six dimensions

- Apply each of the six [frameworks](../../frameworks/) in turn.
- For every statement, classify it as fact, observation, inference or hypothesis per
  [fact-inference-hypothesis](fact-inference-hypothesis.md), and attach a
  [confidence level](confidence-levels.md).
- Apply [triangulation](../governance/triangulation.md) before promoting anything to a
  fact or high-confidence inference.

**Gate:** no unclassified claims; no fact without qualifying evidence.

## Stage 4 — Conclusions and limits

- State what can be concluded and, explicitly, what cannot.
- Record known [limitations and failure modes](../governance/methodology-limitations.md)
  specific to this teardown.

**Gate:** the "cannot be concluded" section is non-empty and honest.

## Stage 5 — Reproducibility and review

- Complete the reproducibility note per
  [reproducibility requirements](../governance/reproducibility.md) so a stranger can
  repeat the work.
- Run all machine validation (schema, lint, types, tests).
- Peer review checks evidence grading, classification and reproducibility — not writing
  style alone.

**Gate:** validation passes and a reviewer other than the author signs off.

## Stage 6 — Publication and lifecycle

- Version the teardown per the [versioning policy](../governance/versioning.md).
- Register it for periodic re-review; changes flow through
  [corrections and disputes](../governance/corrections-and-disputes.md).

## Workflow invariants

- **Evidence precedes claims.** A claim without a prior evidence record is not written.
- **Classification is mandatory.** Every claim is fact, observation, inference or
  hypothesis — never unlabelled.
- **Limits are first-class.** A teardown with no stated limits is incomplete, not
  impressive.
