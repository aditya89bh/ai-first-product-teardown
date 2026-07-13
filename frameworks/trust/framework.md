# Trust and Control Analysis Framework

> **Scope note.** Foundational framework. It defines coverage, rationale, evidence and
> evaluation — enough for rigorous teardowns, to be deepened later. Not exhaustive.

## What is being analysed

How the product helps a user **calibrate trust and exercise control** over a fallible,
autonomous system: how it communicates uncertainty and limits, what oversight and
intervention it offers, how reversible its actions are, and how it handles permissions and
consequential operations. This dimension is about the *governance surface* between the human
and the agent.

## Why it matters

An AI-first product asks the user to delegate work to a system that will sometimes be wrong.
Whether that delegation is safe depends on control: can the user see what will happen,
intervene before harm, and undo mistakes? Trust that is not backed by real control is
misplaced trust — and products can manufacture unwarranted trust as easily as warranted
trust. This dimension distinguishes the two.

## Sub-areas (foundational)

1. **Uncertainty and limit communication** — how the product signals when it is unsure, and
   how honestly it represents its own limits.
2. **Oversight and intervention** — the user's ability to preview, pause, approve, or stop
   the agent before and during action.
3. **Permissions and scope of action** — what the agent is allowed to do, how that is
   granted, and whether scope is legible and constrained.
4. **Reversibility and recovery** — whether consequential actions can be undone, and how
   safely the product handles irreversible ones.
5. **Consequential-action handling** — how the product treats high-stakes operations
   (sending, purchasing, deleting, sharing): confirmation, friction, and safeguards.
6. **Trust calibration** — whether the product's presentation encourages trust proportional
   to its actual reliability, or over/under-states it.

## What evidence is required

- **First-hand observation (E1)** of oversight, permission, confirmation and undo flows —
  including deliberately triggering consequential and uncertain scenarios — under a recorded
  [unit of analysis](../../docs/methodology/unit-of-analysis.md).
- **Primary material (E2)** for stated safeguards and permission models, kept separate from
  observed behaviour.
- Tests of whether controls actually function (does "stop" stop; does "undo" undo).

## How the evidence is evaluated

- A control counts only by its **observed effect**, triangulated across trials — stated
  safeguards that do not demonstrably work are labelled as claims, not facts.
- Trust-calibration judgements compare the product's *presentation of confidence* against its
  *observed reliability* (linking to [agent behaviour](../agent-behaviour/framework.md)).
- All judgements are qualitative and bounded with confidence levels; no composite "trust
  score" (see [false precision](../scoring-false-precision.md)).

## What can be concluded

- The presence, legibility, and observed efficacy of oversight, permission, and undo
  mechanisms for the studied unit, with confidence.
- Whether trust appears well-calibrated or mis-calibrated relative to observed reliability —
  a central finding of this dimension.

## What cannot be concluded

- That safeguards will hold in untested scenarios or against determined adversaries.
- The product maker's intent behind a control choice beyond a labelled inference.
- Legal or regulatory compliance; we describe control behaviour, not legal status.

## How another researcher can reproduce or challenge

Re-run the documented oversight, permission and consequential-action scenarios under the same
unit of analysis, and compare whether controls behave as described.

## Relationship to other dimensions

Trust and control governs [agent behaviour](../agent-behaviour/framework.md), depends on
[memory](../memory/framework.md) (control over stored state), and is experienced through
[UX](../ux/framework.md). See [dimension relationships](../dimension-relationships.md).
