# Evidence-Coverage Comparison and Gap Register

This is the pilot's **evidence-gap register**: an honest map of what the pilot could and could
not support. It classifies conclusions by strength, lists untested questions, and flags
conflicts, plan-dependence and time-sensitivity. It is the single place a reader should look to
judge how much weight the three teardowns can bear.

## 1. Well-supported conclusions (documented, often triangulated)

- **Training defaults differ three ways** — ChatGPT opt-out, Claude opt-in, Perplexity opt-out
  (ev: cg-data-training-optout, cl-training-optin, px-training-optout-default). High confidence
  *as documented*.
- **Each product documents an ephemeral/opt-out data path** and is candid about a limit
  (ev: cg-temporary-chats-retention, cg-safety-context; cl-incognito, cl-retention-5year;
  px-training-optout-limits).
- **Product theses differ** — general assistant vs projects/artifacts assistant vs
  citation-first answer engine (ev: cg-plans-overview, cl-identity-capabilities,
  px-identity-answer-engine).
- **Claude documents portable memory; Perplexity gates rich memory to Max/preview**
  (ev: cl-memory-import-export, px-brain-memory).
- **ChatGPT shows advertising on a paid tier** (ev: cg-ads-go-plan, cg-ads-controls).

## 2. Weakly supported conclusions (single-source or inference-heavy)

- Cost-structure inferences (e.g. Perplexity pass-through) rest on the offering, not financials
  (ev: px-model-choice) — Low confidence.
- "Candour about limits is a shared positive" is an inference across three products' docs —
  Moderate at best.
- Incentive-alignment judgements (ads on paid tiers) are hypotheses, not findings
  (ev: cg-ads-go-plan) — Speculative.

## 3. Untested questions (interaction-dependent; the largest bucket)

For **all three**, the following require the interaction protocol and are `Not rated`:
first-use UX, output/error-state behaviour, agent planning/clarification/failure recovery,
cancellation, in-answer uncertainty signalling, whether memory controls actually work, and net
workflow effect. Product-specific highlights:

- **Perplexity:** *citation accuracy* — does a cited source actually support the claim? This is
  the single highest-value untested question in the pilot (ev: px-citations).
- **ChatGPT/Claude:** whether documented memory deletion/import genuinely removes/imports data
  (ev: cg-memory-delete, cl-memory-import-experimental).

## 4. Conflicting or tension-bearing evidence

- **ChatGPT pricing:** $20 (US help) vs ₹1,999 (INR page) — not a contradiction but a
  **region divergence** that forbids a single price claim (ev: cg-plus-identity-price,
  cg-pricing-region-inr).
- **"Deletion" vs retention:** ChatGPT/Claude document deletion windows *and* long-tail
  retention exceptions (ev: cg-memory-delete, cl-retention-violations) — both true, in tension;
  reported as such.
- No direct source-vs-source factual contradictions were found within a single product.

## 5. Plan-dependent ambiguity

- ChatGPT memory is **rolling out to Plus/Pro in the US first** (ev: cg-memory-rollout-region).
- Claude **chat search is paid-only**; memory spans all plans (ev: cl-chat-search-paid).
- Perplexity **Brain is Max + Computer + preview** (ev: px-brain-memory); advanced models are
  paid-only (ev: px-free-plan-limits).
- **Rule applied:** no finding on one plan was generalised to another.

## 6. Time-sensitive findings (expiry-sensitive)

- All pricing, model line-ups, and rollout states are dated 2026-07-13 (Perplexity docs stamped
  2026-05-01). Memory systems for ChatGPT (rollout) and Perplexity (preview) are explicitly in
  flux (ev: cg-memory-rollout-region, px-brain-preview). Treat all such facts as snapshots.

## 7. Coverage scorecard (documentation coverage, NOT product quality)

| Dimension | ChatGPT | Claude | Perplexity |
| --------- | ------- | ------ | ---------- |
| UX | partial | partial | partial |
| Agent behaviour | thin | thin | partial |
| Memory | strong | strong | thin |
| Trust/control | strong | strong | strong |
| Business model | strong | strong | partial |
| Workflow change | untested | untested | untested |

Coverage reflects how much *documentation* supported each dimension, not how good the product
is. Thin/untested cells are honest gaps, not negative verdicts.

## 8. What this register implies for the library

The pilot supports **documented-design** conclusions well and **behavioural** conclusions
poorly. Scaling the library requires either (a) interaction-capable research to close the
behavioural gaps, or (b) restraint in scoping teardowns to documented design until interaction
is available. This is the central methodological finding, expanded in the stress test.
