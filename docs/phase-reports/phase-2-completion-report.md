# Phase 2 Completion Report

Phase 2 — the **Pilot Teardown and Methodology Stress-Test Phase** — is complete. It took the
repository from 50 to 100 commits by producing three evidence-backed pilot teardowns
(ChatGPT, Claude, Perplexity), a cross-product comparison, and a methodology/tooling
stress-test, all under strict evidence rules.

## Objective and outcome

The goal was **not** to declare a winner but to test whether the Phase 1 method works against
real products. It does — with one large qualification: the method supports **documented-design**
conclusions well and **behavioural** conclusions poorly without authenticated product
interaction, which was unavailable this phase. That finding is the phase's main result.

## Evidence produced

- **68 validated evidence records** (≥ the 60 target; ≥20 per product): ChatGPT 26, Claude 22,
  Perplexity 20.
- **Sources per product (official-first):** ChatGPT 5, Claude 6, Perplexity 5 — every URL was
  actually retrieved during the 2026-07-13 window; no source, URL, price or feature was
  invented.
- **1 source inventory, 1 teardown, 1 scoring record per product**, **1 comparison dataset**,
  **6 per-dimension comparison documents**, and **1 evidence-gap register**.

## Direct product interactions actually performed

- **Read-only, unauthenticated** access to public pages via the in-app browser (for sites that
  return HTTP 403 to direct fetch: `help.openai.com`, `chatgpt.com`, `perplexity.ai`) and via
  direct fetch (for `claude.com`, `support.claude.com`, `privacy.claude.com`).
- Direct **observations** recorded (marked `evidence_directness: direct`): the ChatGPT pricing
  page layout, its region-localised INR pricing, the Go-plan ads notice, free-tier limits, and
  the agentic-tooling list — all on the public pricing page.

## Interactions that could NOT be performed (and are marked `[UNTESTED]`)

Authenticated/paid sessions were unavailable, so these were not tested for any product:
first-use UX, agent planning/clarification/failure-recovery, cancellation, memory
edit/delete/import efficacy, in-answer uncertainty signalling, and — most importantly —
**Perplexity citation accuracy**. All are routed to `docs/research/interaction-test-protocol.md`.

## Validation results (final)

| Check | Result |
| ----- | ------ |
| `pytest` | 45 passed |
| `ruff check .` | clean |
| `mypy src` | clean (4 source files) |
| `pi-validate` | 74 records, 0 failed |
| `pi-evidence-audit` | **0 errors**, 68 warnings, 5 info |
| JSON schemas parse | 3/3 ok |
| YAML validity | all ok |
| Internal doc links | 0 broken |

The evidence audit's **0 errors** confirms no broken evidence references, no orphan records,
and that every High-confidence score is triangulated. The 68 warnings are records still using
the legacy `notes` provenance convention (finding F1); the 5 info items are expiry-sensitive
facts.

## Methodology changes made (evidence-gated, additive only)

- **Evidence-directness clarification** (F2): dated Phase 2 addendum to the evidence hierarchy
  — vendor documentation is self-report; confidence attaches to the specific claim.
- **Plan/region scoping reinforcement** (F5/F6).
- **"Not rated over negative" now mechanically checked** by the evidence audit (F7).
- **Schema extended** with optional Phase 2 fields: `plan_tier`, `region`,
  `evidence_directness`, `product_version`, `expiry_sensitive`, `untested`, `contradicts` (F1);
  all additive, so the 68 records remained valid.
- **New tooling:** `pi-evidence-audit` (broken/orphan references, triangulation, provenance
  coverage, expiry), with tests and a committed report; wired into CI.

No Phase 1 document was rewritten; the six frameworks and the confidence rubric were unchanged
(deepening is Phase 3). Full log: `docs/research/phase-2-methodology-changes.md`.

## Major evidence gaps

- **Behavioural dimensions** (agent behaviour, memory efficacy, workflow) are `Not rated` for
  all three products — the dominant gap.
- **Perplexity:** citation accuracy (highest-value untested question); Brain memory controls;
  standard consumer Pro/Max prices (only Education Pro $10/mo was stated).
- **ChatGPT:** exact free-tier limits ("Limited"); non-INR/US pricing beyond $20 / ₹1,999.
- **Claude:** whether import/export and deletion behave as documented; non-USD pricing.

## Where comparison proved misleading (and was avoided)

- Direct **price** comparison is partly invalid (ChatGPT read in INR, Claude in USD, Perplexity
  consumer prices missing) — recorded separately, never merged.
- **Answer-engine vs assistant** capability is a category error — no such comparison was made.
- **Model vs product**: all three expose multiple models; Perplexity resells third-party
  (OpenAI/Anthropic/Google) models — no model-capability claims were made.

## Honest quality assessment

- **Strong:** every conclusion is evidence-cited and classified; documented data-control and
  memory models are well triangulated (notably the three-way training-default contrast —
  ChatGPT opt-out, Claude opt-in, Perplexity opt-out); no fabrication; gaps are explicit; the
  tooling genuinely catches broken references and untriangulated scores.
- **Limited:** behavioural coverage is thin by necessity (no authenticated interaction), so the
  teardowns are best read as *documented-design* analyses, not usability verdicts. Provenance
  metadata is structured on only 3 representative records; the other 65 still use the `notes`
  convention (surfaced honestly by the audit).
- **Conflict disclosed:** the Claude teardown discloses that this pilot ran within a Claude Code
  environment and documents the mitigations; disclosure is in the research content, not Git
  metadata, per repository rules.

## Recommended scope for Phase 3

1. **Close behavioural gaps via interaction** — execute `interaction-test-protocol.md` on
   authenticated accounts (recording plan/region/date), converting `[UNTESTED]` items into
   `observation` evidence; prioritise Perplexity citation accuracy and memory-control efficacy.
2. **Backfill structured provenance** on the 65 legacy records (drive audit warnings toward 0).
3. **Deepen the six frameworks** into detailed sub-rubrics (the deferred Phase 3 core), informed
   by these pilots.
4. **Add a scoring `basis` field** ("documented" vs "observed") (finding F8).
5. **Broaden pricing/region capture** (multi-region reads) and add a first-class evidence-gap
   record type if the prose register proves insufficient at scale.

Stopping after Phase 2 as instructed.
