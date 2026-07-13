# Teardown: ChatGPT

> **Pilot teardown (Phase 2).** Documentation-first, public-evidence-only. No authenticated
> or paid-plan interaction was performed. Every analytical conclusion cites evidence-record
> ids under `evidence/chatgpt/`. Claims are labelled `[FACT]`, `[OBS]`, `[INFERENCE]` or
> `[HYPOTHESIS]`; documentation claims are vendor-self-reported unless directly observed.

## 1. Research scope

- **Product surface studied:** ChatGPT consumer web application (`chatgpt.com`) and the
  OpenAI Help Center documentation.
- **Access mode:** logged-out / documentation-first, via direct fetch and the in-app browser.
  Direct fetch of `openai.com` / `chatgpt.com` / `help.openai.com` returned HTTP 403; help
  articles were read through the in-app browser and are cited with access dates.
- **Plan/tier:** Free tier by default; paid-tier facts (Go, Plus, Pro, Business, Enterprise)
  are taken only from official pricing/help pages and marked plan-specific.
- **Region:** not specified by sources; treated as global/US-default and flagged as ambiguity.
- **Research date:** 2026-07-13.
- **Capabilities included:** documented web-app features, plans, memory and data controls as
  described in official help articles.
- **Capabilities excluded:** mobile/desktop apps, API, custom GPT internals, enterprise admin,
  and any behaviour requiring an authenticated or paid session.
- **Evidence limitations:** most behavioural claims are vendor-self-reported; interaction-
  dependent behaviour is marked `[UNTESTED]` and routed to the interaction protocol.
- **Version ambiguity:** no explicit product version string; model availability is described
  by OpenAI as changing over time, so findings are dated to the research window.

## 2. Product metadata

See `metadata.yaml` (validated against `schemas/product-metadata.schema.json`). Summary:
ChatGPT, teardown v0.1.0, status active, observation window 2026-07-13, review by
2026-10-13.

## 3. Source inventory

See `source-inventory.md`. Official-first; access barriers recorded.

## 4. Evidence coverage

See `source-inventory.md` (source-to-evidence map) and section 13 (evidence gaps). Evidence
records live in `evidence/chatgpt/`.

<!-- Sections 5–17 are populated by subsequent Phase 2 commits, one dimension per commit. -->

## 5. User experience analysis

_Framework: `frameworks/ux/framework.md`. Documentation-first; most in-product UX is
`[UNTESTED]` because no authenticated chat session was used._

- `[FACT]` OpenAI documents a consistent settings location for personalisation — "Settings >
  Personalization" for both Memory and Custom Instructions (ev: cg-ux-settings-navigation).
  Confidence: High (that it is *documented*).
- `[FACT]` An in-context provenance affordance is documented: a "book icon below the
  response" reveals which sources (custom instructions, past chats, files, memories)
  personalised an answer (ev: cg-ux-memory-sources-affordance). Confidence: High that it is
  documented.
- `[OBS]` On the public, logged-out web surface, the pricing page presents a clear top
  navigation and comparable plan cards with a feature-comparison table
  (ev: cg-ux-web-nav-observed). This is the marketing surface, not the chat UX.
- `[INFERENCE]` The documented, in-context "sources" affordance suggests a deliberate design
  choice to make personalisation legible at the point of use rather than only in settings
  (ev: cg-ux-memory-sources-affordance). Confidence: Moderate — inferred from documentation,
  not observed, and the vendor notes it "may not show every factor".
- `[HYPOTHESIS]` Placing memory and custom-instruction controls under a single
  "Personalization" settings area may aid discoverability for users who look for
  personalisation in one place — untested (route: interaction protocol §1, §7).

**Evidence gaps (UX):** first-use orientation, input structure, output rendering, error
states, progressive disclosure and accessibility indicators are all `[UNTESTED]` this phase
because they require an authenticated chat session. See §13 and the interaction protocol
(§1, §2, §6). No UX sub-area is scored negatively for missing evidence; such sub-areas are
`Not rated`.

## 6. Agent-behaviour analysis

