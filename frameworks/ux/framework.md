# UX Analysis Framework

> **Scope note.** This is a *foundational* framework. It defines what the dimension covers,
> why it matters, what evidence it needs, and how it is evaluated — enough to produce
> rigorous teardowns. Later phases deepen it into detailed sub-rubrics. It is not exhaustive.

## What is being analysed

The **user experience** of an AI-first product: how a person understands what the product
can do, forms intent, hands work to it, interprets what it does, and recovers when things go
wrong. Unlike conventional UX, the interface is often open-ended (natural language) and the
system's behaviour is probabilistic, so the analysis centres on *interaction under
uncertainty* rather than fixed screens and flows.

## Why it matters

In AI-first products the interface is the product's theory of how humans and models should
collaborate. Good UX here is what lets a user get value without either over-trusting a
fallible system or fighting it. Poor UX shows up as confusion about capability, brittle
"prompt-guessing", and silent failures the user cannot detect or repair.

## Sub-areas (foundational)

1. **Capability legibility** — how well the product communicates what it can and cannot do,
   and its boundaries, before and during use.
2. **Intent expression** — how the user forms and conveys a goal (natural language, forms,
   examples, controls) and how much effort correct expression requires.
3. **Feedback and legibility of action** — how clearly the product shows what it is doing,
   what it did, and why, while and after acting.
4. **Error recovery and repair** — how a user notices a wrong result and corrects it; the
   cost and clarity of getting back on track.
5. **Effort and friction** — the work the interface demands relative to the value returned,
   including cognitive load from uncertainty.
6. **Onboarding and progressive disclosure** — how a new user reaches first useful outcomes
   and learns the product's real (not marketed) capabilities.

## What evidence is required

- **First-hand observation (E1)** of real interaction flows under a recorded
  [unit of analysis](../../docs/methodology/unit-of-analysis.md), including deliberate
  error and recovery scenarios.
- **Primary material (E2)** for stated onboarding and capability claims, kept separate from
  observed behaviour.
- Repeated trials to account for non-determinism in feedback and recovery.

## How the evidence is evaluated

- Behavioural claims (e.g., "the product surfaces what it is about to do") require
  observation and repetition, not a single screenshot.
- Claims about intended UX (from docs) are labelled as stated design, not experience.
- Each sub-area yields **qualitative, bounded judgements** with confidence levels — never a
  numeric UX score (see [false precision](../scoring-false-precision.md)).

## What can be concluded

- How legible, low-friction and recoverable the experience is *for the studied unit and
  scenarios*, with evidence and confidence.
- Specific patterns and anti-patterns in delegation, feedback and repair.

## What cannot be concluded

- That the observed experience generalises to all users, tasks, tiers or contexts.
- Anything about users' internal satisfaction without evidence (we observe behaviour and
  friction, not feelings).
- Intent behind a design choice beyond a labelled, confidence-rated inference.

## How another researcher can reproduce or challenge

Re-run the documented interaction and error-recovery scenarios under the same unit of
analysis, compare observed feedback and repair behaviour, and dispute specific claims with
their own observations via the [corrections process](../../docs/governance/corrections-and-disputes.md).

## Relationship to other dimensions

UX is where [trust and control](../trust/framework.md) and [agent behaviour](../agent-behaviour/framework.md)
become tangible to the user. See [dimension relationships](../dimension-relationships.md).
