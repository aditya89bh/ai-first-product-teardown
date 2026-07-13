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

_Framework: `frameworks/ux/framework.md`. Documentation-first; in-product chat UX is
`[UNTESTED]`._

- `[FACT]` Claude documents distinct interaction surfaces — chat, **Artifacts** (shareable
  creations), **Projects** (topic-scoped workspaces), Voice Mode and file analysis
  (ev: cl-identity-capabilities, cl-artifacts, cl-projects). Confidence: High that these are
  documented.
- `[FACT]` Memory is inspectable/editable from a single documented location, Settings >
  Capabilities > "View and edit memory" (ev: cl-ux-memory-settings-location).
- `[FACT]` A point-of-use privacy affordance is documented: a **ghost icon** toggles
  incognito chats when starting a chat outside a project (ev: cl-ux-incognito-affordance).
- `[INFERENCE]` Claude's UX appears to organise work around **persistent, scoped containers**
  (Projects) plus in-context privacy/memory affordances, suggesting a design emphasis on
  structured, resumable work (ev: cl-projects, cl-ux-memory-settings-location,
  cl-ux-incognito-affordance). Confidence: Moderate — documentation-based.
- `[HYPOTHESIS]` Surfacing an incognito toggle at the moment of starting a chat may make
  privacy choices more salient than burying them in settings — untested (route: interaction
  protocol §1, §7).

**Evidence gaps (UX):** first-use orientation, input structure, output/Artifact rendering,
error states, progressive disclosure and accessibility indicators are `[UNTESTED]` and require
an authenticated session (protocol §1, §2). Such sub-areas are `Not rated`.

## 6. Agent-behaviour analysis

_Framework: `frameworks/agent-behaviour/framework.md`. Behavioural sub-areas are `[UNTESTED]`._

- `[FACT]` The product offers agentic/tool-using surfaces — web search (ev: cl-web-search),
  Artifacts generation (ev: cl-artifacts), and external integrations with Google Workspace,
  JIRA, Zapier and Intercom (ev: cl-agent-integrations). Confidence: High that these are
  offered.
- `[INFERENCE]` The integration set and Artifacts suggest Claude is positioned for
  **tool-connected, output-producing work** (documents, tickets, automations), not only
  Q&A (ev: cl-agent-integrations, cl-artifacts). Confidence: Moderate — from feature listing,
  not observed execution.
- `[HYPOTHESIS]` Artifacts as a distinct, shareable output surface may change how much the
  agent *shows its work* versus embedding it in chat — untested (route: interaction protocol
  §3).

**Evidence gaps (agent behaviour):** task interpretation, planning visibility, clarification,
autonomy vs confirmation, failure recovery, intervention and boundary communication are all
`[UNTESTED]` (protocol §3–§5, §9, §10). Documentation shows *that* tools exist, not *how* the
agent behaves. These sub-areas are `Not rated`.

## 7. Memory analysis

_Framework: `frameworks/memory/framework.md`. Well documented; efficacy `[UNTESTED]`._

- `[FACT]` Claude maintains an **automatic synthesised memory** across chat history
  (ev: cl-memory-how-it-works), inspectable/editable in Settings > Capabilities
  (ev: cl-ux-memory-settings-location).
- `[FACT]` Memory is **scoped per Project** — each Project has a separate memory space and
  summary (ev: cl-memory-projects-separate) — a different model from a single global memory.
- `[FACT]` **Incognito chats** are not saved to memory or history (ev: cl-incognito).
- `[FACT]` Memory is available on **all plans**, but adjacent **chat search is paid-only**
  (ev: cl-chat-search-paid) — availability is plan-dependent.
- `[FACT]` Memory is **portable**: importable from and exportable to other AI providers
  (ev: cl-memory-import-export), though import is documented as **experimental** and "may not
  always" work (ev: cl-memory-import-experimental).
- `[INFERENCE]` Claude's memory model emphasises **scoping and portability** (per-project
  isolation, incognito, cross-provider import/export), which reads as a design stance toward
  user control and anti-lock-in (ev: cl-memory-projects-separate, cl-incognito,
  cl-memory-import-export). Confidence: Moderate — documentation-based.
- `[INFERENCE]` Portable memory is unusual and directly reduces switching costs — a memory
  finding with a business-model consequence (ev: cl-memory-import-export). Confidence:
  Moderate; import reliability is caveated (ev: cl-memory-import-experimental).
