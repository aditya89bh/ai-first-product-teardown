# Library Index

The library holds the applied output of the method: product teardowns and cross-product
comparisons. As of Phase 2 it contains the **AI-assistants pilot** — three teardowns and a
comparison produced to stress-test the Phase 1 methodology.

## Pilot: AI assistants / answer interfaces (2026-07-13)

| Product | Teardown | Scores | Sources | Evidence | Records |
| ------- | -------- | ------ | ------- | -------- | ------- |
| ChatGPT | [teardown](products/chatgpt/teardown.md) | [scores](products/chatgpt/scores.yaml) | [sources](products/chatgpt/source-inventory.md) | `evidence/chatgpt/` | 26 |
| Claude | [teardown](products/claude/teardown.md) | [scores](products/claude/scores.yaml) | [sources](products/claude/source-inventory.md) | `evidence/claude/` | 22 |
| Perplexity | [teardown](products/perplexity/teardown.md) | [scores](products/perplexity/scores.yaml) | [sources](products/perplexity/source-inventory.md) | `evidence/perplexity/` | 20 |

**Comparison:** [`comparisons/ai-assistants-pilot/`](comparisons/ai-assistants-pilot/) —
[dataset](comparisons/ai-assistants-pilot/comparison-dataset.yaml),
[UX](comparisons/ai-assistants-pilot/ux.md),
[agent behaviour](comparisons/ai-assistants-pilot/agent-behaviour.md),
[memory](comparisons/ai-assistants-pilot/memory.md),
[trust](comparisons/ai-assistants-pilot/trust.md),
[business model](comparisons/ai-assistants-pilot/business-model.md),
[workflow change](comparisons/ai-assistants-pilot/workflow-change.md),
[evidence coverage / gap register](comparisons/ai-assistants-pilot/evidence-coverage.md).

## How to READ a teardown

1. Start with **§1 Research scope** and **§14 Limitations** — they tell you what the teardown
   does and does not cover before you read any conclusion.
2. Each conclusion is labelled `[FACT]` / `[OBS]` / `[INFERENCE]` / `[HYPOTHESIS]` and cites
   evidence ids like `(ev: cg-memory-delete)`. Follow the id to `evidence/<product>/<id>.yaml`
   for the source, quotation, access date and directness.
3. Treat everything documentation-based as **vendor self-report** unless a record is marked
   `evidence_directness: direct`. Most behavioural questions are `[UNTESTED]` this phase.
4. Read **§13 Evidence gaps** and the shared
   [gap register](comparisons/ai-assistants-pilot/evidence-coverage.md) to see what is not
   established.

## How to REPRODUCE

1. Open the product's `source-inventory.md` and retrieve each source (note: some vendor sites
   return 403 to direct fetch and must be read in a browser).
2. Compare each quotation in the evidence records against the live page on your access date;
   record any drift (products change silently).
3. To close behavioural gaps, run `docs/research/interaction-test-protocol.md` on an
   authenticated account, recording plan, region, date and prompts, and add `observation`-type
   evidence records with `unit_ref`s and `evidence_directness: direct`.
4. Re-run `pi-validate` and `pi-evidence-audit`.

## How to CHALLENGE

- Disagree with a specific claim? Open a dispute per
  [`docs/governance/corrections-and-disputes.md`](../docs/governance/corrections-and-disputes.md),
  citing the evidence id and your counter-evidence, held to the same standards.
- Think a score is unfair? Scores are ordinal, per-sub-area, with a one-line rationale and
  evidence ids — challenge the rationale or the evidence, not a number (there is no overall
  score to argue about, by design).

## How to EXTEND

1. Copy the templates in [`../templates/`](../templates/) (teardown, evidence YAML, source
   inventory, research log).
2. Follow [`docs/research/research-protocol.md`](../docs/research/research-protocol.md).
3. Meet the teardown quality checklist (17 sections), cite evidence ids for every conclusion,
   and keep `pytest`, `ruff`, `mypy`, `pi-validate` and `pi-evidence-audit` green.
4. Add a row to this index.

## Provenance and honesty notes

- No source, URL, price, feature or quotation in these teardowns was invented; every cited URL
  was retrieved during the 2026-07-13 window.
- The Claude teardown carries a **conflict/bias disclosure** (this pilot ran within a Claude
  Code environment); see its §14.
- These are **pilot** teardowns: their purpose was to test the method. See
  [`docs/research/phase-2-methodology-stress-test.md`](../docs/research/phase-2-methodology-stress-test.md).
