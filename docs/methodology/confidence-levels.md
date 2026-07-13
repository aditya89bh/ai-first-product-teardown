# The Confidence-Level Rubric

Every inference and every non-obvious fact carries a confidence level. Confidence expresses
*how sure we are*, given the evidence, its strength, its age, and how well it triangulates.
It is deliberately coarse: fine-grained confidence numbers would be false precision (see
[scoring false precision](../../frameworks/scoring-false-precision.md)).

## The levels

We use four ordered levels. Each has explicit entry conditions so that two researchers apply
them consistently.

### High

- Supported by strong evidence — typically E1/E2 on the
  [evidence hierarchy](evidence-hierarchy.md) — that is **triangulated** across independent
  sources or repeated observations.
- Recent enough that staleness is not a concern (see [recency](recency-policy.md)).
- No material unresolved dispute.
- Appropriate for statements presented as facts.

### Moderate

- Supported by reasonable evidence but with a real gap: a single strong source not yet
  corroborated, or good corroboration among mid-tier sources.
- Some staleness or scope limitation exists but does not undermine the core claim.
- Appropriate for most well-founded inferences.

### Low

- Supported only by weak or partial evidence (for example, uncorroborated E4), or by strong
  evidence that is significantly stale or narrow in scope.
- The claim is plausible but fragile; a modest amount of new evidence could overturn it.
- Must be clearly flagged; not suitable to present as a fact.

### Speculative

- Not yet supported enough to be an inference. This is the confidence attached to a
  [hypothesis](fact-inference-hypothesis.md).
- Included to guide future research, explicitly labelled as untested.

## Assigning a level

Confidence is a judgement over four inputs, considered together:

1. **Evidence tier** — stronger tiers permit higher confidence.
2. **Triangulation** — independent agreement raises confidence; a lone source caps it.
3. **Recency** — older evidence lowers confidence for volatile properties.
4. **Scope match** — evidence that exactly fits the claim's scope supports higher confidence
   than evidence that must be stretched to fit.

The **weakest** relevant input dominates: a recent, well-triangulated claim resting on a
single uncorroborated report is still Low, because triangulation failed.

## Rules

- **No High without triangulation.** A single source, however good, caps confidence at
  Moderate.
- **Confidence never exceeds evidence.** The [evidence hierarchy](evidence-hierarchy.md)
  sets the ceiling; this rubric can only sit at or below it.
- **State the reason.** A confidence level is always accompanied by a one-line rationale, so
  it can be challenged.
- **Levels are visible.** Confidence appears next to the claim, not buried in an appendix.

## Why only four levels

Coarse levels are honest about how well product behaviour can actually be known.
Numeric confidence (say, "78%") would imply a precision the evidence cannot support and
invite spurious comparison. Four well-defined buckets are enough to guide a reader and cheap
to apply consistently.
