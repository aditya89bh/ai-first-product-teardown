# The Unit of Analysis for an AI-First Product

Before analysing a product we must define precisely *what* we are analysing. Ambiguity here
silently invalidates everything downstream: two researchers who disagree about the unit of
analysis are not actually studying the same thing, and their evidence cannot be compared.

## Definition

The **unit of analysis** is the specific, bounded configuration of a product that a teardown
studies. It is fixed at Stage 0 of the [workflow](research-workflow.md) and stated at the
top of every teardown.

A fully specified unit of analysis names all of the following:

| Element              | Question it answers                                | Example (synthetic)                     |
| -------------------- | -------------------------------------------------- | --------------------------------------- |
| Product              | Which product?                                     | "Acme Assistant" *(synthetic)*          |
| Edition / tier       | Which paid or free tier?                           | Free tier, no add-ons                   |
| Surface              | Which client or entry point?                        | Web app (not the mobile or API surface) |
| Version / build      | Which version, or what identifies it?              | Build visible in-product on capture day |
| Observation window   | Over what dates was it observed?                    | 2026-07-01 to 2026-07-10                |
| Account context      | New account, aged account, with/without memory?    | Fresh account, memory enabled           |

## Why AI-first products make this harder

Conventional software is relatively stable between releases. AI-first products complicate
the unit of analysis in specific ways that the definition above is designed to pin down:

- **Non-determinism.** The same input can yield different outputs, so "the product" must be
  understood as a distribution of behaviours over a window, not a single behaviour.
- **Silent model changes.** The underlying model can change without a version bump, so the
  observation window and capture date are part of the identity of what was studied.
- **Personalisation and memory.** Behaviour depends on accumulated state, so the account
  context (fresh vs aged, memory on vs off) is part of the unit, not a footnote.
- **Server-side configuration.** Feature flags and gradual rollouts mean two users on the
  "same version" may see different products; we record what *we* observed and treat it as a
  sample.

## Consequences for claims

- Every claim is implicitly scoped to the declared unit of analysis. A finding about the
  free web tier is **not** a finding about the enterprise API.
- Generalising beyond the unit is an **inference** at best and must be labelled and
  qualified as such (see [fact-inference-hypothesis](fact-inference-hypothesis.md)).
- If the product changes materially, the unit has changed; this triggers a new version of
  the teardown under the [versioning policy](../governance/versioning.md).

## Minimum standard

A teardown whose unit of analysis omits any required element cannot pass review. "We looked
at Product X" is not a unit of analysis; the table above, fully filled, is.
