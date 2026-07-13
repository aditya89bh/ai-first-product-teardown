# Source Inventory: ChatGPT

- **Product slug:** chatgpt
- **Research window:** 2026-07-13 to 2026-07-13
- **Compiled by:** phase-2-pilot

All URLs below were actually retrieved during the research window. `help.openai.com`,
`chatgpt.com` and `openai.com` return HTTP 403 to direct fetch; those pages were read through
the in-app browser. Quotations recorded in the evidence records are faithful to the pages as
read on the access date.

## Official / first-party sources

| # | Title | URL | Type | Ownership | Directness | Accessed |
| - | ----- | --- | ---- | --------- | ---------- | -------- |
| 1 | What is ChatGPT Plus? | https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus | help-centre | first-party | vendor-self-reported | 2026-07-13 |
| 2 | Memory FAQ | https://help.openai.com/en/articles/8590148-memory-faq | help-centre | first-party | vendor-self-reported | 2026-07-13 |
| 3 | Data Controls FAQ | https://help.openai.com/en/articles/7730893-data-controls-faq | help-centre | first-party | vendor-self-reported | 2026-07-13 |
| 4 | ChatGPT Custom Instructions | https://help.openai.com/en/articles/8096356-chatgpt-custom-instructions | help-centre | first-party | vendor-self-reported | 2026-07-13 |
| 5 | ChatGPT Plans (pricing) | https://chatgpt.com/pricing | pricing | first-party | vendor-self-reported | 2026-07-13 |

## Independent / third-party sources

None used as primary evidence for ChatGPT. Web search was used only to locate the official
pages above; search-result snippets are not cited as evidence.

## Access constraints encountered

| Source attempted | URL | Barrier | Effect on research |
| ---------------- | --- | ------- | ------------------ |
| OpenAI / ChatGPT / Help direct fetch | openai.com, chatgpt.com, help.openai.com | HTTP 403 to WebFetch | Read via in-app browser instead; recorded with access date |
| Authenticated app behaviour | chatgpt.com (signed-in) | No authenticated session used | Interaction-dependent claims marked `[UNTESTED]` |
| Pricing currency/region | chatgpt.com/pricing | Page rendered in INR (₹) for the research region | US prices taken from help article; region divergence recorded as a finding |

## Region and version notes

- The pricing page rendered prices in **INR** during the research window, implying a
  region-localised page; the "What is ChatGPT Plus?" help article states **$20/month (US)**.
  Prices are therefore **region-dependent** and recorded per source, not merged.
- OpenAI states model availability "change[s] over time"; there is no stable product version
  string, so all findings are dated to 2026-07-13.

## Source-to-evidence map

| Source # | Evidence record id(s) |
| -------- | --------------------- |
| 1 | cg-plus-identity-price, cg-plus-features |
| 2 | cg-memory-how-it-works, cg-memory-summary-edit, cg-memory-delete, cg-memory-rollout-region, cg-memory-sources, cg-temporary-chats-memory |
| 3 | cg-data-training-optout, cg-temporary-chats-retention, cg-ads-controls, cg-safety-context, cg-business-data-controls |
| 4 | cg-custom-instructions, cg-custom-instructions-limit |
| 5 | cg-plans-overview, cg-pricing-region-inr, cg-ads-go-plan, cg-training-optout-pricing, cg-models-offered |
