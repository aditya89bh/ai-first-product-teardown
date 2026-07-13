# Claim Verification Requirements

This document defines the checks a claim must pass before it can appear in a published
teardown. Verification is the gate between "we wrote it down" and "we stand behind it". It
applies to every claim, whether classified as fact, observation, inference or hypothesis —
though the bar differs by type.

## The verification checklist

Every claim must satisfy all applicable items before publication.

1. **Sourced.** The claim links to at least one [evidence record](../../templates/) recorded
   to the [citation standard](../methodology/citation-standard.md). No orphan claims.
2. **Classified.** The claim is labelled fact, observation, inference or hypothesis per
   [fact-inference-hypothesis](../methodology/fact-inference-hypothesis.md).
3. **Graded.** Its supporting evidence carries an E-tier from the
   [evidence hierarchy](../methodology/evidence-hierarchy.md).
4. **Confidence-assigned.** Non-trivial claims carry a
   [confidence level](../methodology/confidence-levels.md) with a one-line rationale.
5. **Scope-matched.** The claim does not exceed what the evidence supports for the declared
   [unit of analysis](../methodology/unit-of-analysis.md).
6. **Recency-checked.** The supporting evidence is within an acceptable age for its type, or
   the claim is flagged as potentially stale (see [recency](../methodology/recency-policy.md)).

## Verification bar by claim type

- **Fact:** requires strong evidence, generally triangulated (see
  [triangulation](triangulation.md)). A claim that cannot be triangulated may still be
  published — but as an inference, not a fact.
- **Observation:** requires a recorded, reproducible unit of analysis and conditions. An
  observation nobody else could reproduce as described is not verified.
- **Inference:** requires explicit reasoning connecting it to underlying facts/observations,
  plus a confidence level. The reasoning itself is reviewable.
- **Hypothesis:** requires only honest labelling as untested and, where possible, a note on
  how it could be tested or refuted.

## Reviewer responsibilities

Verification is checked by a reviewer other than the author. The reviewer confirms that:

- Each cited source actually supports the specific claim (not merely the topic).
- The classification and confidence are justified, not inflated.
- No fact rests on a single uncorroborated source.
- The claim's scope matches the evidence and the unit of analysis.

A reviewer who cannot trace a claim to supporting evidence must send it back, regardless of
how reasonable it sounds.

## Failure handling

- A claim that fails verification is **downgraded** (for example, fact → inference,
  inference → hypothesis) or **removed**, never quietly kept.
- Systematic verification failures in a teardown block its publication until resolved.
- Post-publication verification failures are handled through
  [corrections and disputes](corrections-and-disputes.md).

## Principle

The library's credibility is the sum of its verified claims. One unverified claim presented
as fact costs more trust than ten honest "we don't know"s. When in doubt, verify harder or
claim less.
