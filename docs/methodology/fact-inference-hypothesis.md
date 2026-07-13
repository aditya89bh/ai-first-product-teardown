# Distinguishing Fact, Observation, Inference and Hypothesis

The single most important discipline in this library is keeping four kinds of statement
separate. Most bad product analysis fails here: it presents an inference as a fact, or a
hypothesis as a finding. Every statement in a teardown is classified as exactly one of the
four types defined below, and the type is visible to the reader.

## The four types

### Fact

A statement that is established beyond reasonable dispute for the stated
[unit of analysis](unit-of-analysis.md), supported by strong, ideally triangulated evidence.

- Example (synthetic): "On the free web tier, as observed 2026-07-01, sending a message with
  no input returned an error rather than an empty reply." *(synthetic)*
- Requires: high-tier evidence, typically corroborated. Facts are scoped to the unit and the
  date; they are not universal truths.

### Observation

A specific, first-hand record of what happened under recorded conditions. An observation is
descriptive and does not interpret intent or cause.

- Example (synthetic): "In 5 of 5 runs of a fixed prompt on 2026-07-02, the agent asked a
  clarifying question before acting." *(synthetic)*
- Requires: a recorded unit of analysis and reproducible conditions. Observations are the raw
  material from which facts and inferences are built.

### Inference

A conclusion *drawn from* facts and observations using reasoning. Inferences go beyond what
was directly observed and are therefore fallible.

- Example (synthetic): "Because the agent consistently asked before acting, the product
  appears designed to favour confirmation over speed." *(synthetic — an inference about
  design intent from observed behaviour.)*
- Requires: explicit reasoning linking it to the underlying evidence, and a
  [confidence level](confidence-levels.md). Never stated as a fact.

### Hypothesis

A proposed explanation or prediction that is *not yet supported* well enough to be an
inference. Hypotheses drive future research; they are not conclusions.

- Example (synthetic): "The confirmation behaviour may reduce task-completion speed for
  expert users — this is untested." *(synthetic)*
- Requires: explicit labelling as unconfirmed and, ideally, a note on how it could be tested
  or refuted.

## How the types relate

Observations aggregate and triangulate into facts. Facts and observations support
inferences. Gaps and open questions become hypotheses, which future observations may promote
to inferences or facts — or refute. The flow is always **evidence → classified claim**,
never the reverse.

## Rules

1. **Label everything.** No statement in a teardown is unclassified. Templates enforce
   labelled sections.
2. **Do not upgrade silently.** Promoting a hypothesis to an inference, or an inference to a
   fact, requires new evidence and is a visible change, not a wording tweak.
3. **Match language to type.** Facts use definite language; inferences use "appears/suggests"
   with a confidence level; hypotheses use "may/might, untested".
4. **Opinion is not a fifth type.** Unsupported preference has no home here. If a judgement
   cannot be expressed as a graded inference or a labelled hypothesis, it does not belong in
   a teardown (see [non-goals](../vision/non-goals.md)).

## Why this matters most

A reader must be able to trust that when we say "fact", we mean it, and when we speculate, we
say so. This separation is the library's core promise. Everything else — evidence grading,
confidence, reproducibility — exists to keep it honest.
