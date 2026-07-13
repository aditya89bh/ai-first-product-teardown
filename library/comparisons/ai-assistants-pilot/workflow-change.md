# Cross-Product Workflow-Change Comparison

> **No global ranking.** Net workflow effect is `[UNTESTED]` for all three; this compares the
> *documented intent* of how each restructures work. Scope: consumer web surface,
> documentation-first, 2026-07-13.

## Comparison 1 — The core workflow each targets

- **ChatGPT:** broad knowledge work — drafting, research (Deep Research), automation (Scheduled
  tasks, Projects) (ev: cg-agent-tooling-offered, cg-agent-deep-research).
- **Claude:** structured project work and buildable outputs — Projects + Artifacts + tool
  integrations (ev: cl-projects, cl-artifacts, cl-agent-integrations).
- **Perplexity:** research/question-answering — collapse "search many pages" into one cited
  answer (ev: px-pro-search-steps, px-ux-direct-answers).
- **Confidence:** Moderate that these are the documented targets. **Limitation:** actual effect
  untested.

## Comparison 2 — Steps removed vs steps added

- **Removed (documented intent):** all three claim to remove collation/repetition — Perplexity
  removes manual source-sifting (ev: px-pro-search-steps); ChatGPT/Claude reduce repetition via
  memory (ev: cg-memory-how-it-works, cl-memory-how-it-works).
- **Added (inferred):** each introduces a **verification step** — checking outputs, and for
  ChatGPT/Claude, checking *why* memory shaped an answer (ev: cg-ux-memory-sources-affordance).
  Perplexity's inline citations make the added check **easier to perform in place**
  (ev: px-citations). Confidence: Low (inferred, untested).

## Comparison 3 — Output artifacts vs answers

- **Claude:** Artifacts as first-class shareable outputs (ev: cl-artifacts).
- **Perplexity:** Create files and apps — dashboards, spreadsheets, web apps
  (ev: px-create-files-apps).
- **ChatGPT:** Projects/Canvas/Codex offered (ev: cg-agent-tooling-offered).
- **User context:** for "produce a shareable artifact" workflows, Claude and Perplexity both
  document dedicated surfaces; which fits depends on the artifact type. Confidence: Moderate.

## Comparison 4 — New dependencies / failure modes (inferred)

- **All:** delegating creates a dependency on output correctness; a new failure mode is
  *confident-but-wrong* output that the user must catch. For Perplexity specifically, a
  citation that does not support its claim is a distinctive failure mode
  (ev: px-citations) — high-impact and untested.
- **Confidence:** Low/Speculative — these are hypotheses for interaction testing.

## What cannot be concluded (workflow change)

- No claim about which product saves more time or changes work "more" — all untested.
- No aggregate productivity claims (out of scope; require dedicated studies).
- Net effect is `Not rated` for every product pending the interaction protocol.
