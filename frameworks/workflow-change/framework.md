# Workflow-Change Analysis Framework

> **Scope note.** Foundational framework. It defines coverage, rationale, evidence and
> evaluation — enough for rigorous teardowns, to be deepened later. Not exhaustive.

## What is being analysed

How the product **changes the way work gets done**: which tasks it takes over, which it
augments, how the human's role shifts (from operator to supervisor, from author to editor),
what new steps it introduces (reviewing, correcting, prompting), and how it fits into or
disrupts an existing workflow. This dimension studies the product's effect on the *unit of
work*, not just the product in isolation.

## Why it matters

The defining promise of AI-first products is that they change *how* work happens, not just
*where* a button is. The most important effects are often second-order: a task becomes
faster but requires new verification steps; a role shifts from doing to reviewing; a skill
atrophies or a new one becomes essential. These shifts determine whether a product genuinely
helps or merely relocates the work.

## Sub-areas (foundational)

1. **Task reallocation** — which tasks move to the agent, which stay with the human, and
   which are newly created (e.g., prompt-crafting, output-checking).
2. **Role shift** — how the human's role changes (operator → supervisor, author → editor,
   maker → reviewer) and what that demands of them.
3. **New workflow steps** — steps the product introduces, including verification, correction,
   and re-prompting overhead.
4. **Fit and disruption** — how well it integrates with existing tools and workflows versus
   forcing new ones.
5. **Skill and capability effects** — what skills become more or less necessary, and where
   over-reliance risks arise.
6. **Net workflow effect** — on balance, and with evidence, whether the product reduces total
   work and friction or shifts it elsewhere.

## What evidence is required

- **First-hand observation (E1)** of completing representative real tasks end to end with the
  product, under a recorded [unit of analysis](../../docs/methodology/unit-of-analysis.md),
  attending to the *new* steps it introduces, not only the ones it removes.
- **Primary/independent material (E2/E3)** for stated workflow claims and documented
  integrations, kept separate from observed effects.
- Corroborated user reports (E4) about workflow effects, used cautiously and triangulated.

## How the evidence is evaluated

- Claims about workflow effects rest on observed end-to-end task completion, not on the
  product's marketing of time saved.
- We explicitly account for **induced work** (verification, correction) so that "faster" is
  not claimed while ignoring new overhead.
- Net-effect judgements are inferences with confidence levels, scoped to the observed tasks
  and unit — never generalised to "all work".

## What can be concluded

- How the product reallocates tasks and shifts roles for the *observed tasks and unit*, with
  evidence and confidence, including the new steps it introduces.
- Where over-reliance or skill effects are plausible, as labelled inferences or hypotheses.

## What cannot be concluded

- Aggregate productivity effects across an organisation or population (unobservable here;
  such claims require dedicated studies we do not run).
- Long-term skill effects, which are hypotheses unless supported by longitudinal evidence.
- That workflow effects observed for one task type transfer to others.

## How another researcher can reproduce or challenge

Complete the same representative tasks end to end under the same unit of analysis, recording
both removed and induced steps, and compare the net-effect assessment.

## Relationship to other dimensions

Workflow change is the downstream consequence of [agent behaviour](../agent-behaviour/framework.md)
and [UX](../ux/framework.md), and is shaped by [business-model](../business-model/framework.md)
incentives. See [dimension relationships](../dimension-relationships.md).
