# The Evidence Hierarchy

Not all evidence is equal. The evidence hierarchy ranks *kinds* of evidence by how directly
and reliably they support a claim. Every evidence record is graded on this hierarchy, and a
claim's maximum defensible confidence is bounded by the strength of the evidence beneath it.

The hierarchy answers one question for a reader: *how close is this evidence to the thing it
claims, and how easily could it be wrong?*

## The tiers

Tiers run from **E1 (strongest)** to **E5 (weakest)**. Lower tiers are not forbidden; they
are simply weaker, and claims resting only on them cannot reach high confidence.

### E1 — Direct, reproducible first-hand observation

The researcher directly observed the behaviour under a recorded [unit of
analysis](unit-of-analysis.md), and the observation is reproducible as described. Example:
running a documented prompt and recording the product's response and settings.

- Strongest support for claims about *what the product does*.
- Bounded by non-determinism: a single observation is a sample, not a guarantee. Repetition
  and [triangulation](../governance/triangulation.md) strengthen it.

### E2 — Primary published material from the product owner

Official documentation, changelogs, product pages, or on-the-record statements from the
makers. Strong for claims about *stated* design, features and intent — but stated intent is
not observed behaviour, and the two must not be conflated.

### E3 — Independent, verifiable third-party reporting

Reputable independent reporting or analysis that itself cites checkable evidence. Strength
depends on the source's rigour and on our ability to verify its underlying evidence.

### E4 — Corroborated user reports

Multiple independent user accounts describing the same behaviour. Useful signal, especially
for behaviour we cannot reproduce ourselves, but individual reports are unverified and
prone to selection effects. Requires corroboration to carry weight.

### E5 — Single, unverified, or anecdotal reports

A lone user report, an uncorroborated claim, or informal commentary. May motivate a
hypothesis or a line of inquiry, but cannot on its own support a fact or a high-confidence
inference.

## Rules for using the hierarchy

1. **Grade every record.** No evidence record enters the library without an E-tier.
2. **Confidence is capped by evidence.** A claim resting only on E4/E5 cannot be presented
   as a fact or as high confidence (see [confidence levels](confidence-levels.md)).
3. **Prefer observation for behaviour, primary sources for intent.** Match the evidence type
   to the claim type; do not use a product page to prove behaviour, or a single run to prove
   intent.
4. **Triangulate before promoting.** Promoting a claim to a fact generally requires
   agreement across independent evidence, ideally spanning tiers (see
   [triangulation](../governance/triangulation.md)).
5. **Record limitations of the evidence, not just its tier.** Note sample size, date,
   account context and anything that would let a reader judge fragility.

## What the hierarchy is not

It is not a substitute for judgement. A high tier does not make a claim true, and a low tier
does not make it false — it calibrates how confidently the claim may be stated and how much
corroboration it needs.

## Phase 2 addendum (2026-07-13): evidence directness and scope

*Added after the pilot stress-test (see `docs/research/phase-2-methodology-stress-test.md`,
finding F2). This clarifies, and does not replace, the tiers above.*

- **A primary source (E2) that is the vendor's own documentation is *vendor self-report*, not
  observed behaviour.** A documented feature supports the fact *that the vendor states it*, and
  is at most an **inference** about actual behaviour until directly observed. Record this with
  the evidence record's `evidence_directness` field (`direct` / `vendor-self-reported` /
  `indirect`).
- **Confidence attaches to the specific claim.** "High confidence that a feature is documented"
  is **not** "High confidence that the behaviour occurs". State which you mean.
- **Scope every claim to a plan and region.** A finding on one plan/region is not evidence about
  another (e.g. ChatGPT Plus at $20 US vs ₹1,999 in an INR render are recorded separately, never
  merged).
- **Thin documentation yields `Not rated`, never a low score** — missing evidence is never
  converted into a negative finding.
