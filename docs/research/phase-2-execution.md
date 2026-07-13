# Phase 2 Execution Document

Phase 2 is the **Pilot Teardown and Methodology Stress-Test Phase**. Its goal is not to
produce polished teardowns for their own sake, but to run the Phase 1 research system
against three real products — ChatGPT, Claude and Perplexity — and learn where the system
holds, where it strains, and what must change before the library scales.

This document audits the Phase 1 foundation and sets out how Phase 2 will be executed.

## 1. Audit of the Phase 1 foundation

Confirmed present and passing at the start of Phase 2 (repository at 50 commits):

- **Methodology** (`docs/methodology/`): workflow, unit of analysis, inclusion/selection
  criteria, evidence hierarchy, source types, citation standard, recency policy,
  fact/observation/inference/hypothesis distinction, confidence rubric.
- **Governance** (`docs/governance/`): claim verification, triangulation, reproducibility,
  bias and conflicts, corrections and disputes, versioning, archival, ethics, privacy,
  methodology limitations.
- **Frameworks** (`frameworks/`): the six dimensions plus relationships, comparison
  principles, qualitative scoring, and the no-false-precision rules.
- **Schemas** (`schemas/`): `product-metadata`, `evidence-record`, `scoring-record`.
- **Tooling** (`src/product_intelligence/`): typed validation package with `pi-validate`
  discovery/audit runner; 34 tests; `ruff`, `mypy`, `pytest` all green; CI on 3.11/3.12.

Baseline validation at Phase 2 start: `pytest` 34 passed, `ruff check .` clean, `mypy src`
clean, `pi-validate` reports 0 records (expected — no teardowns existed yet).

## 2. Existing strengths (what we expect to hold)

- **Claim classification and evidence grading** should map cleanly onto documentation-based
  research.
- **The no-false-precision scoring model** (ordinal, per-sub-area, no composites) is
  well-suited to comparing products that are not truly commensurable.
- **The evidence-record schema's `type` and `evidence_tier`** cover the source hierarchy
  this phase depends on.
- **Discovery-based `pi-validate`** already validates any record we drop into `evidence/`
  and `library/`.

## 3. Expected methodology stress points (hypotheses to test)

These are predictions, to be confirmed or refuted and recorded in the Phase 2 methodology
stress-test (commit 44):

- **H-S1:** The evidence schema lacks structured fields Phase 2 needs — plan/tier, region,
  access date as a first-class field, evidence directness (direct vs vendor-self-reported),
  product-version ambiguity, and expiry sensitivity. Likely a **schema problem**.
- **H-S2:** The evidence hierarchy does not cleanly encode "vendor states X about its own
  product" — official documentation is a primary source but is self-reported, not observed
  behaviour. Likely a **framework/documentation problem**.
- **H-S3:** Interaction-dependent dimensions (memory behaviour, failure recovery,
  cancellation) cannot be evidenced from documentation alone and will produce many
  **evidence gaps** unless direct interaction is available.
- **H-S4:** Comparison across products with different product boundaries (an assistant vs an
  answer engine) risks category error; the comparison rules may need sharpening. Likely a
  **comparison problem**.
- **H-S5:** No structured representation exists for evidence gaps and untested claims;
  they currently live only in prose.

## 4. Research dependencies

- **Web discovery** (search) to locate official sources.
- **Web/browser fetch** to read official documentation, help centres, pricing, privacy and
  terms pages, and to record faithful summaries or short quotations with access dates.
- **Local toolchain** (`.venv`) for validation after every change.

## 5. Evidence-access constraints (measured, not assumed)

Capabilities were probed before research began (2026-07-13):

| Capability            | Result on official sources                                              |
| --------------------- | ----------------------------------------------------------------------- |
| Web search            | Available; used for **discovery only**, never as primary evidence.      |
| Direct fetch (WebFetch) | Works for some official hosts (e.g. `claude.com`, `support.claude.com`); returns HTTP 403 for others (`openai.com`, `chatgpt.com`, `help.openai.com`, `perplexity.ai`). |
| In-app browser        | Renders official help/support pages that block direct fetch; used to read and quote primary sources. |
| Authenticated product use | **Not available.** No signed-in sessions to ChatGPT, Claude or Perplexity paid plans are used in this phase. |

**Consequence:** This phase relies on **official documentation and publicly accessible
pages**, read via fetch or the in-app browser. It does **not** claim authenticated,
paid-plan, or logged-in product interaction. Behaviour that can only be confirmed by using
the product on a specific plan is marked **untested** and handed to a human-testing protocol
(`docs/research/interaction-test-protocol.md`). Regional differences, paid-plan restrictions
and inaccessible pages are documented as evidence gaps rather than bypassed.

## 6. Evidence conventions for Phase 2

Until the schema is extended (planned commit 46), each evidence record uses the Phase 1
`evidence-record` schema and records the additional Phase 2 attributes in its `notes` field
using a `key=value` convention, plus `tags`:

- `plan=` the plan/tier the claim applies to (or `unspecified`).
- `region=` region context (default `global/US-default` where the source does not specify).
- `directness=` one of `direct` (we observed it), `vendor-self-reported` (official docs), or
  `indirect` (credible third-party).
- `confidence=` High / Moderate / Low / Speculative (per the Phase 1 rubric).
- `product_version=` interface/version context where identifiable, else `ambiguous`.

That this metadata cannot yet be validated structurally is itself a Phase 2 finding
(see H-S1) and motivates the schema extension.

## 7. Success criteria

Phase 2 succeeds if:

1. Three complete teardowns exist, each meeting the teardown quality checklist, with **every
   analytical conclusion referencing evidence-record identifiers**.
2. At least 60 validated evidence records exist (≥20 per product), each citing a real,
   dated, official-first source — with **zero fabricated sources, URLs, prices or features**.
3. Interaction-dependent questions are explicitly marked untested, not guessed.
4. A cross-product comparison exists that compares specific design choices in context and
   contains **no global winner ranking**.
5. Methodology friction is documented and classified, and schema/tooling changes are made
   **only where Phase 2 evidence demonstrates a real need**, each change justified.
6. The final repository passes `pytest`, `ruff check .`, `mypy src`, `pi-validate`, plus the
   Phase 2 evidence audit.

## 8. Non-goals for Phase 2

- No global product ranking or "best assistant" verdict.
- No revenue speculation without reliable evidence.
- No treating model capability as product capability.
- No Phase 3 framework deepening (deferred).
