# Reproducibility Requirements

A teardown is only as credible as its reproducibility. Reproducibility here means: **a
stranger, given the teardown and its evidence records, could repeat the work, reach their
own judgement, and identify exactly where they agree or disagree with us.** This is the
property that separates research from assertion.

## What must be reproducible

For each teardown, the following must be reconstructable from what we publish:

1. **The unit of analysis** — the exact product, edition, surface, version window and
   account context (see [unit of analysis](../methodology/unit-of-analysis.md)).
2. **The observation procedure** — for first-hand observations, enough detail (inputs,
   settings, steps) that someone could attempt the same interaction.
3. **The evidence trail** — every source recorded to the
   [citation standard](../methodology/citation-standard.md), with archives for volatile
   material.
4. **The reasoning** — how observations and facts were combined into inferences, so the
   logical steps can be checked, not just the conclusions.
5. **The classification and grading** — why each claim is a fact/observation/inference/
   hypothesis and why its evidence sits at its tier and confidence.

## The reproducibility note

Every teardown ends with a **reproducibility note** covering:

- How the product was accessed and over what dates.
- The key procedures used to generate first-hand observations.
- Known factors that could make exact reproduction difficult (non-determinism, rollouts,
  account-specific behaviour), and how a re-runner should account for them.
- What a challenger should do to test the strongest and weakest claims.

## Reproducibility under non-determinism

We cannot promise identical outputs from a probabilistic system. Instead we make the *method*
reproducible and report behaviour as tendencies:

- State how many trials were run, over what window, under what conditions.
- Report frequencies rather than implying determinism.
- Treat "I ran it once and got something different" not as a refutation but as an invitation
  to compare procedures and sample sizes.

## Machine reproducibility

The tooling side is held to a stricter standard, because it *can* be deterministic:

- Structured records validate against the [schemas](../../schemas/) with a single documented
  command.
- Tests, lint and type checks run from documented commands and must pass in CI.
- Anyone can clone the repository and re-run the full validation suite.

## Failure to be reproducible

- A claim whose supporting observation cannot be reproduced as described is downgraded or
  removed.
- A teardown without a usable reproducibility note cannot pass review.
- If reproduction by a third party materially disagrees with a published finding, it enters
  the [corrections and disputes](corrections-and-disputes.md) process.

## Principle

We would rather publish a modest, fully reproducible finding than an impressive one nobody
can check. Reproducibility is not paperwork; it is the mechanism by which the library earns
and keeps trust.
