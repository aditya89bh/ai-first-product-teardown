# Teardown: Claude

> **Pilot teardown (Phase 2).** Documentation-first, public-evidence-only. No authenticated
> or paid-plan interaction was performed. Every analytical conclusion cites evidence-record
> ids under `evidence/claude/`. Claims are labelled `[FACT]`, `[OBS]`, `[INFERENCE]` or
> `[HYPOTHESIS]`; documentation claims are vendor-self-reported unless directly observed.
>
> **Material disclosure:** this pilot was executed within a Claude Code environment. See
> §14 for the conflict-and-bias note. It is disclosed transparently here in the research
> content; it is deliberately kept out of Git metadata.

## 1. Research scope

- **Product surface studied:** Claude consumer web application (`claude.ai` / `claude.com`)
  and official Claude support (`support.claude.com`), privacy (`privacy.claude.com`) and
  pricing documentation.
- **Access mode:** logged-out / documentation-first. `claude.com`, `support.claude.com` and
  `privacy.claude.com` were reachable via direct fetch; cited with access dates.
- **Plan/tier:** Free by default; paid-tier facts (Pro, Max, Team, Enterprise) taken only
  from official pages and marked plan-specific.
- **Region:** pricing read in USD; treated as US-default and flagged where relevant.
- **Research date:** 2026-07-13.
- **Capabilities included:** documented chat, Projects, Artifacts, web search, file analysis,
  memory, and privacy/data controls.
- **Capabilities excluded:** Claude API / developer platform, Claude Code, mobile/desktop
  specifics, enterprise admin, and any behaviour requiring an authenticated or paid session.
- **Evidence limitations:** most behavioural claims are vendor-self-reported; interaction-
  dependent behaviour is `[UNTESTED]`.
- **Version ambiguity:** no explicit product version string; findings dated to 2026-07-13.

## 2. Product metadata

See `metadata.yaml`. Summary: Claude, teardown v0.1.0, status active, observation window
2026-07-13, review by 2026-10-13.

## 3. Source inventory

See `source-inventory.md`. Official-first; access notes recorded.

## 4. Evidence coverage

See `source-inventory.md` (source-to-evidence map) and §13. Evidence records live in
`evidence/claude/`.

## 5. User experience analysis

_Populated in a later commit._

## 6. Agent-behaviour analysis

_Populated in a later commit._

## 7. Memory analysis

_Populated in a later commit._

## 8. Trust and control analysis

_Populated in a later commit._

## 9. Business-model analysis

_Populated in a later commit._

## 10. Workflow-change analysis

_Populated in a later commit._

## 11. Cross-dimensional findings

_Populated in the synthesis commit._

## 12. Scoring record

See `scores.yaml`, added in the synthesis commit.

## 13. Evidence gaps

_Populated across dimension commits and consolidated in the synthesis commit._

## 14. Limitations

_Populated in the synthesis commit (includes the conflict/bias note)._

## 15. Reproduction instructions

_Populated in the synthesis commit._

## 16. Update triggers

_Populated in the synthesis commit._

## 17. Facts, observations, inferences and hypotheses

Each dimension section separates these explicitly using the `[FACT]` / `[OBS]` /
`[INFERENCE]` / `[HYPOTHESIS]` labels.
