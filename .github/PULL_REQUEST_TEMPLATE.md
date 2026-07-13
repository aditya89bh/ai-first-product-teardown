<!-- See CONTRIBUTING.md before opening a pull request. -->

## What this changes

Briefly describe the change and link any related issue or dispute.

## Type

- [ ] Research content (teardown / evidence / comparison)
- [ ] Methodology, governance or framework
- [ ] Tooling, schema or tests
- [ ] Other (describe)

## Research checklist (for content changes)

- [ ] No fabricated facts, sources, quotes, URLs or statistics.
- [ ] Every claim is classified (fact / observation / inference / hypothesis).
- [ ] Every claim cites a graded evidence record.
- [ ] Non-trivial claims carry a confidence level.
- [ ] Synthetic examples are labelled *(synthetic)*.
- [ ] "What cannot be concluded" is present and non-empty (teardowns).
- [ ] Conflicts of interest are declared.
- [ ] No numeric or composite scores (ordinal scale only).

## Validation checklist (for tooling / structured data)

- [ ] `pytest` passes.
- [ ] `ruff check .` passes.
- [ ] `mypy src` passes.
- [ ] `pi-validate` passes (all structured records validate).
