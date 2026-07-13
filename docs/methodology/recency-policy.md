# Research Recency Policy

AI-first products change quickly, and often silently. Evidence about them has a shelf life.
This policy defines how we treat the age of evidence, when findings must be re-checked, and
how staleness is communicated to readers. The goal is that a reader always knows *as of when*
a finding was true.

## Core principle

**Every finding is dated, and its age is part of its meaning.** A claim is not "true"; it is
"true as observed on a date, for a stated unit of analysis". Detaching a finding from its
date is a misrepresentation.

## Freshness expectations by evidence type

- **First-hand observations (E1):** treated as a dated snapshot. Because behaviour is
  non-deterministic and models change silently, observations lose force with age faster than
  most other evidence.
- **Primary published material (E2):** ages more slowly for *stated* design and pricing, but
  can be invalidated by a newer release or changelog; always check for a more recent version.
- **Independent reporting and research (E3):** weighted by both quality and date; a rigorous
  but old report may still be superseded by product changes.
- **User reports (E4/E5):** most volatile; treat older reports as weak and re-corroborate
  before relying on them.

## Re-review triggers

A teardown or claim must be re-checked when any of these occurs:

1. **Scheduled review** falls due (each teardown carries a review-by date).
2. **A material product change** is observed or announced (new version, pricing change,
   redesign, model swap).
3. **A dispute or correction** challenges a dated finding.
4. **Cross-checking for a comparison** surfaces a discrepancy with newer evidence.

## Communicating staleness to readers

- Every teardown shows its **observation window**, its **last-updated date**, and its
  **review-by date**.
- Findings that rest on evidence older than their type's comfortable window are flagged as
  **potentially stale** and their confidence is reduced accordingly.
- When a product is known to have changed since the observation window, the teardown carries
  a prominent notice until it is re-reviewed and re-versioned.

## Interaction with confidence and versioning

- Age is one input to the [confidence level](confidence-levels.md): older evidence lowers
  confidence, all else equal.
- A material change that invalidates the [unit of analysis](unit-of-analysis.md) triggers a
  new version under the [versioning policy](../governance/versioning.md), rather than a quiet
  edit.

## What we do not do

- We do not silently update findings to look current without re-gathering evidence.
- We do not present old observations as if they were made today.
- We do not treat "it probably still works this way" as evidence; that is a hypothesis until
  re-observed.
