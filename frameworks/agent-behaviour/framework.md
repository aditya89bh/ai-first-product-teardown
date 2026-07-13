# Agent-Behaviour Analysis Framework

> **Scope note.** Foundational framework. It defines coverage, rationale, evidence and
> evaluation for the dimension — enough for rigorous teardowns, to be deepened in later
> phases. Not exhaustive.

## What is being analysed

How the product's **agent behaves** when given work: what it does autonomously versus with
confirmation, how it plans and sequences steps, how it uses tools or takes actions, how
reliably it does the right thing, and how it behaves at the edges (ambiguity, failure,
adversarial input). This dimension studies the *behaviour of the acting system*, distinct
from how that behaviour is presented (UX) or trusted (trust and control).

## Why it matters

An AI-first product's value and risk both live in what its agent actually does. Two products
with similar interfaces can differ enormously in autonomy, reliability, and failure
behaviour. Because behaviour is probabilistic, understanding it requires characterising
*distributions and tendencies*, not single outputs.

## Sub-areas (foundational)

1. **Autonomy and initiative** — how much the agent does on its own versus asking; whether
   it acts, proposes, or waits, and under what conditions.
2. **Planning and decomposition** — whether and how it breaks work into steps, sequences
   them, and adapts when steps fail.
3. **Tool and action use** — how it invokes external tools or takes real-world actions;
   scope of what it can do and how it decides to do it.
4. **Reliability and consistency** — how often it does the right thing across repeated
   trials; variance in behaviour for similar inputs.
5. **Failure behaviour** — what it does when it cannot succeed: does it stop, ask, guess,
   fabricate, or fail loudly versus silently.
6. **Robustness at the edges** — behaviour under ambiguity, unusual inputs, and adversarial
   or manipulative prompts.

## What evidence is required

- **First-hand observation (E1)** across **repeated trials** under a recorded
  [unit of analysis](../../docs/methodology/unit-of-analysis.md), covering normal, ambiguous,
  and failure scenarios.
- Reported behaviour frequencies ("did X in N of M runs"), not single anecdotes.
- **Primary material (E2)** for stated capabilities and limits, kept separate from observed
  behaviour.

## How the evidence is evaluated

- Behavioural claims require repetition and [triangulation](../../docs/governance/triangulation.md);
  a behaviour seen once is an observation, not a characterisation.
- Reliability is described in bounded, qualitative terms with reported frequencies and
  conditions — never a single "accuracy score" that hides variance or scope.
- Claims about *why* the agent behaves a way are inferences with confidence levels, since
  internals are usually opaque.

## What can be concluded

- The agent's observed tendencies in autonomy, planning, tool use, reliability and failure
  *for the studied unit and scenarios*, with frequencies and confidence.
- Whether failure is generally loud or silent, and whether the agent fabricates when
  uncertain — both high-value findings.

## What cannot be concluded

- Guaranteed behaviour on any single future run (non-determinism forbids this).
- Behaviour outside the tested scenarios, tiers or inputs.
- Internal mechanism or intent beyond labelled, confidence-rated inference.

## How another researcher can reproduce or challenge

Re-run the documented scenarios for the same unit of analysis, record behaviour frequencies,
and compare. Disagreement is resolved by comparing procedures and sample sizes, not by
trading single anecdotes.

## Relationship to other dimensions

Agent behaviour is what [trust and control](../trust/framework.md) surfaces must govern and
what [UX](../ux/framework.md) must make legible. See
[dimension relationships](../dimension-relationships.md).