_Framework: `frameworks/agent-behaviour/framework.md`. Behavioural sub-areas are largely
`[UNTESTED]` (documentation cannot evidence how an agent actually behaves)._

- `[OBS]` The product offers a range of agentic / tool-using features — Search, Deep
  research, Codex, Scheduled tasks, Projects, a built-in browser and "Workspace agents" —
  several tier-gated and marked "Limited" on Free (ev: cg-agent-tooling-offered).
- `[FACT]` OpenAI documents "Deep Research tools (where available)" as a Plus capability
  (ev: cg-agent-deep-research). The qualifier "where available" is preserved.
- `[INFERENCE]` The breadth of scheduled/agentic features suggests ChatGPT is positioned as
  a general-purpose agent platform, not only a chat box (ev: cg-agent-tooling-offered,
  cg-agent-deep-research). Confidence: Moderate — inferred from the product's own feature
  listing, not from observed task execution.
- `[HYPOTHESIS]` The gating of most agentic features behind paid tiers may mean free-tier
  agent behaviour differs materially from paid-tier behaviour — untested; explicitly do not
  generalise across plans.

**Evidence gaps (agent behaviour):** task interpretation, planning visibility, clarification
behaviour, autonomy vs confirmation, failure recovery, user intervention and boundary
communication are all `[UNTESTED]` and require interaction (protocol §3, §4, §5, §9, §10).
Documentation lists *that* features exist; it cannot show *how* the agent behaves. These
sub-areas are `Not rated`, not scored negatively.

## 7. Memory analysis

_Framework: `frameworks/memory/framework.md`. This is ChatGPT's best-documented dimension;
several controls are documented in detail, though their efficacy is `[UNTESTED]`._

- `[FACT]` When enabled, ChatGPT automatically remembers context from chats, files and
  connected apps, and memory is user-toggleable in Settings > Personalization > Memory
  (ev: cg-memory-how-it-works). Confidence: High that this is documented.
- `[FACT]` The product distinguishes two personalisation channels: explicit **Custom
  Instructions** vs inferred **conversational memory** (ev: cg-memory-vs-custom-instructions).
- `[FACT]` A **memory summary** lets users view and edit what is remembered, but "Don't
  mention this again" suppresses rather than deletes (ev: cg-memory-summary-edit).
- `[FACT]` **Full deletion** of a remembered detail requires deleting every source where it
  appears (past/archived chats, files, the summary, connected apps); turning memory off does
  not delete past chats, and re-enabling may re-derive memories (ev: cg-memory-delete).
- `[FACT]` **Temporary Chats** neither use nor create memories — triangulated across the
  Memory FAQ and Data Controls FAQ (ev: cg-temporary-chats-memory,
  cg-temporary-chats-retention). Confidence: High.
- `[FACT]` The new memory system is **plan- and region-gated** (rolling out to Plus/Pro in
  the US first) (ev: cg-memory-rollout-region). Memory findings therefore cannot be
  generalised across plans, regions or time.
- `[INFERENCE]` ChatGPT's memory model is relatively transparent *as documented* (summary,
  sources affordance, explicit vs inferred split) but places a **non-trivial deletion
  burden** on the user, since suppression ≠ deletion and full removal spans many surfaces
  (ev: cg-memory-summary-edit, cg-memory-delete). Confidence: Moderate — documentation-based.
- `[HYPOTHESIS]` The gap between "suppress" and "delete" may cause users to believe
  information is removed when it is only hidden — a potential trust failure mode; untested
  (route: interaction protocol §7).

**Evidence gaps (memory):** whether edit/delete controls actually behave as documented,
retrieval visibility in real conversations, and cross-session continuity are `[UNTESTED]`.
Plan/region rollout means even the documented behaviour may not apply to a given account.

## 8. Trust and control analysis

_Framework: `frameworks/trust/framework.md`. Data-control surface is well documented;
in-conversation trust behaviour (uncertainty, source accuracy) is `[UNTESTED]`._

