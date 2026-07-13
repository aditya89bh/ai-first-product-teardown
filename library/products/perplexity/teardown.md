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

_Framework: `frameworks/agent-behaviour/framework.md`. Behavioural quality is `[UNTESTED]`,
but Perplexity documents unusually specific agent behaviour._

- `[FACT]` Pro Search is a documented **multi-step retrieve-and-synthesise** agent: multiple
  web searches across source types, compiled from "dozens of sources"
  (ev: px-pro-search-steps). Confidence: High that this is documented.
- `[FACT]` **Planning is made visible** — the product shows "how the AI broke down your
  question and approached the research" (ev: px-pro-search-planning-visible). Notable and
  differentiating.
- `[FACT]` Users can **select a model per session** (Sonar, GPT-5, Claude Sonnet 4.6, Gemini
  3.1 Pro) (ev: px-pro-search-models), and Pro Search includes a **code interpreter**
  (ev: px-code-interpreter).
- `[INFERENCE]` Perplexity's agent design emphasises **transparency of process** (visible
  breakdown + citations) more prominently than the other two products' documentation does
  (ev: px-pro-search-planning-visible, px-citations). Confidence: Moderate —
  documentation-based; whether the shown breakdown faithfully mirrors the real process is
  untested.
- `[HYPOTHESIS]` Visible planning may aid user trust and correction but could also be
  post-hoc rationalisation rather than the true process — untested (route: interaction
  protocol §3, §6).

**Evidence gaps (agent behaviour):** clarification behaviour, autonomy vs confirmation,
failure recovery, intervention, and whether the visible plan reflects the actual process are
`[UNTESTED]` (protocol §3–§5, §9). These sub-areas are `Not rated`.

## 7. Memory analysis

_Framework: `frameworks/memory/framework.md`. Documentation on base-product memory is thin;
the richer memory is gated and in preview._

- `[FACT]` The Free plan documents "Search history access" (ev: px-free-plan-limits) but the
  read documentation describes no automatic cross-session personalisation memory for the base
  product comparable to ChatGPT's or Claude's.
- `[FACT]` The richer memory — **Brain** — is a "self-improving memory system that builds a
  working model of your projects, people, and files", **gated to Max + Perplexity Computer**
  and in **Research Preview** (ev: px-brain-memory, px-brain-preview). Confidence: High that
  this is documented.
- `[INFERENCE]` Consistent with its answer-engine thesis, Perplexity appears to treat
  persistent user memory as a **premium, workspace-tier capability (Brain)** rather than a
  default of the core product (ev: px-brain-memory, px-free-plan-limits). Confidence: Moderate
  — documentation-based, and Brain is early (preview).
- `[HYPOTHESIS]` An answer engine may need less persistent memory than a general assistant
  because each query is more self-contained — plausible but untested. Confidence: Speculative.

**Evidence gaps (memory):** Brain's user controls (view/edit/delete), retention, and whether
it trains models were **not** documented on the pages read — a notable asymmetry versus
ChatGPT's and Claude's detailed memory docs. Base-product memory behaviour is `[UNTESTED]`.
This gap is recorded, not filled with assumptions.

## 8. Trust and control analysis

_Framework: `frameworks/trust/framework.md`. Source transparency and data controls are
documented; in-answer citation accuracy is `[UNTESTED]`._

- `[FACT]` **Source transparency** is central: every answer carries citations to sources for
  verification (ev: px-citations), and Pro Search exposes its reasoning breakdown
  (ev: px-pro-search-planning-visible).
- `[FACT]` Consumer training default is **opt-out**: "AI Data Retention is enabled by default"
  for Free/Pro/Max, with a toggle to opt out (ev: px-training-optout-default). Confidence:
  High that this is documented.
- `[FACT]` The opt-out has documented **limits**: it is not retroactive and "previously
  collected training data cannot be deleted or removed" (ev: px-training-optout-limits).
- `[FACT]` Perplexity states it **does not sell** user data (ev: px-no-data-sale), and
  **Enterprise** data is never used for training with **ZDR agreements** binding third-party
  model providers (ev: px-enterprise-no-training).
