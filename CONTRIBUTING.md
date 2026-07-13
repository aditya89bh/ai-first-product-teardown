# Contributing

Thank you for considering a contribution. This is an **evidence-first research library**, so
contributions are held to research standards as much as engineering standards. You do not
need to write code to contribute meaningfully — research, evidence and corrections are
first-class contributions.

Please read the [methodology](docs/methodology/), [governance](docs/governance/) and the
relevant [frameworks](frameworks/) before proposing a teardown. The
[research workflow](docs/methodology/research-workflow.md) is the best starting point.

## Ways to contribute

| Contribution                | Code needed? | Where to start                                             |
| --------------------------- | ------------ | ---------------------------------------------------------- |
| Propose a product to study  | No           | Open a "Product proposal" issue                            |
| Contribute evidence         | No           | Add an evidence record from the YAML template              |
| Author or extend a teardown | No           | Copy the teardown template; follow the workflow            |
| Dispute or correct a claim  | No           | Open a "Correction / dispute" issue with evidence          |
| Improve methodology         | No           | Open a "Methodology proposal" issue                        |
| Improve validation tooling  | Yes          | See "Working on the tooling" below                         |

## Non-negotiable research rules

Every content contribution must follow these. Pull requests that violate them will be sent
back regardless of how well written they are.

1. **No fabrication.** Never invent facts, sources, quotes, URLs, findings or statistics.
2. **Classify every claim** as fact, observation, inference or hypothesis (see
   [fact-inference-hypothesis](docs/methodology/fact-inference-hypothesis.md)).
3. **Cite graded evidence.** Every claim links to an evidence record with an evidence tier
   (see [citation standard](docs/methodology/citation-standard.md)).
4. **Attach confidence** to non-trivial claims (see
   [confidence levels](docs/methodology/confidence-levels.md)).
5. **Label synthetic examples** explicitly as *(synthetic)*.
6. **State what cannot be concluded** — the teardown template requires it.
7. **Declare conflicts of interest** (see
   [bias-and-conflicts](docs/governance/bias-and-conflicts.md)).
8. **No false precision** — ordinal scores only, never numeric or composite (see
   [scoring-false-precision](frameworks/scoring-false-precision.md)).

## Submitting a teardown or evidence

1. Copy the relevant template from [`templates/`](templates/).
2. Place teardown files under `library/products/<product-slug>/` and evidence under
   `evidence/<product-slug>/`.
3. Ensure `metadata.yaml`, evidence records, and any `scores.yaml` validate (see below).
4. Open a pull request; a reviewer other than you will verify evidence, classification and
   reproducibility.

## Working on the tooling

Requirements: Python 3.11+.

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

Before opening a pull request, all of the following must pass:

```bash
pytest
ruff check .
mypy src
pi-validate          # validates every structured record in the repository
```

CI runs the same checks; a red build blocks merge.

## Commit and review conventions

- Use [conventional commits](https://www.conventionalcommits.org/) (e.g. `docs:`, `feat:`,
  `test:`, `ci:`, `fix:`).
- Keep each commit to one coherent change; do not bundle unrelated work.
- Be specific and evidence-backed in reviews; critique claims and evidence, not people (see
  the [code of conduct](CODE_OF_CONDUCT.md)).

## Reporting problems

- **Security or exposed sensitive data:** follow [`SECURITY.md`](SECURITY.md); do not open a
  public issue with details.
- **A wrong or unsupported claim:** open a "Correction / dispute" issue with your evidence.
