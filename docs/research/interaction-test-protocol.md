# Reproducible Product-Interaction Test Protocol

Several of the six dimensions — especially agent behaviour, memory, trust/control and
workflow change — can only be fully evidenced by **using the product**. Phase 2 research is
documentation-first and does **not** use authenticated or paid-plan sessions, so most of
these tests are **specified here but not executed**. This protocol exists so that a human (or
a later, interaction-capable session) can run the tests reproducibly and close the
corresponding evidence gaps.

**Status legend used throughout the teardowns:**
`[UNTESTED]` — specified here, not run this phase. `[DIRECT]` — actually observed this phase.

## How to run a test (when interaction is available)

For each test, record: product, **surface** (web app), **plan/tier**, **region**,
**date/time**, the **exact prompt or action**, the **settings** in effect (model picker,
toggles), and a **faithful description of what happened**. Do **not** enter private or
sensitive information. Save the notes as an `observation`-type evidence record with a
`unit_ref` and `directness=direct`. Run each test at least twice to account for
non-determinism, and report frequencies, not single outcomes.

## Standard test categories

Each category lists a neutral, reproducible task usable across all three products. Tasks are
deliberately generic and contain no sensitive data.

1. **First-use orientation.** From a fresh, logged-out or newly-created session, record what
   the first screen presents: input affordances, examples, capability/limit disclosure.
2. **Information retrieval.** Ask a factual question with a knowable answer and record whether
   sources are shown, how many, and how they are attributed.
3. **Multi-step task handling.** Give a task requiring several steps (e.g. "outline, then
   draft, then summarise") and record whether the product plans, sequences, and exposes steps.
4. **Clarification behaviour.** Give a deliberately ambiguous request and record whether the
   product asks a clarifying question or proceeds on an assumption.
5. **Correction handling.** After an initial answer, correct one detail and record whether the
   correction is incorporated and whether prior context is retained.
6. **Source presentation.** For a claim-bearing answer, record whether citations are present,
   clickable, and whether the cited source actually supports the claim.
7. **Memory disclosure and control.** Locate any "memory"/"saved info" setting; record what it
   says is stored, and test whether viewing, editing, and deleting behave as documented.
8. **Uncertainty communication.** Ask something the product is likely unsure about and record
   whether it signals uncertainty or answers with unwarranted confidence.
9. **Failure recovery.** Induce a failure (e.g. an impossible or malformed request) and record
   whether it fails loudly, asks for help, or fabricates.
10. **User override and cancellation.** Start a long generation and attempt to stop/cancel;
    record whether cancellation works and what state results.

## Cross-cutting rules

- **Two runs minimum** per test; note variation.
- **Plan matters.** Record the plan; never generalise a paid-tier result to the free tier.
- **Region matters.** Record region; features roll out unevenly.
- **Separate observation from interpretation.** The record states what happened; the teardown
  interprets it as a labelled inference.

## Evidence gaps this protocol is designed to close

Because this phase does not execute these tests, the following are marked `[UNTESTED]` in the
teardowns and listed in the evidence-gap register: clarification behaviour, correction
handling, memory edit/delete efficacy, uncertainty signalling, failure recovery, and
cancellation. Documentation claims about these behaviours are recorded as
`vendor-self-reported` and are **not** promoted to observed facts.

## What was actually performed this phase

Direct interactions performed in Phase 2 are limited to reading **publicly accessible,
unauthenticated** pages (documentation, help centres, pricing) via fetch and the in-app
browser. Any such access is recorded per source with its access date. No authenticated
product sessions, paid-plan features, or logged-in memory settings were exercised. Each
teardown's reproduction-instructions section states this explicitly.
