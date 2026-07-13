# Phase 2 Research Protocol

This protocol defines the concrete steps for producing each pilot teardown. It operationalises
the Phase 1 [research workflow](../methodology/research-workflow.md) for the specific
conditions of Phase 2: documentation-first research, limited to public sources, without
authenticated product interaction.

## 1. Research sequence (per product)

1. **Scope.** Fix the product surface, access mode, plan, region and research date in
   `metadata.yaml` (validated against `schemas/product-metadata.schema.json`).
2. **Source discovery.** Build the official-source inventory (`source-inventory.md`).
3. **Evidence collection.** Create evidence records (`evidence/<product>/*.yaml`), one source
   → one claim, official sources first.
4. **Dimension analysis.** Work through the six frameworks, citing evidence-record ids for
   every conclusion.
5. **Synthesis.** Cross-dimensional findings, scoring record, evidence gaps, limitations,
   reproduction instructions, update triggers.
6. **Validation.** Run the full toolchain and fix any failure before moving on.

## 2. Source-discovery process

- Start from the product's **own domains**: help centre, pricing, privacy, security, terms,
  and official announcements/changelog.
- Use web search **only to locate** those official pages, never as evidence itself. When a
  search surfaces a claim, follow it to the underlying official source and cite that.
- Prefer sources in the Phase 2 order of preference (official docs → help centre → pricing →
  privacy/security/terms → announcements → accessible product UI → credible technical
  reporting → clearly-labelled researcher observation).
- Record every source in the inventory with its URL, type, ownership (first-party vs
  third-party) and access date.

## 3. Direct-observation protocol

- Direct observation is used **only where a public, unauthenticated product surface is
  actually reachable** and interaction genuinely occurs.
- When it does, record: the exact surface, the steps, the date, and whether a login/plan was
  required. Mark the resulting evidence `directness=direct` and `type: observation`, with a
  `unit_ref`.
- Where interaction requires authentication or a paid plan we do not have, **do not simulate
  it**. Mark the question untested and route it to the
  [interaction test protocol](interaction-test-protocol.md).
- No private or sensitive information is entered into any product during research.

## 4. Claim classification

Every claim in a teardown is labelled per the Phase 1
[fact/observation/inference/hypothesis](../methodology/fact-inference-hypothesis.md) rule:

- **Fact** — established for the studied surface, triangulated where possible.
- **Observation** — something we directly saw on a reachable surface (rare this phase).
- **Inference** — reasoning from documentation/observation, with a confidence level.
- **Hypothesis** — untested proposition, explicitly flagged.

Crucially for this phase: **official documentation is a primary source but is
vendor-self-reported.** A documented feature supports the fact *that the vendor states it*,
and is at most an inference about *actual behaviour* until observed. Records mark this with
`directness=vendor-self-reported`.

## 5. Evidence-gap handling

- When a material question cannot be answered from available evidence, create an **explicit
  evidence gap** in the teardown's evidence-gaps section and in the shared
  [evidence-gap register](../../library/comparisons/ai-assistants-pilot/evidence-coverage.md)
  (built in commit 43).
- A gap records: the question, why it is unanswerable now (access, plan, region, ambiguity),
  and how it could be closed (usually via the interaction protocol).
- **Missing evidence is never converted into a negative score.** The relevant sub-area is
  scored `Not rated` with `Speculative` confidence.

## 6. Review process

- After each product, run the full validation checkpoint (tests, ruff, mypy, `pi-validate`,
  YAML/JSON validation, internal-link and evidence-reference checks) and confirm a clean
  tree.
- Every analytical conclusion is checked to ensure it cites at least one evidence-record id.
- Every high-confidence claim is checked for triangulation (≥2 independent records).
- Scope discipline is checked: no cross-plan generalisation, no model-as-product claims.

## 7. Honesty guarantees

- No source, URL, price, feature or quotation is invented. Every cited URL was actually
  retrieved during the research window; every quotation is faithful to the source.
- Current behaviour is not inferred from outdated announcements; dated sources are treated as
  dated.
- Marketing language is recorded as a vendor claim, never as verified behaviour.
