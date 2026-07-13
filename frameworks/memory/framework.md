# Memory Analysis Framework

> **Scope note.** Foundational framework. It defines coverage, rationale, evidence and
> evaluation — enough for rigorous teardowns, to be deepened later. Not exhaustive.

## What is being analysed

How the product **accumulates, uses, exposes and forgets state about the user** over time:
what it remembers, how memory changes its behaviour, whether the user can see and control
what is stored, and how memory persists across sessions and surfaces. This dimension studies
the product as a system that *changes with use*, which conventional software frameworks
rarely address.

## Why it matters

Memory is what turns a stateless tool into something that feels personalised — and it is
where personalisation, privacy, and control collide. Memory shapes behaviour invisibly: a
product may act differently for two users, or for the same user over time, because of stored
state the user never sees. Analysing memory is therefore essential to understanding both the
value and the risk of an AI-first product.

## Sub-areas (foundational)

1. **What is retained** — the kinds of information the product appears to store (facts,
   preferences, history, derived profiles) and at what granularity.
2. **Persistence and scope** — how long memory lasts and across what boundaries (session,
   device, surface, account).
3. **Influence on behaviour** — how, and how visibly, stored state changes what the product
   does.
4. **Visibility and inspectability** — whether the user can see what is remembered about
   them, and how faithfully that view reflects reality.
5. **User control** — whether the user can add, correct, export, or delete memory, and how
   effective those controls are in practice.
6. **Forgetting and decay** — whether and how memory is removed, ages, or is overridden, and
   whether deletion is genuine or cosmetic.

## What evidence is required

- **First-hand observation (E1)** across sessions and accounts under a recorded
  [unit of analysis](../../docs/methodology/unit-of-analysis.md) — comparing fresh vs aged
  accounts, and behaviour before and after using memory controls.
- **Primary material (E2)** on stated memory features and retention, kept separate from
  observed behaviour.
- Tests of control efficacy: does "delete" actually stop the behaviour it should?

## How the evidence is evaluated

- Claims about *what* is stored are, where internals are opaque, **inferences from observed
  behaviour** ("acted on a previously stated preference"), labelled and confidence-rated.
- Control efficacy is judged behaviourally: a control is only as real as its observed effect,
  triangulated across trials.
- Stated retention (docs) is never conflated with observed retention.

## What can be concluded

- Observable memory behaviour and the *apparent* effectiveness of user controls for the
  studied unit, with confidence.
- Whether memory is inspectable and whether deletion appears genuine or cosmetic — both
  high-value findings.

## What cannot be concluded

- The exact internal storage mechanism or full contents of memory (usually unobservable).
- That absence of observed recall means nothing is stored (absence of evidence is not
  evidence of absence).
- Compliance or legal conclusions about data handling; we describe behaviour, not legal
  status.

## How another researcher can reproduce or challenge

Repeat the cross-session and control-efficacy procedures on fresh and aged accounts under
the same unit of analysis, and compare observed influence and deletion behaviour.

## Relationship to other dimensions

Memory directly feeds [trust and control](../trust/framework.md) (what can I see and delete?)
and shapes [agent behaviour](../agent-behaviour/framework.md) over time. See
[dimension relationships](../dimension-relationships.md).
