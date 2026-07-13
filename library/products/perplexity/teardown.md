# Teardown: Perplexity

> **Pilot teardown (Phase 2).** Documentation-first, public-evidence-only. No authenticated
> or paid-plan interaction was performed. Every analytical conclusion cites evidence-record
> ids under `evidence/perplexity/`. Claims are labelled `[FACT]`, `[OBS]`, `[INFERENCE]` or
> `[HYPOTHESIS]`; documentation claims are vendor-self-reported unless directly observed.

## 1. Research scope

- **Product surface studied:** Perplexity consumer web application (`perplexity.ai`) and the
  official Perplexity Help Center.
- **Access mode:** logged-out / documentation-first. `perplexity.ai` returned HTTP 403 to
  direct fetch; help articles were read through the in-app browser (last updated 2026-05-01)
  and cited with the 2026-07-13 access date.
- **Plan/tier:** Free (Standard) by default; paid-tier facts (Pro, Max, Enterprise Pro/Max)
  taken only from official pages and marked plan-specific.
- **Region:** not specified by the help articles; treated as global/US-default.
- **Research date:** 2026-07-13.
- **Capabilities included:** documented answer-engine behaviour, Search / Pro Search / Deep
  Research, citations, model selection, subscription plans, the "Brain" memory system, and
  data-collection/opt-out controls.
- **Capabilities excluded:** Sonar API, Comet browser specifics, Enterprise admin, mobile
  specifics, and any behaviour requiring an authenticated or paid session.
- **Evidence limitations:** most behavioural claims are vendor-self-reported; interaction-
  dependent behaviour is `[UNTESTED]`. Perplexity **integrates third-party models** (OpenAI,
  Anthropic, Google), so "product" and "model" are especially distinct here.
- **Version ambiguity:** help articles dated 2026-05-01; findings dated to the 2026-07-13
  access date and expiry-sensitive.

## 2. Product metadata

See `metadata.yaml`. Summary: Perplexity, teardown v0.1.0, status active, observation window
2026-07-13, review by 2026-10-13.

## 3. Source inventory

See `source-inventory.md`. Official-first; access notes recorded.

## 4. Evidence coverage

See `source-inventory.md` (source-to-evidence map) and §13. Evidence records live in
`evidence/perplexity/`.

## 5. User experience analysis

_Framework: `frameworks/ux/framework.md`. Documentation-first; in-product UX `[UNTESTED]`._

- `[FACT]` The documented UX thesis is **answer-first**: synthesised direct answers instead of
  lists of links, with sources as citations (ev: px-ux-direct-answers, px-citations).
  Confidence: High that this is the stated design.
- `[FACT]` Pro Search supports **conversational refinement** with retained context
  (ev: px-ux-refinement).
- `[INFERENCE]` Perplexity's UX optimises for **fast verifiable answers** rather than
  open-ended assistance — a narrower, more focused interaction model than a general assistant
  (ev: px-ux-direct-answers, px-identity-answer-engine). Confidence: Moderate —
  documentation-based.
- `[HYPOTHESIS]` Presenting citations inline may make source-checking a normal part of the UX
  loop (rather than an afterthought) — untested (route: interaction protocol §2, §6).

**Evidence gaps (UX):** first-use orientation, input structure, actual output/citation
rendering, error states, and accessibility indicators are `[UNTESTED]` (protocol §1, §2). Such
sub-areas are `Not rated`.

## 6. Agent-behaviour analysis

_Populated in a later commit._

## 7. Memory analysis

_Populated in a later commit._

## 8. Trust and control analysis

_Populated in a later commit._

## 9. Business-model analysis

_Populated in a later commit._

## 10. Workflow-change analysis

_Populated in a later commit._

## 11. Cross-dimensional findings

_Populated in the synthesis commit._

## 12. Scoring record

See `scores.yaml`, added in the synthesis commit.

## 13. Evidence gaps

_Populated across dimension commits and consolidated in the synthesis commit._

## 14. Limitations

_Populated in the synthesis commit._

## 15. Reproduction instructions

_Populated in the synthesis commit._

## 16. Update triggers

_Populated in the synthesis commit._

## 17. Facts, observations, inferences and hypotheses

Each dimension section separates these explicitly using the `[FACT]` / `[OBS]` /
`[INFERENCE]` / `[HYPOTHESIS]` labels.
