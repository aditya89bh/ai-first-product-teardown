<!--
CANONICAL PRODUCT TEARDOWN TEMPLATE
Copy this file into library/products/<product-slug>/teardown.md and fill every section.
Rules:
  - Classify EVERY claim as [FACT], [OBS], [INFERENCE] or [HYPOTHESIS].
  - Attach a confidence level (High / Moderate / Low / Speculative) to every non-trivial claim.
  - Cite evidence by record id, e.g. (ev: acme-pricing-2026-07). Never paste raw URLs inline.
  - Label any synthetic example explicitly as *(synthetic)*.
  - Do not delete a section. If it does not apply, write "Not applicable" and say why.
  - The "What cannot be concluded" section must be non-empty.
See docs/methodology/ and frameworks/ for the rules each section enforces.
-->

# Teardown: <Product Name>

## 1. Metadata

> Machine-readable metadata for this teardown lives in `metadata.yaml` alongside this file
> and must validate against `schemas/product-metadata.schema.json`. The summary below must
> match it.

- **Product:** <name>
- **Teardown version:** <MAJOR.MINOR.PATCH>
- **Status:** active | stale | deprecated | withdrawn
- **Observation window:** <YYYY-MM-DD> to <YYYY-MM-DD>
- **Last updated:** <YYYY-MM-DD>
- **Review by:** <YYYY-MM-DD>
- **Authors:** <names or handles>
- **Declared conflicts of interest:** <none | describe>

## 2. Unit of analysis

State the exact unit studied (product, edition/tier, surface, version/build, observation
window, account context). See `docs/methodology/unit-of-analysis.md`. A vague unit fails
review.

## 3. Summary

A short, plain-language summary a non-technical reader can follow. Every claim here must be
classified and must also appear, with full evidence, in the relevant dimension section below.

## 4. Dimension analysis

For each dimension, cover: what was observed, the classified claims, the score(s) with
rationale and confidence, and the evidence cited. Use the frameworks in `frameworks/`.

### 4.1 User experience
_(framework: `frameworks/ux/framework.md`)_

- **Findings:** `[OBS]` … / `[FACT]` … / `[INFERENCE]` … / `[HYPOTHESIS]` …
- **Score(s):** <sub-area>: <Strong|Adequate|Weak|Absent|Not rated> — rationale — confidence
- **Evidence:** (ev: …)

### 4.2 Agent behaviour
_(framework: `frameworks/agent-behaviour/framework.md`)_

- **Findings:** …
- **Score(s):** …
- **Evidence:** (ev: …)

### 4.3 Memory
_(framework: `frameworks/memory/framework.md`)_

- **Findings:** …
- **Score(s):** …
- **Evidence:** (ev: …)

### 4.4 Trust and control
_(framework: `frameworks/trust/framework.md`)_

- **Findings:** …
- **Score(s):** …
- **Evidence:** (ev: …)

### 4.5 Business model
_(framework: `frameworks/business-model/framework.md`)_

- **Findings:** …
- **Score(s):** …
- **Evidence:** (ev: …)

### 4.6 Workflow change
_(framework: `frameworks/workflow-change/framework.md`)_

- **Findings:** …
- **Score(s):** …
- **Evidence:** (ev: …)

## 5. Cross-dimension observations

Findings that live at the seams between dimensions (e.g., a business-model incentive shaping
agent behaviour). Name both dimensions and cite evidence for each side. See
`frameworks/dimension-relationships.md`. Cross-links are inferences unless directly observed.

## 6. What can be concluded

The defensible conclusions, each classified and confidence-rated, scoped to the unit of
analysis.

## 7. What cannot be concluded

**(Required, non-empty.)** The specific limits of this teardown: what the evidence does not
support, and why. See `docs/governance/methodology-limitations.md`.

## 8. Reproducibility note

How the product was accessed and over what dates; the key procedures used to generate
first-hand observations; factors that complicate exact reproduction; and what a challenger
should do to test the strongest and weakest claims. See
`docs/governance/reproducibility.md`.

## 9. Evidence index

List every evidence record id cited above, each pointing to a file under `evidence/`
validating against `schemas/evidence-record.schema.json`.

## 10. Changelog

| Version | Date | Type (MAJOR/MINOR/PATCH) | Change | Evidence (for conclusion changes) |
| ------- | ---- | ------------------------ | ------ | --------------------------------- |
| 0.1.0   | <YYYY-MM-DD> | — | Initial teardown | — |