- `[FACT]` A documented, unrestricted **training opt-out** ("Improve the model for everyone")
  is available signed-in and signed-out; opting out keeps chats in history but excludes them
  from training, changeable anytime (ev: cg-data-training-optout). Confidence: High that it
  is documented.
- `[FACT]` **Temporary Chats** provide an ephemeral mode: deleted after 30 days, not used to
  train, reviewable "only to monitor for abuse" (ev: cg-temporary-chats-retention).
- `[FACT]` A documented **control limit**: turning off memory/personalisation "does not
  disable safety features" that may use limited safety-relevant context in rare, high-risk
  situations (ev: cg-safety-context). An honest, material caveat to user control.
- `[FACT]` Data-control capability is **plan-dependent** — Team/Enterprise/Edu offer
  additional controls (ev: cg-business-data-controls).
- `[FACT]` **Source transparency** for personalisation is documented via the "sources"
  affordance (ev: cg-ux-memory-sources-affordance), though the vendor notes it may not show
  every factor.
- `[INFERENCE]` ChatGPT's *documented* data-control surface is comparatively detailed and
  candid about limits (training opt-out, ephemeral chats, an explicit safety-context
  exception) (ev: cg-data-training-optout, cg-temporary-chats-retention, cg-safety-context).
  Confidence: Moderate — documentation is candid, but efficacy is unobserved.
- `[HYPOTHESIS]` Because deletion spans many surfaces (see §7) and a safety-context exception
  persists, a user's effective control may be weaker than the settings imply — untested.

**Evidence gaps (trust/control):** in-answer uncertainty signalling, citation accuracy,
reversibility/cancellation of actions, and whether controls behave as documented are all
`[UNTESTED]` (protocol §6, §8, §9, §10). No sub-area is scored negatively for missing
evidence.

## 9. Business-model analysis

_Framework: `frameworks/business-model/framework.md`. Boundary note: this describes how the
product creates/captures value; it does **not** value the company or forecast revenue._

- `[FACT]` ChatGPT is packaged as a **tiered consumer product** (Free, Go, Plus, Pro) plus
  Business/Enterprise (ev: cg-plans-overview). Confidence: High.
- `[FACT]` Pricing is **region-localised**: $20/month Plus in the US help article
  (ev: cg-plus-identity-price) vs ₹1,999/month in the observed (INR) pricing page
  (ev: cg-pricing-region-inr). These are not merged into one figure.
- `[FACT]` The **free tier is a capped funnel** — "Limited" messages, uploads, memory and
  deep research (ev: cg-free-tier-limits) — with a usage-based **expansion path** into Pro
  ("5x or 20x more usage") (ev: cg-pro-usage-tiers).
- `[FACT]` **Advertising** is now part of monetisation: the Go plan card states it "may
  include ads" (ev: cg-ads-go-plan), corroborated by documented ad controls
  (ev: cg-ads-controls). Confidence: High that ads exist on at least one tier.
- `[FACT]` **Data controls are a plan differentiator** (business tiers get more)
  (ev: cg-business-data-controls).
- `[INFERENCE]` The model combines **subscription tiers, usage-based upsell, and advertising**
  — a multi-pronged capture strategy where even a paid tier (Go) may carry ads (ev:
  cg-ads-go-plan, cg-pro-usage-tiers, cg-free-tier-limits). Confidence: Moderate.
- `[HYPOTHESIS]` Introducing ads on a *paid* tier suggests pressure to monetise the large
  free/low-tier base beyond subscriptions — plausible but not evidenced by financials, which
  are out of scope. Confidence: Speculative.

**Evidence gaps (business model):** revenue, margins, switching costs, distribution deals and
ecosystem lock-in are **not** evidenced here and are not speculated on. Exact free-tier limits
are unquantified ("Limited"). Prices are region- and time-sensitive.

## 10. Workflow-change analysis

_Populated in a later commit._

## 11. Cross-dimensional findings

_Populated in the synthesis commit._

## 12. Scoring record

See `scores.yaml` (validated against `schemas/scoring-record.schema.json`), added in the
synthesis commit.

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