- `[HYPOTHESIS]` Per-project memory isolation may reduce cross-context "memory bleed" that a
  single global memory can cause — untested (route: interaction protocol §7).

**Evidence gaps (memory):** whether view/edit/delete and import actually behave as documented,
retrieval visibility, and cross-session continuity in practice are `[UNTESTED]`.

## 8. Trust and control analysis

_Framework: `frameworks/trust/framework.md`. Data-control surface well documented; in-answer
trust behaviour (uncertainty, citation accuracy) is `[UNTESTED]`._

- `[FACT]` Training on consumer chats is **opt-in** — used only if the user chooses to allow
  it (ev: cl-training-optin). Confidence: High that this is documented. (Contrast: ChatGPT
  documents an opt-**out**; see cross-product comparison.)
- `[FACT]` **Incognito** is a hard carve-out from training even if model-improvement is on
  (ev: cl-incognito-training-excluded), triangulated with the memory article (ev: cl-incognito).
- `[FACT]` **Deletion** is documented within 30 days of removal (ev: cl-retention-30day), but
  **opt-in data may be retained de-identified up to 5 years** (ev: cl-retention-5year) and
  **safety/violation data persists 2–7 years** (ev: cl-retention-violations) — documented
  limits on "deletion".
- `[INFERENCE]` Claude's data-control posture is **opt-in-by-default and candid about
  retention trade-offs** (5-year opt-in retention, 2–7 year safety retention stated openly)
  (ev: cl-training-optin, cl-retention-5year, cl-retention-violations). Confidence: Moderate
  — documentation-based, not verified.
- `[HYPOTHESIS]` Opt-in training (vs opt-out) may materially reduce the share of consumer data
  used for training relative to an opt-out product — plausible but unquantified and untested.
  Confidence: Speculative.

**Evidence gaps (trust/control):** in-answer uncertainty signalling, whether web-search
answers cite sources accurately, reversibility/cancellation, and whether controls behave as
documented are `[UNTESTED]` (protocol §6, §8, §9, §10). No sub-area scored negatively for
missing evidence.

## 9. Business-model analysis

_Framework: `frameworks/business-model/framework.md`. Describes value creation/capture only;
no company valuation or revenue forecast._

- `[FACT]` Claude is packaged as **Free → Pro → Max → Team → Enterprise**
  (ev: cl-plans-pricing), with Pro at $17/mo annual ($20 monthly) (ev: cl-pro-price), Max
  from $100 and Team from $20/seat (ev: cl-max-team-plans), and Enterprise as **seat price +
  usage at API rates** (ev: cl-enterprise-usage-pricing). Prices read in USD.
- `[FACT]` Memory is **portable across providers** (import/export) (ev: cl-memory-import-export)
  — a feature that *lowers* switching costs rather than raising them.
- `[INFERENCE]` Capture escalates from flat subscription (Pro) to usage-scaled seats
  (Max/Team/Enterprise), i.e. **more usage-based capture at higher tiers**
  (ev: cl-max-team-plans, cl-enterprise-usage-pricing). Confidence: Moderate.
- `[INFERENCE]` Offering portable memory is a **notable anti-lock-in stance**: it reduces a
  switching cost most competitors leave in place (ev: cl-memory-import-export). Confidence:
  Moderate. (No advertising was observed on the pages read; we make **no claim** that ads are
  absent, only that none were evidenced — see gaps.)
- `[HYPOTHESIS]` Competing on portability and opt-in privacy may be a deliberate
  differentiation against opt-out, higher-lock-in competitors — plausible, unquantified,
  Speculative.

**Evidence gaps (business model):** revenue, margins, distribution, and whether any
advertising exists are **not** evidenced (absence of observed ads is not evidence of absence).
Region-localised pricing beyond USD was not checked. Prices are time-sensitive.

## 10. Workflow-change analysis

_Framework: `frameworks/workflow-change/framework.md`. Net workflow effect is `[UNTESTED]`; no
superficial evidence was manufactured — existing records are cited._

- `[FACT]` The product offers features aimed at **restructuring how work is organised and
  produced** — Projects (persistent, topic-scoped context) (ev: cl-projects,
  cl-memory-projects-separate), Artifacts (shareable outputs) (ev: cl-artifacts), and tool
  integrations (ev: cl-agent-integrations). Confidence: High that these are offered.
- `[INFERENCE]` If they work as documented, Claude shifts knowledge work toward
  **container-based, resumable projects** and **externalised artifacts**, moving the human
  from author toward director/reviewer (ev: cl-projects, cl-artifacts). Confidence: Low —
  inferred from feature descriptions, not observed task completion.
