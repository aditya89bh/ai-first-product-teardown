# Cross-Product Trust and Control Comparison

> **No global ranking.** Compares documented data-control and transparency choices. Efficacy is
> `[UNTESTED]`; all claims are vendor-self-reported unless marked `[OBS]`. Scope: consumer web
> surface, documentation-first, 2026-07-13.

## Comparison 1 — Training default (the clearest three-way contrast)

- **ChatGPT:** **opt-out** — "Improve the model for everyone" is on and can be turned off
  anytime, signed-in or signed-out (ev: cg-data-training-optout).
- **Claude:** **opt-in** — consumer chats are used for training only "if you choose to allow"
  (ev: cl-training-optin).
- **Perplexity:** **opt-out** — "AI Data Retention is enabled by default" for Free/Pro/Max,
  with a toggle to opt out; opt-out is **non-retroactive** (ev: px-training-optout-default,
  px-training-optout-limits).
- **User context:** a privacy-conscious user gets the most favourable default from Claude
  (opt-in); ChatGPT and Perplexity require action to opt out.
- **Confidence:** High that these defaults are documented. **Limitation:** enforcement is
  vendor-stated and untested; this is about *defaults*, not overall privacy.

## Comparison 2 — Ephemeral / non-retained mode

- **ChatGPT:** Temporary Chats — deleted after 30 days, not trained on, no memory
  (ev: cg-temporary-chats-retention).
- **Claude:** incognito — not saved to memory/history, excluded from training even if
  model-improvement is on (ev: cl-incognito, cl-incognito-training-excluded).
- **Perplexity:** not documented on pages read (gap).
- **Confidence:** High (ChatGPT/Claude documented). **Limitation:** retention claims not
  independently verifiable.

## Comparison 3 — Candour about control limits

- **ChatGPT:** documents a safety-context exception that persists despite personalisation being
  off (ev: cg-safety-context) — candid.
- **Claude:** documents long-tail retention — opt-in data up to 5 years, safety data 2–7 years
  (ev: cl-retention-5year, cl-retention-violations) — candid.
- **Perplexity:** documents that opt-out is non-retroactive and prior training data can't be
  removed (ev: px-training-optout-limits) — candid.
- **Observation:** all three disclose meaningful limits rather than overstating control — a
  positive commonality, stated as an inference. Confidence: Moderate.

## Comparison 4 — Source transparency in answers

- **Perplexity:** inline citations are central, plus visible planning
  (ev: px-citations, px-pro-search-planning-visible) — strongest documented.
- **ChatGPT / Claude:** personalisation-source affordance (ChatGPT) and offered web search
  (Claude), but in-answer citation behaviour is untested
  (ev: cg-ux-memory-sources-affordance, cl-web-search).
- **User context:** for verify-as-you-read research, Perplexity's inline-citation model is the
  most directly supportive **as documented**.
- **Confidence:** Moderate. **Limitation (critical):** citation *accuracy* is untested for all.

## Comparison 5 — Third-party model data handling (Perplexity-specific)

- **Perplexity** uniquely must address third-party model providers: it documents Zero Data
  Retention / Zero Data Training agreements with OpenAI, Anthropic and others for Enterprise
  (ev: px-enterprise-no-training). Not applicable to ChatGPT/Claude (first-party models).

## What cannot be concluded (trust/control)

- Which product is "most private" overall — defaults differ, but efficacy, retention practice
  and in-answer honesty are untested.
- Whether any control behaves as documented — untested for all three.
- No cross-plan generalisation (business tiers differ from consumer on all three).
