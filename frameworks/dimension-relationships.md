# Relationships Between the Six Analytical Dimensions

The six dimensions — [UX](ux/framework.md), [agent behaviour](agent-behaviour/framework.md),
[memory](memory/framework.md), [trust and control](trust/framework.md),
[business model](business-model/framework.md), and [workflow change](workflow-change/framework.md)
— are analysed separately so that each rests on its own evidence. But they are not
independent: a product is a single system, and the dimensions describe different views of it.
This document defines how they relate, so that teardowns can connect findings without
collapsing the dimensions into one blurred verdict.

## Why separate, yet related

- **Separate** so that evidence for one does not silently leak into another, and so that a
  strong impression on one dimension (a slick UX) does not inflate judgements on others (a
  halo effect — see [bias](../docs/governance/bias-and-conflicts.md)).
- **Related** because the interesting findings are often at the *seams*: a business-model
  incentive that shapes agent behaviour, or a memory feature that expands the trust surface.

## The core relationships

- **Agent behaviour is the substrate.** What the agent actually does is the raw reality the
  other dimensions interpret. UX makes it legible; trust and control governs it; workflow
  change is its downstream effect; the business model shapes its constraints.
- **UX is the interface layer.** It is where agent behaviour, memory and trust become
  perceptible to the user. A control that exists but is invisible in the UX is, for the user,
  nearly absent.
- **Memory feeds trust and behaviour.** Stored state changes agent behaviour over time and
  expands what the user must be able to see and control — so memory findings frequently
  imply trust-and-control findings.
- **Trust and control governs behaviour.** Oversight, permissions and reversibility are the
  mechanisms that make delegating to a fallible agent safe; they are meaningless without the
  behaviour they constrain.
- **Business model sets incentives.** Pricing and cost structure shape what the agent is
  allowed to do, how it is metered, and what the UX nudges toward — often explaining
  *why* the other dimensions look as they do.
- **Workflow change is the outcome.** It is the net second-order effect of the other five on
  how work actually gets done.

## Relationship diagram

```text
              business model (incentives, constraints)
                         │
                         ▼
   memory ──▶ agent behaviour ──▶ workflow change
     │              │
     ▼              ▼
   trust & control ◀┘
        │
        ▼
       UX  (makes all of the above legible to the user)
```

The arrows indicate "shapes / constrains / surfaces", not strict causation. Every arrow is a
place where a cross-dimension finding may live.

## Rules for using relationships in a teardown

1. **Evidence stays within its dimension.** A cross-dimension claim must be supported by
   evidence appropriate to *each* dimension it touches, not borrowed from one to prop up the
   other.
2. **Name the seam explicitly.** When a finding spans dimensions (e.g., "metering limits
   drive the agent's early-stopping behaviour"), state which dimensions and cite evidence for
   each side of the link.
3. **Cross-links are inferences.** A causal link between dimensions is an inference with a
   confidence level unless directly observed.
4. **No collapsing.** Relationships connect findings; they never justify a single overall
   score across dimensions (see [false precision](scoring-false-precision.md)).

## Principle

The dimensions are lenses on one system. Kept separate, they keep the evidence honest; read
together, they reveal how a product's economics, memory, behaviour, controls and interface
add up to its effect on work. The value of the framework is in holding both truths at once.