- `[INFERENCE]` Per-project memory (ev: cl-memory-projects-separate) implies **less
  cross-context repetition** within a project but a **new setup step** (creating/curating
  projects). Confidence: Low.
- `[HYPOTHESIS]` Artifacts may reduce copy-paste-and-format steps for buildable outputs while
  adding a review/iterate loop on the artifact — net effect task-dependent; untested (route:
  interaction protocol §3).

**Evidence gaps (workflow change):** tasks compressed, steps removed vs added, human decision
points, coordination changes and new failure modes require running representative tasks end to
end (protocol §3–§10). The dimension is `Not rated` pending interaction.

## 11. Cross-dimensional findings

- **Memory ↔ business model.** Portable, per-project memory (ev: cl-memory-import-export,
  cl-memory-projects-separate) is simultaneously a memory-control feature and an anti-lock-in
  business choice — a clean example of a seam finding. Confidence: Moderate.
- **Trust ↔ business model.** Opt-in training (ev: cl-training-optin) is both a trust posture
  and a differentiator; it plausibly trades some training data for user trust. Stated as an
  inference. Confidence: Low.
- **Model vs product discipline.** No claims are made about the underlying model's capability;
  only documented product features are assessed.

## 12. Scoring record

See `scores.yaml` (validated). Ordinal, per-sub-area, **no overall product score**.
Interaction-dependent sub-areas are `Not rated` / `Speculative`.

## 13. Evidence gaps

| Question | Why unanswerable now | How to close |
| -------- | -------------------- | ------------ |
| Do memory import/export, view/edit behave as documented? | No authenticated session; import is "experimental" | Interaction protocol §7 |
| First-use orientation, Artifact/output rendering, error states | No chat session | Protocol §1, §2 |
| Agent planning, clarification, failure recovery, cancellation | Behavioural; untested | Protocol §3–§5, §9, §10 |
| Does web search cite sources accurately in answers? | Behavioural; untested | Protocol §6, §8 |
| Any advertising present? | Not evidenced either way | Direct product use across tiers |
| Non-USD / regional pricing | Read USD only | Access from multiple regions |

## 14. Limitations and conflict/bias note

**General limitations.** Documentation-first; most claims are `vendor-self-reported` and
unobserved. No authenticated/paid interaction. Pricing read in USD only. No version string;
findings dated 2026-07-13 and expiry-sensitive.

**Material conflict/bias disclosure (required).** This pilot was executed **within a Claude
Code environment** — i.e. the research tooling used to produce the whole library runs on a
product made by the same company (Anthropic) that makes Claude, the subject of this teardown.
This is a genuine potential source of bias and is disclosed transparently. Mitigations applied:

- Claude was held to the **identical** documentation-first method, evidence rules, and
  scoring discipline as ChatGPT and Perplexity; no dimension was scored on more favourable
  terms.
- Every Claude claim cites an official Claude/Anthropic source with a faithful quotation and
  access date, exactly as for the other products.
- Interaction-dependent claims are marked `[UNTESTED]` for Claude just as for the others; no
  behavioural advantage was inferred without evidence.
- The comparison (commits 36–43) makes **no global ranking** and explicitly avoids declaring
  Claude (or any product) a "winner".

A reader who suspects residual bias should re-run this teardown against the cited sources and
file a dispute via `docs/governance/corrections-and-disputes.md`. Per repository rules, this
disclosure lives in the research content and is deliberately **not** placed in Git metadata.

## 15. Reproduction instructions

1. Retrieve the six sources in `source-inventory.md` (claude.com / support.claude.com /
   privacy.claude.com were directly fetchable). Note `anthropic.com/pricing` redirects to
   `claude.com/pricing`.
2. Compare each quotation in `evidence/claude/*.yaml` against the live page on your access
   date; record drift.
3. To close §13 gaps, run the relevant interaction-protocol categories on an authenticated
   account, recording plan, region, date and prompts; add `observation`-type records.
4. Re-run `pi-validate`.

## 16. Update triggers

Re-review when: the memory system, incognito, or import/export changes; the training default
(opt-in) or retention windows change; pricing/tiers change; advertising is introduced; or the
review-by date (2026-10-13) is reached.

## 17. Facts, observations, inferences and hypotheses

Each dimension section separates these explicitly using the `[FACT]` / `[OBS]` /
`[INFERENCE]` / `[HYPOTHESIS]` labels.