- `[INFERENCE]` Perplexity's trust story leans on **process/source transparency** (citations,
  visible planning) more than on privacy-by-default: consumer training is on by default and
  the opt-out is non-retroactive (ev: px-citations, px-training-optout-default,
  px-training-optout-limits). Confidence: Moderate — documentation-based.
- `[HYPOTHESIS]` For a citation-first product, *source accuracy* may matter more to trust than
  data controls; if citations frequently fail to support claims, the core value erodes —
  untested and important (route: interaction protocol §6).

**Evidence gaps (trust/control):** whether citations accurately support the claims they
attach to, in-answer uncertainty signalling, and whether the opt-out toggle behaves as
documented are `[UNTESTED]` (protocol §6, §8). No sub-area scored negatively for missing
evidence.

## 9. Business-model analysis

_Framework: `frameworks/business-model/framework.md`. Value creation/capture only; no company
valuation or revenue forecast._

- `[FACT]` Perplexity is packaged **Free → Pro → Max**, with **Education Pro at $10/mo**, plus
  **Enterprise Pro/Max** and a **Sonar API** (ev: px-plans-overview, px-education-pro-price).
  Free gives broad basic search but gates advanced models and Pro Search
  (ev: px-free-plan-limits).
- `[FACT]` **Max** targets high-volume power users; model access applies to the web product,
  while **API is billed separately** (ev: px-max-tier).
- `[FACT]` The product **resells access to third-party models** (OpenAI, Anthropic, Google)
  as an orchestration layer (ev: px-model-choice).
- `[INFERENCE]` Because it pays third parties for model access, Perplexity's **cost structure
  is partly pass-through**, which plausibly explains gating advanced models behind paid tiers
  and metering Pro Search on Free (ev: px-model-choice, px-free-plan-limits). Confidence:
  Moderate — a cautious inference from the offering, not from financials.
- `[INFERENCE]` Value capture combines **subscription tiers + a student discount + separate
  usage-based API** (ev: px-plans-overview, px-max-tier, px-education-pro-price). Confidence:
  Moderate.
- `[HYPOTHESIS]` Depending on a third-party-model layer creates a strategic dependency risk
  (pricing/availability of upstream models) — plausible but not evidenced by financials.
  Confidence: Speculative.

**Evidence gaps (business model):** exact standard **Pro and Max consumer prices** were not
stated on the read pages (only Education Pro $10/mo) — recorded as a gap, not guessed. Revenue,
margins, and upstream model-cost terms are not evidenced. No advertising was observed on the
pages read (absence is not evidence of absence).

## 10. Workflow-change analysis

_Framework: `frameworks/workflow-change/framework.md`. Net effect `[UNTESTED]`._

- `[FACT]` Pro Search is documented to **compress the research workflow** — replacing "sifting
  through pages of search results" with one synthesised, cited answer (ev: px-pro-search-steps,
  px-ux-direct-answers). Confidence: High that this is the stated design.
- `[FACT]` **Create files and apps** produces reports, dashboards, spreadsheets and web apps
  (Pro limited, Max minimal limits) (ev: px-create-files-apps), moving beyond answers into
  artifacts.
- `[INFERENCE]` If these work as documented, Perplexity **removes manual search-and-collate
  steps** and shifts effort toward **verifying citations** — the citation model both compresses
  and adds a checking step (ev: px-pro-search-steps, px-citations). Confidence: Low — inferred,
  not observed.
- `[INFERENCE]` Because answers are inline-cited, the **verification burden is lighter to
  discharge** than in products where sources are hidden — the user can check in place
  (ev: px-citations, px-pro-search-planning-visible). Confidence: Low.
- `[HYPOTHESIS]` For research tasks, an answer engine may reduce total steps more than a
  general assistant does — but only if citation accuracy holds; otherwise verification cost
  rises — untested (route: interaction protocol §2, §6).

**Evidence gaps (workflow change):** tasks compressed, steps removed vs added (especially
citation-checking), and new failure modes require running representative research tasks end to
end (protocol §2, §3, §6). The dimension is `Not rated` pending interaction.

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
