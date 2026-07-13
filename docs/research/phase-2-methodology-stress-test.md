# Phase 2 Methodology Stress-Test Findings

This document records every methodology failure, ambiguity or friction encountered while
producing the three pilot teardowns, each classified by type:

`documentation` · `schema` · `framework` · `evidence-access` · `comparison` ·
`researcher-judgement`

It is the primary deliverable of Phase 2. Fixes made in response are in
`docs/research/phase-2-methodology-changes.md` (only where evidence demonstrated a real need)
and in the schema/tooling commits that follow.

## Findings

### F1 — Evidence schema has no structured fields for Phase 2 attributes
- **Type:** schema (confirms hypothesis H-S1).
- **What happened:** the required Phase 2 attributes — plan/tier, region, evidence directness
  (direct vs vendor-self-reported vs indirect), product-version ambiguity, and expiry
  sensitivity — had no schema fields, so they were stuffed into `notes` as `key=value` text
  (e.g. `plan=Plus; region=US; directness=vendor-self-reported`). This is not
  machine-validatable and cannot be audited.
- **Impact:** high — undermines the machine-readable promise for exactly the metadata Phase 2
  needs most.
- **Fix:** extend the evidence-record schema with optional typed fields (commit 46).

### F2 — The hierarchy conflates "primary source" with "observed behaviour"
- **Type:** framework / documentation (confirms H-S2).
- **What happened:** official documentation is `primary`/E2, but it is *vendor self-report*,
  not observed behaviour. A documented feature supports only the fact *that the vendor states
  it*. The evidence hierarchy and confidence rubric did not force this distinction, so it had
  to be maintained by hand in every `claim_support` and analysis line.
- **Impact:** high — the single biggest source of potential over-claiming.
- **Fix:** add an `evidence_directness` field (schema) and a documentation note clarifying that
  confidence attaches to *what is being claimed* — "High that it is documented" ≠ "High that
  the behaviour occurs" (commits 45, 46).

### F3 — No structured representation for evidence gaps and untested claims
- **Type:** schema / framework (confirms H-S5).
- **What happened:** gaps and `[UNTESTED]` items lived only in prose (teardown §13 and the gap
  register). They cannot be counted, audited, or linked to interaction-protocol categories
  mechanically.
- **Impact:** medium — gaps are first-class in the method but second-class in the data.
- **Fix:** add an `untested` marker to evidence records and an audit that reports gaps
  (commits 46, 48).

### F4 — Direct fetch blocked on some vendors; no authenticated interaction
- **Type:** evidence-access (confirms H-S3).
- **What happened:** `openai.com`, `chatgpt.com`, `help.openai.com` and `perplexity.ai`
  returned HTTP 403 to direct fetch; they were read via the in-app browser instead.
  Authenticated/paid sessions were unavailable, so agent-behaviour, memory-efficacy and
  workflow dimensions are largely `[UNTESTED]`.
- **Impact:** high on coverage — behavioural conclusions could not be reached.
- **Fix:** none to the method; documented as a standing constraint and routed to the
  interaction protocol. Access method recorded per source.

### F5 — Region-localised pricing created ambiguity
- **Type:** evidence-access / schema.
- **What happened:** the ChatGPT pricing page rendered in **INR** while the US help article
  said **$20**. Without a `region` field, this risked being mis-recorded as a contradiction.
- **Impact:** medium.
- **Fix:** add a `region` field and record prices per region, never merged (commit 46).

### F6 — Comparing different product theses risks category error
- **Type:** comparison (confirms H-S4).
- **What happened:** Perplexity (answer engine) vs ChatGPT/Claude (assistants) are not
  commensurable on "capability"; price comparison was partly invalid (INR vs USD vs missing).
  The Phase 1 comparison principles held up, but required constant vigilance and explicit
  "not comparable here" statements.
- **Impact:** medium — method held, but is easy to violate.
- **Fix:** documentation reinforcement, not a rule change (commit 45); the comparison docs make
  scope differences explicit per claim.

### F7 — "Not rated" vs a low score risks converting gaps into negatives
- **Type:** researcher-judgement.
- **What happened:** several sub-areas (e.g. Perplexity memory controls) had thin documentation.
  The temptation is to score them low; the rule requires `Not rated`/`Speculative`. This
  judgement recurred and needed a firm convention.
- **Impact:** medium — a real risk to fairness.
- **Fix:** documentation clarification plus an audit check that flags high-confidence claims and
  unsupported scores (commits 45, 48).

### F8 — Scoring needed a "documented-only" qualifier
- **Type:** schema / researcher-judgement.
- **What happened:** most scoreable sub-areas judge *what the vendor documents*, not observed
  behaviour. The scoring schema had no way to mark this, so it was noted only in `rationale`.
- **Impact:** low-medium.
- **Fix:** clarified via rationale convention now; a structured `basis` field is a candidate for
  a later phase (recorded, not yet built — Phase 3).

### F9 — Research-environment conflict of interest (Claude teardown)
- **Type:** researcher-judgement.
- **What happened:** the pilot runs within a Claude Code environment while tearing down Claude.
  The Phase 1 bias/COI policy covered *how* to disclose but the pilot had to decide *where*
  (research content, not Git metadata) and *how* to mitigate (identical method, no favourable
  scoring).
- **Impact:** medium — credibility.
- **Fix:** explicit conflict/bias note in the Claude teardown §14; no method change needed, the
  policy worked.

## Summary by type

| Type | Findings |
| ---- | -------- |
| schema | F1, F3, F5, F8 |
| framework | F2, F3 |
| documentation | F2, F6 |
| evidence-access | F4, F5 |
| comparison | F6 |
| researcher-judgement | F7, F8, F9 |

**Overall:** the Phase 1 *method* held — classification, evidence grading, no-false-precision
scoring, and comparison guardrails all worked. The main real needs are **schema fields** for
Phase 2 attributes (F1, F5), a **directness distinction** (F2), and **structured gap/untested
handling** (F3), all addressed in the following commits. Everything else is documentation
reinforcement or a standing access constraint.
