# Business-Model Analysis Framework

> **Scope note.** Foundational framework. It defines coverage, rationale, evidence and
> evaluation — enough for rigorous teardowns, to be deepened later. Not exhaustive.
>
> **Boundary note.** This framework analyses *how a product appears to create and capture
> value*. It does **not** value companies, forecast revenue, or give investment advice (see
> [non-goals](../../docs/vision/non-goals.md)).

## What is being analysed

The **economic logic** of the product as it is observable from the outside: how it is
packaged and priced, how value is created for and captured from users, what the cost drivers
of AI-first delivery imply, and how the pricing model interacts with the product's behaviour
and incentives. This is product-level economics, not company-level finance.

## Why it matters

AI-first products have distinctive economics: inference has a real marginal cost, capability
scales with spend, and pricing choices (per-seat, usage-based, tiered, free) shape both user
behaviour and the incentives baked into the product. Understanding the business model
explains *why* a product behaves as it does — for example, why it limits, meters, or nudges
usage in particular ways.

## Sub-areas (foundational)

1. **Packaging and tiers** — how the product is divided into editions and what distinguishes
   them.
2. **Pricing model** — the observable pricing structure (per-seat, usage-based, tiered,
   freemium) and how it is presented.
3. **Value creation** — what value the product claims and is observed to deliver, and to whom.
4. **Value capture** — how the product converts that value into revenue, and the friction or
   alignment between what users value and what they pay for.
5. **Cost-structure implications** — what the economics of AI delivery (metering, limits,
   throttling) reveal about cost drivers, inferred cautiously.
6. **Incentive alignment** — whether the business model's incentives align with or work
   against the user's interest (e.g., engagement vs task completion).

## What evidence is required

- **Primary material (E2)**: pricing pages, tier descriptions, terms — the strongest source
  for packaging and price, dated per the [recency policy](../../docs/methodology/recency-policy.md)
  because pricing changes often.
- **First-hand observation (E1)** of paywalls, limits, metering and upgrade prompts under a
  recorded [unit of analysis](../../docs/methodology/unit-of-analysis.md).
- **Independent reporting (E3)** for context, used carefully and never as a substitute for
  primary pricing evidence.

## How the evidence is evaluated

- Pricing and packaging facts rest on primary sources, dated, because they are highly
  volatile.
- Statements about cost structure and margins are **inferences** from observable behaviour
  (limits, metering) and are explicitly labelled and confidence-rated — we do not have
  internal financials.
- Incentive-alignment judgements are inferences linking observed model behaviour to the
  pricing structure, not assertions.

## What can be concluded

- The observable packaging, pricing and value-capture mechanics for the studied unit and
  date, with confidence.
- Cautious inferences about cost drivers and incentive alignment, clearly labelled.

## What cannot be concluded

- Company revenue, margins, valuation, or commercial success (out of scope and unobservable).
- Whether the product is a good investment (explicitly a non-goal).
- Future pricing, which is speculative unless announced.

## How another researcher can reproduce or challenge

Re-capture the pricing and packaging sources (dated), re-run the paywall and metering
observations under the same unit of analysis, and compare.

## Relationship to other dimensions

The business model shapes [agent behaviour](../agent-behaviour/framework.md) (limits,
metering) and [UX](../ux/framework.md) (upgrade prompts, gating), and its incentives bear on
[trust](../trust/framework.md). See [dimension relationships](../dimension-relationships.md).
