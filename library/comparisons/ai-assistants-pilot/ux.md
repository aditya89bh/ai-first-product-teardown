# Cross-Product UX Comparison

> **No global ranking.** This compares specific documented design choices and the contexts in
> which they may help or hinder, per `frameworks/cross-product-comparison.md`. All in-product
> chat UX is `[UNTESTED]` for every product; comparisons are of *documented design*, not
> observed experience. Scope: consumer web surface, documentation-first, 2026-07-13.

## Comparison 1 — Primary interaction model

- **Dimension:** UX · **Design choice:** what the product optimises the main surface for.
- **ChatGPT:** general open-ended assistant surface; personalisation controls under a single
  Settings > Personalization area (ev: cg-ux-settings-navigation). 
- **Claude:** work organised around **Projects** (persistent, scoped containers) and
  **Artifacts** (shareable outputs) (ev: cl-projects, cl-artifacts).
- **Perplexity:** **answer-first** — synthesised direct answers with citations instead of link
  lists (ev: px-ux-direct-answers, px-identity-answer-engine).
- **User context:** open-ended creation favours ChatGPT/Claude framing; fast verifiable
  look-ups favour Perplexity's framing.
- **Scope difference:** these are different product theses; "better UX" is not comparable
  across them.
- **Confidence:** Moderate (documented design). **Limitation:** actual usability untested.

## Comparison 2 — In-context transparency affordances

- **Design choice:** surfacing *why*/*from where* an answer came, at the point of use.
- **ChatGPT:** a "sources" book-icon reveals personalisation provenance, but "may not show
  every factor" (ev: cg-ux-memory-sources-affordance).
- **Claude:** memory viewable/editable in Settings > Capabilities; incognito toggled by a
  ghost icon at chat start (ev: cl-ux-memory-settings-location, cl-ux-incognito-affordance).
- **Perplexity:** inline **citations** on answers plus a visible **reasoning breakdown** in Pro
  Search (ev: px-citations, px-pro-search-planning-visible).
- **User context:** Perplexity's inline citations make source-checking part of the normal read
  loop; ChatGPT/Claude expose provenance more in settings/affordances than inline.
- **Confidence:** Moderate. **Limitation:** whether these affordances are discoverable and
  accurate in practice is untested.

## Comparison 3 — Point-of-use privacy control

- **Design choice:** how easily a user can start a non-remembered session.
- **ChatGPT:** Temporary Chats (memory-free) (ev: cg-temporary-chats-memory).
- **Claude:** incognito via a ghost icon when starting a chat (ev: cl-ux-incognito-affordance,
  cl-incognito).
- **Perplexity:** not documented on the pages read (evidence gap).
- **User context:** ChatGPT and Claude both document a salient, per-chat ephemeral mode;
  Perplexity's equivalent (if any) is unevidenced here.
- **Confidence:** Moderate for ChatGPT/Claude; **not rated** for Perplexity (gap).

## What cannot be concluded (UX)

- No claim about which product is "easier to use" — that needs the interaction protocol.
- No cross-plan or cross-region UX generalisation.
- Absence of a documented affordance (e.g. Perplexity incognito) is a **gap**, not a negative
  finding.
