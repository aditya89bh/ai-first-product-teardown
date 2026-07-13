# Pilot-Product Selection Rationale

Phase 2 studies three products: **ChatGPT** (OpenAI), **Claude** (Anthropic) and
**Perplexity** (Perplexity AI). This document explains why these three were chosen, where
they are legitimately comparable, where comparison would be invalid, and exactly which
product surfaces are in and out of scope. It exists so that the comparison built later
(commits 36–43) rests on an explicit, challengeable scoping decision rather than an implicit
one.

## Why these three

The pilots must stress-test the Phase 1 methodology, which means they should be **similar
enough to compare** yet **different enough to expose the limits of comparison**.

1. **They share a surface class.** All three offer a consumer-facing, natural-language
   **assistant / answer interface** on the web, with free and paid tiers. This gives the six
   dimensions a common footing.
2. **They differ in product thesis.** ChatGPT positions as a general assistant; Claude as an
   assistant with a strong coding/writing and safety emphasis; Perplexity as an
   answer engine built around cited web search. These differences are exactly what test
   whether our comparison rules prevent category error (stress hypothesis H-S4).
3. **They have substantial official documentation.** Each maintains public help centres,
   pricing, and privacy/terms pages — the primary sources this evidence-first phase requires.
4. **They are eligible and studiable** under the Phase 1
   [inclusion criteria](../methodology/inclusion-criteria.md): shipped, reachable, and
   documentable without breaching terms, privacy or security.

## Where they are comparable

Comparison is valid, with care, on **specific design choices within a dimension**, for
comparable surfaces (the web app, consumer tiers), such as:

- How each presents sources and communicates uncertainty (trust and control).
- How each exposes and controls saved user information (memory).
- How each structures free-vs-paid boundaries (business model).
- How each changes a concrete task's workflow (workflow change).

## Where comparison would be invalid

Comparison is **category error** and is prohibited where product boundaries diverge:

- **"Best overall assistant."** The three optimise for different jobs; there is no shared
  scalar. No global ranking will be produced (see
  [comparison principles](../../frameworks/cross-product-comparison.md)).
- **Answer-engine vs assistant strengths.** Perplexity's citation-first answer flow and
  ChatGPT/Claude's open-ended assistance are different jobs; contrasting them on raw
  "capability" misleads.
- **Model vs product.** Each product may expose multiple underlying models on different
  plans. We study the **product surface**, never the model in the abstract, and never treat
  a model benchmark as a product claim.
- **Cross-plan generalisation.** A feature on a paid tier is not evidence about the free
  tier, and vice versa.

## Product surfaces included

For each product, the pilot studies the **consumer web application and its official
documentation**, on the **free tier by default**, with paid-tier facts drawn only from
official pricing/help pages and clearly marked as plan-specific:

- ChatGPT: the ChatGPT web app (`chatgpt.com`) and OpenAI Help Center documentation.
- Claude: the Claude web app (`claude.ai` / `claude.com`) and Claude support/pricing
  documentation.
- Perplexity: the Perplexity web app (`perplexity.ai`) and Perplexity Help Center
  documentation.

## Product surfaces excluded

Explicitly **out of scope** for this pilot (documented as evidence gaps where relevant):

- Native mobile and desktop apps, browser extensions, and voice-first surfaces.
- Developer APIs and platform/enterprise admin consoles.
- Authenticated, paid-plan, logged-in behaviour (no signed-in sessions are used).
- Region-specific variants; where a source does not specify region, findings are treated as
  global/US-default and the ambiguity is recorded.
- Underlying model benchmarks and capability claims divorced from the product.

## Scope caveats carried into every teardown

Each product teardown repeats, in its own metadata and limitations, that: (a) only the web
surface and documentation were studied; (b) no authenticated or paid-plan interaction
occurred; (c) documentation reflects vendor self-reporting unless a claim was directly
observed; and (d) product facts are dated to the 2026-07-13 research window and are
expiry-sensitive.
