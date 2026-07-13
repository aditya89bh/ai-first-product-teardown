# Cross-Product Memory Comparison

> **No global ranking.** Compares documented memory models by memory *type*, per the task's
> required distinctions. Efficacy is `[UNTESTED]` for all three. Scope: consumer web surface,
> documentation-first, 2026-07-13.

## Memory types framework (used for this comparison)

Per the required distinctions: (a) conversation context, (b) saved user information,
(c) project/workspace context, (d) retrieval from uploaded material, (e) cross-session
continuity, (f) user-controlled memory.

## Type-by-type comparison

### (a) Conversation context (within a session)
All three maintain within-conversation context (documented or inherent). Perplexity documents
that Pro Search "maintains context from previous interactions" (ev: px-ux-refinement). Not a
differentiator.

### (b) Saved user information (explicit)
- **ChatGPT:** explicit **Custom Instructions** separate from inferred memory
  (ev: cg-memory-vs-custom-instructions, cg-custom-instructions).
- **Claude:** memory summary is viewable/editable; explicit vs inferred not as sharply split
  in the docs read (ev: cl-ux-memory-settings-location).
- **Perplexity:** not documented on pages read (gap).

### (c) Project / workspace context
- **Claude:** **per-Project separate memory spaces** — the strongest documented scoping
  (ev: cl-memory-projects-separate).
- **ChatGPT:** Projects offered (ev: cg-agent-tooling-offered) but per-project memory isolation
  not detailed in the docs read (partial).
- **Perplexity:** Brain builds a working model of "projects, people, and files", Max-gated and
  in preview (ev: px-brain-memory).

### (d) Retrieval from uploaded material
All three document file uploads/analysis (ev: cg-plus-features, cl-identity-capabilities,
px-free-plan-limits), but retrieval behaviour is untested for all.

### (e) Cross-session continuity
- **ChatGPT:** automatic memory across chats/files/connected apps (ev: cg-memory-how-it-works),
  **plan/region-gated in rollout** (ev: cg-memory-rollout-region).
- **Claude:** automatic synthesis across chat history (ev: cl-memory-how-it-works),
  available on all plans (ev: cl-chat-search-paid).
- **Perplexity:** base-product continuity beyond "search history" not documented; Brain
  (Max/preview) is the continuity mechanism (ev: px-brain-memory, px-free-plan-limits).

### (f) User-controlled memory
- **ChatGPT:** view/edit summary; **suppression ≠ deletion**, full deletion spans many surfaces
  (ev: cg-memory-summary-edit, cg-memory-delete).
- **Claude:** view/edit; **incognito**; and uniquely **import/export across providers**
  (experimental) (ev: cl-ux-memory-settings-location, cl-incognito, cl-memory-import-export,
  cl-memory-import-experimental).
- **Perplexity:** Brain controls (view/edit/delete) not documented on pages read (gap).

## Headline contrasts

- **Scoping:** Claude documents the cleanest **per-project isolation** (ev: cl-memory-projects-separate).
- **Portability:** Claude uniquely documents **cross-provider import/export**, lowering switching
  cost (ev: cl-memory-import-export) — a memory feature with a business-model consequence.
- **Deletion honesty:** ChatGPT is explicit that suppression is not deletion
  (ev: cg-memory-delete) — candid, but implies a real deletion burden.
- **Positioning:** Perplexity treats rich memory as a **premium/preview** capability
  (ev: px-brain-memory), consistent with an answer-engine thesis.

## What cannot be concluded (memory)

- Whether any control (edit/delete/import) actually works — untested for all three.
- Perplexity's memory model cannot be fairly scored on user controls (documentation gap) —
  marked `Not rated`, not scored negatively.
- No cross-plan/region generalisation (ChatGPT memory is mid-rollout).
