# Product Inclusion and Exclusion Criteria

These criteria decide whether a product is *eligible* for a teardown at all. Eligibility is
separate from priority: a product can be eligible but low priority. Priority is handled by
the [selection and prioritisation criteria](selection-criteria.md). Keeping the two
separate stops interesting-but-out-of-scope products from creeping in.

## Inclusion criteria (all must hold)

A product is eligible only if **all** of the following are true.

1. **AI-first.** The product's core value depends on model-driven behaviour. If you removed
   the AI capability and the product remained substantially the same, it is not AI-first
   for our purposes.
2. **Real and reachable.** It is a shipped product a researcher can actually use or observe,
   at least in a trial, free tier, or well-documented demo. Vaporware and closed private
   betas we cannot access are excluded.
3. **Studiable.** Enough of its behaviour is observable, or enough acceptable sources exist,
   to support graded evidence across the six dimensions. If we cannot gather evidence, we
   cannot do a teardown.
4. **Legal and safe to study.** Studying it does not require breaking terms in ways we
   consider unacceptable, accessing others' private data, or defeating security controls.
5. **Relevant to the audience.** It plausibly informs founders, product leaders, designers,
   researchers or students about how AI-first products work.

## Exclusion criteria (any one excludes)

A product is ineligible if **any** of the following holds.

1. **AI as garnish.** Model features are peripheral to the product's value (for example, a
   spreadsheet with a minor "summarise" button).
2. **Unstudiable in practice.** No usable access and insufficient acceptable sources to
   support graded claims.
3. **Requires unethical or unsafe access.** Studying it would require violating privacy,
   defeating security, or breaching terms in ways we will not sanction.
4. **Purely hypothetical.** Announced but not shipped, or a concept with no working surface.
5. **Conflict we cannot manage.** A conflict of interest exists that
   [governance](../governance/bias-and-conflicts.md) judges unmanageable for this product.

## Edge cases and how we resolve them

- **Platforms vs features.** A large platform may contain several AI-first products. We
  scope to a specific product/surface via the [unit of analysis](unit-of-analysis.md)
  rather than trying to tear down the whole platform at once.
- **Rapidly changing betas.** Eligible if reachable and studiable, but the volatility is
  recorded as a limitation and reflected in confidence levels.
- **Deprecated products.** May be included for historical or comparative value, clearly
  marked as studying a past state, subject to the archival policy.

## Recording the decision

Every teardown records, in its metadata, that inclusion criteria were checked and notes any
edge case and how it was resolved. Eligibility is a documented decision, not an assumption.
