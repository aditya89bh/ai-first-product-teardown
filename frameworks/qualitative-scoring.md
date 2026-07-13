# Qualitative Scoring Principles

The library uses **qualitative, bounded scoring** to summarise judgements within a dimension.
Scoring exists to aid comparison and skim-reading — not to replace the evidence and reasoning
behind a finding. This document defines how scoring works and the discipline that keeps it
honest. Its companion, [scoring false precision](scoring-false-precision.md), defines the
lines it must never cross.

## What a score is (and is not)

- A score **is** a compact, evidence-backed judgement of how a product handles one
  sub-area or dimension, expressed on a small ordinal scale with a stated rationale.
- A score **is not** a measurement, a number that can be averaged, or a verdict that stands
  without its supporting evidence and confidence level.

## The scoring scale

Scores use a small, ordinal, clearly labelled scale. The recommended default:

| Level      | Meaning                                                                     |
| ---------- | --------------------------------------------------------------------------- |
| Strong     | Handles this well, with clear evidence; few or minor observed weaknesses.   |
| Adequate   | Works acceptably; notable strengths and weaknesses both observed.           |
| Weak       | Notable problems observed; handles this poorly for the studied unit.        |
| Absent     | The capability is not present or not observable at all.                     |
| Not rated  | Insufficient evidence to score responsibly.                                 |

The scale is ordinal (ordered categories), **not** numeric. "Adequate" is better than "Weak"
but there is no defined "distance" between them, and they cannot be arithmetically combined.

## Rules for scoring

1. **Every score cites evidence.** A score with no linked evidence records is invalid.
2. **Every score carries a confidence level** (see
   [confidence levels](../docs/methodology/confidence-levels.md)). A confident "Weak" and a
   tentative "Weak" are different findings.
3. **Every score has a one-line rationale** stating what drove it, so it can be challenged.
4. **Scores are scoped.** A score applies to the studied
   [unit of analysis](../docs/methodology/unit-of-analysis.md) and date, never universally.
5. **"Not rated" is a first-class result.** When evidence is insufficient, we say so rather
   than guessing a score.
6. **Scores never aggregate across dimensions.** There is no overall product score (see
   [false precision](scoring-false-precision.md)).

## Why ordinal, not numeric

Product behaviour under uncertainty cannot be measured to a decimal. A 1–10 or percentage
score would imply a precision the evidence cannot support and would invite spurious
averaging and ranking. A small ordinal scale communicates a bounded judgement honestly and
resists misuse.

## Scoring and comparison

- Within a dimension, ordinal scores support the relative judgements described in
  [cross-product comparison](cross-product-comparison.md), for comparable units.
- Scores are never summed or averaged to compare products overall — that is precisely the
  false precision the next document forbids.

## Principle

A score is a signpost to a finding, not a substitute for it. It must always be traceable to
evidence, qualified by confidence, scoped to a unit, and honest enough to say "not rated"
when the evidence is not there.
