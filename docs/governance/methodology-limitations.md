# Methodology Limitations and Known Failure Modes

A method that cannot state its own limits invites false confidence. This document records the
inherent limitations of our approach and the failure modes we are most likely to fall into,
so that readers can calibrate trust and contributors can guard against them. Naming these
weaknesses is a feature of the method, not an admission that it is broken.

## Inherent limitations

These are constraints we cannot fully remove; we manage them and disclose them.

- **Non-determinism.** Because AI-first products behave probabilistically, our observations
  are samples. We report tendencies and frequencies, never guaranteed behaviour, and any
  single observation may not reproduce.
- **Opacity.** We usually cannot see a product's internals — models, prompts, memory
  implementation, server-side logic. Much of our analysis is necessarily behavioural and
  inferential, and inferences about internals are labelled as such.
- **Silent change.** Products change without notice. Findings are dated snapshots; even a
  recent teardown may be describing a product that has since shifted.
- **Access asymmetry.** We typically study products from the outside, on available tiers.
  Behaviour on other tiers, regions, or account types may differ and is out of scope unless
  separately studied.
- **Sampling and coverage limits.** We cannot exercise every path of a complex product.
  Coverage is bounded, and absence of a finding is not evidence of absence.

## Known failure modes (and their guards)

These are ways the method can go wrong in practice. Each has a guard, but guards can fail.

| Failure mode                                   | Guard                                                        |
| ---------------------------------------------- | ----------------------------------------------------------- |
| Over-reading a single impressive interaction   | Triangulation and repeated trials before behavioural facts  |
| Presenting inference as fact                   | Mandatory claim classification; independent review          |
| Accepting vendor claims as observed behaviour  | Separating E2 (stated) from E1 (observed) evidence           |
| Findings quietly going stale                   | Recency policy, review-by dates, staleness flags            |
| Confirmation bias in evidence selection        | Disconfirmation requirement; recording contrary evidence    |
| False precision in scoring                     | Qualitative bounded scoring; no composite indices           |
| Bias from undisclosed conflicts                | COI declaration and recusal rules                           |
| Broken or moved sources                        | Archiving volatile sources at capture time                  |

## Limits on what teardowns can conclude

- We can characterise **behaviour and stated design** with evidence; we generally cannot
  prove **intent** or **internal mechanism** — only infer them, with stated confidence.
- We can describe **how a product appears to create and capture value**; we cannot forecast
  **commercial outcomes**.
- We can identify **patterns across products**; we cannot claim **causation** without
  evidence that supports it.

## Obligations this places on every teardown

- State the specific limitations that bear on *its* findings, not just these general ones.
- Populate a non-empty "what cannot be concluded" section.
- Reflect these limits in confidence levels rather than papering over them with confident
  prose.

## Principle

The method is a disciplined way of being *appropriately* uncertain about hard-to-observe
systems. Its honesty about its own limits is precisely what makes the claims it *does* make
worth trusting.
