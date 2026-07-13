# Cross-Product Agent-Behaviour Comparison

> **No global ranking.** Documented behaviour and observed page facts are kept separate from
> actual agent behaviour, which is `[UNTESTED]` for all three. Scope: consumer web surface,
> documentation-first, 2026-07-13.

## Important separation: documented vs observed

Nothing in this comparison establishes how well any agent *actually* plans, clarifies, or
recovers from failure — those are behavioural and were not tested. What follows compares the
**documented/offered** agent surface and, where marked `[OBS]`, directly observed page facts.

## Comparison 1 — Offered agentic surface

- **ChatGPT** `[OBS]`: pricing table lists Search, Deep research, Codex, Scheduled tasks,
  Projects, built-in browser, "Workspace agents" (ev: cg-agent-tooling-offered); Deep Research
  documented on Plus (ev: cg-agent-deep-research).
- **Claude:** web search, Artifacts, and integrations (Google Workspace, JIRA, Zapier,
  Intercom) (ev: cl-web-search, cl-artifacts, cl-agent-integrations).
- **Perplexity:** Pro Search multi-step retrieve-and-synthesise, a code interpreter, and
  per-session model choice (ev: px-pro-search-steps, px-code-interpreter, px-pro-search-models).
- **Scope difference:** ChatGPT documents the broadest agent/automation surface; Perplexity's
  is search-centric; Claude's is tool-integration-centric.
- **Confidence:** Moderate that these are offered. **Limitation:** breadth of offering ≠
  quality of behaviour.

## Comparison 2 — Planning visibility

- **Design choice:** whether the product shows the user how it approached a task.
- **Perplexity:** explicitly documents showing "how the AI broke down your question and
  approached the research" (ev: px-pro-search-planning-visible) — the most explicit of the
  three.
- **ChatGPT / Claude:** the documentation read did not describe an equivalent user-facing
  plan-exposure for standard chat (evidence gap; not a negative finding).
- **User context:** visible planning may help users trust and correct multi-step research.
- **Confidence:** Moderate for Perplexity (documented); **not rated** for the others (gap).
  **Limitation:** whether a shown plan reflects the true process is untested for Perplexity too.

## Comparison 3 — Model choice as an agent-behaviour lever

- **ChatGPT** `[OBS]`: multiple models exposed via a picker, tier-gated (ev: cg-models-offered).
- **Claude:** the product page frames Claude as the assistant; model choice less foregrounded
  in the docs read (partial).
- **Perplexity:** per-session choice among Sonar, GPT-5, Claude Sonnet 4.6, Gemini 3.1 Pro
  (ev: px-pro-search-models) — and it **resells third-party models** (ev: px-model-choice).
- **Scope difference (critical):** for Perplexity, "the agent" orchestrates *other companies'*
  models; equating its behaviour with any one model is a category error.
- **Confidence:** High that model choice is offered; **no capability claims** are made.

## What cannot be concluded (agent behaviour)

- Which product plans, clarifies, or recovers from failure "better" — all untested.
- Anything about reliability/consistency (needs repeated trials per the interaction protocol).
- That a broader offered surface implies better or safer behaviour.
