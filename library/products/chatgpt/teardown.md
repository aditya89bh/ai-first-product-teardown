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
