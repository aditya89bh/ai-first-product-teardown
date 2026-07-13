# Cross-Product Comparison Principles

Comparisons are among the most valuable — and most dangerous — outputs of the library. Done
well, comparing products across the six dimensions reveals patterns no single teardown can.
Done badly, comparison manufactures false equivalence and misleads readers. This document
sets the principles that make comparison rigorous. Detailed comparison records are built in
later phases; this is the foundation.

## Precondition: compare like with like

A comparison is only valid when the things compared are genuinely comparable:

1. **Comparable units of analysis.** Compare products on equivalent
   [units](../docs/methodology/unit-of-analysis.md) — similar tiers, surfaces, and task
   types. Comparing a free tier to an enterprise tier, or a chat surface to an API, is
   category error unless that difference is itself the point and is stated.
2. **Comparable observation windows.** Products change over time; comparisons must use
   evidence from reasonably aligned dates, or explicitly note the mismatch and its effect.
3. **Comparable evidence strength.** A comparison is only as strong as its weaker side. Do
   not contrast a well-triangulated finding for one product with a single anecdote for
   another.

## Comparison is dimension-by-dimension

- Products are compared **within a dimension**, not as overall winners. "Product A has more
  legible oversight controls than Product B, for the studied units" is a valid comparison;
  "Product A is better than Product B" is not.
- Each dimension comparison carries its own evidence and confidence, and inherits the
  [scoring principles](qualitative-scoring.md) and the ban on
  [false precision](scoring-false-precision.md).

## What comparisons may claim

- **Relative, bounded judgements** within a dimension, for comparable units, with evidence on
  both sides and a confidence level.
- **Patterns and contrasts** that recur across several products (e.g., "products in this
  group tend to make consequential actions reversible; this one does not").
- **Trade-offs**, showing that a strength on one dimension often comes with a cost on another.

## What comparisons must not do

- **No overall ranking or "best" verdicts.** The library does not produce leaderboards (see
  [non-goals](../docs/vision/non-goals.md)).
- **No composite cross-dimension scores.** Dimensions are not commensurable; summing or
  averaging them is false precision.
- **No false equivalence.** Do not present two products as comparable on a dimension when the
  evidence for one is materially weaker; say so instead.
- **No implied causation** between products' choices and outcomes without evidence.

## Handling incomparability honestly

When products cannot be fairly compared on a dimension — different tiers, misaligned dates,
asymmetric evidence — the correct output is to **say they are not comparable here and why**,
not to force a comparison. A stated "not comparable" is a finding; a forced comparison is a
distortion.

## Recording comparisons

Later-phase comparison records will, like teardowns, be structured and validated. Each will
cite the underlying teardowns and evidence records for both products, so any comparison can
be traced back to the single-product findings it rests on.

## Principle

Comparison amplifies both insight and error. The discipline that protects single teardowns —
comparable scope, matched evidence strength, dimension separation, no false precision —
applies with *extra* force when two products are set side by side.
