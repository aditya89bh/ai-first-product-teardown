# Rules Preventing False Precision in Scoring

False precision is the presentation of a judgement as more exact than the evidence supports.
It is the most seductive failure mode in product analysis: a single number feels
authoritative, ranks cleanly, and travels well — which is exactly why it misleads. This
document defines the hard rules that keep the library's [qualitative
scoring](qualitative-scoring.md) honest. These rules are not stylistic preferences; they are
constraints validated by tooling where possible.

## The core prohibition

**No score in this library may imply more precision than the evidence and the phenomenon
allow.** Product behaviour under uncertainty is not measurable to a decimal, and our scores
must not pretend otherwise.

## Hard rules

1. **No numeric or percentage scores** for qualitative judgements. Use the ordinal scale
   (Strong / Adequate / Weak / Absent / Not rated), not 7/10 or 82%.
2. **No composite or overall scores.** Sub-area scores are never summed or averaged into a
   dimension score, and dimension scores are never combined into a product score. Dimensions
   are not commensurable.
3. **No cross-product numeric ranking.** Products are not ordered on a numeric scale; only
   bounded, evidenced, dimension-specific relative judgements are allowed (see
   [comparison](cross-product-comparison.md)).
4. **No weighting schemes that manufacture a total.** Assigning weights to dimensions to
   produce a single figure reintroduces exactly the false precision this document forbids.
5. **No score without confidence.** A score detached from its
   [confidence level](../docs/methodology/confidence-levels.md) overstates certainty by
   omission.
6. **No false decimal confidence.** Confidence uses the four defined levels, never a
   percentage.

## Why each rule exists

- **Numbers invite arithmetic.** The moment a judgement is a number, someone will average,
  weight, or rank it — operations the underlying evidence cannot bear.
- **Composites hide disagreement.** A single "trust: 6.4" buries the fact that oversight was
  Strong and reversibility was Absent. The interesting finding is in the components, not the
  average.
- **Ranking implies a scalar reality.** "Best AI product" presumes a single axis of quality
  that does not exist across six incommensurable dimensions.
- **Precision without evidence is a lie of form.** The format signals rigour the content does
  not have.

## Positive practices in place of false precision

- Report **bounded ordinal scores with rationale and confidence**.
- Report **frequencies and conditions** for behavioural claims ("did X in 8 of 10 runs"),
  which are honest quantities, not manufactured scores.
- Present **profiles**, not totals: a product's shape across sub-areas, shown component by
  component.
- Say **"not rated"** when evidence is thin, rather than inventing a defensible-looking
  number.

## Enforcement

- Templates and schemas constrain score fields to the allowed ordinal values, so numeric
  scores cannot be recorded in structured data.
- Review checks that no teardown or comparison presents a composite, weighted, or numeric
  ranking.
- The [validation tooling](../src/product_intelligence/) rejects scoring records whose values
  fall outside the permitted set.

## Principle

It is better to be **honestly vague** than **precisely wrong**. A reader is served by
"oversight controls are Strong; reversibility is Absent; overall trust is genuinely
mixed" — and misled by "trust score: 6.1/10". The library chooses honesty over the comfort
of a false number, every time.
