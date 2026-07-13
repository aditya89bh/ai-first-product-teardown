# Corrections and Dispute Process

The library optimises for being *correctable*, not for being right the first time. A clear,
low-friction process for challenging and fixing findings is therefore core infrastructure,
not an afterthought. This document defines how anyone can dispute a claim, how corrections
are made, and how the record of changes is kept honest.

## Who can dispute, and what

Anyone — contributor or reader — may dispute:

- A specific **claim** (its accuracy, classification, evidence, or confidence).
- The **evidence** behind a claim (source quality, misreading, staleness).
- The **method** as applied in a teardown (scope, reproducibility, bias).

Disputes are about claims and evidence, never about people (see the
[code of conduct](../../CODE_OF_CONDUCT.md)).

## How to raise a dispute

1. Open a dispute using the project's issue process, identifying the exact claim (by its
   location and, where relevant, the evidence record `id`).
2. State what is wrong and provide **evidence or reasoning**, held to the same standards the
   library uses (see [source types](../methodology/source-types.md) and the
   [evidence hierarchy](../methodology/evidence-hierarchy.md)).
3. Indicate the requested outcome: correction, downgrade, added caveat, or withdrawal.

A dispute without evidence or reasoning is treated as a question, not a dispute.

## How disputes are resolved

- **Triage.** A maintainer confirms the dispute is specific and evidence-backed.
- **Assessment.** The disputed claim is re-checked against its evidence, the
  [verification](claim-verification.md) checklist, and any new evidence supplied.
- **Decision.** One of: uphold (with reasoning), correct, downgrade confidence/classification,
  add a caveat, or withdraw the claim.
- **Independence.** Where a dispute touches a contributor's own work, a different maintainer
  decides.
- **Timeliness.** Disputes are acknowledged promptly; material factual disputes are
  prioritised over stylistic ones.

## How corrections are recorded

Corrections are transparent, never silent:

1. The change is made in the teardown and its version is bumped per the
   [versioning policy](versioning.md).
2. A **correction note** records what changed, why, and on what evidence, with the date.
3. Significant corrections are surfaced in the teardown's changelog so a reader can see the
   history, not just the current state.
4. If a claim is withdrawn, the withdrawal and its reason remain visible; we do not erase the
   fact that we once made the claim.

## Standard of correction

- We correct toward the evidence, even when it is inconvenient or contradicts a prior public
  statement.
- We do not "balance" a correction to save face; if we were wrong, the note says so plainly.
- Repeated, systematic errors trigger a review of the method or the contributor's process,
  not just the individual claim.

## Principle

Every published claim is provisional and challengeable. The measure of the library is not how
rarely it errs but how quickly, transparently and completely it corrects. A visible
correction strengthens trust; a hidden one destroys it.
