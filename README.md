# AI-First Product Teardown

A **Product Intelligence Research Library**: systematic, evidence-based teardowns of
AI-first products, examined through six analytical dimensions — user experience, agent
behaviour, memory, trust and control, business model, and workflow change.

This repository is built to function like the working archive of a small research
institution, not a collection of opinion pieces. Every teardown separates what is
**observed** from what is **inferred** and what is **hypothesised**, records the
evidence behind each claim, and documents a method that another researcher can
reproduce or challenge.

---

## The thesis

AI-first products are not conventional software with a model bolted on. They introduce
properties that older product frameworks do not describe well:

- Behaviour is **probabilistic**, so the same input can produce different outputs.
- The system **accumulates state about the user** (memory) in ways that change the
  product over time.
- Users must decide **how much to trust and how much to control** an agent that acts
  on their behalf.
- The **unit of work shifts** from "operate the tool" to "delegate and supervise".

These properties change how such products should be evaluated. This library develops
and applies a shared analytical vocabulary for doing that evaluation rigorously.

## Who this is for

| Audience          | What they get                                                            |
| ----------------- | ------------------------------------------------------------------------ |
| Founders          | Structured teardowns of how AI-first products earn trust and retention.  |
| Product leaders   | A repeatable method for evaluating agent UX, memory and control surfaces.|
| Designers         | Concrete patterns and anti-patterns for delegation, feedback and repair. |
| Researchers       | Reproducible methods, an evidence hierarchy, and machine-readable data.  |
| Students          | A worked example of disciplined product research and analysis.           |

## What makes this different

- **Evidence before conclusions.** Claims are graded, sourced and dated. Unsupported
  opinion is out of scope.
- **Facts, inferences and hypotheses are kept separate.** See
  [`docs/methodology/fact-inference-hypothesis.md`](docs/methodology/fact-inference-hypothesis.md).
- **Machine-readable and human-readable.** Teardowns are Markdown; evidence and scores
  are validated YAML/JSON against JSON Schema.
- **Reproducible.** Every teardown documents how it was produced so it can be re-run
  and disputed.
- **Honest about limits.** Each analysis states what *cannot* be concluded.

## Repository map

```text
docs/         Vision, methodology, governance, architecture, roadmap
frameworks/   The six analytical dimensions and how they relate
schemas/      JSON Schema definitions for machine-readable records
templates/    Canonical templates for teardowns and evidence records
library/      Product teardowns (Phase 2+) and cross-product comparisons
evidence/     Evidence records supporting claims
src/          Python validation tooling (product_intelligence package)
tests/        Test suite for the tooling
```

## Project status

**Phase 1 — Foundation.** This phase establishes the research architecture,
methodology, governance and validation tooling. **No product teardowns exist yet**;
they begin in Phase 2. See the [roadmap](docs/roadmap/roadmap.md) for the full plan.

## Contributing

Read [`CONTRIBUTING.md`](CONTRIBUTING.md) and the
[methodology](docs/methodology/) before proposing a teardown. Contributions are held to
the evidence and reproducibility standards described there.

## Licence

Content and code are released under the terms in [`LICENSE`](LICENSE).
