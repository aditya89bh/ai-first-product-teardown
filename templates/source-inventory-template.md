<!--
CANONICAL SOURCE-INVENTORY TEMPLATE
Copy to library/products/<product-slug>/source-inventory.md and fill for that product.
List every source consulted, official-first. Each row must be a real source actually
retrieved during the research window. Do not list a source you did not open.
Ownership: "first-party" = the product maker's own domain; "third-party" = independent.
Directness: how the source functions as evidence:
  vendor-self-reported | direct-observation | independent-reporting
-->

# Source Inventory: <Product Name>

- **Product slug:** <slug>
- **Research window:** <YYYY-MM-DD> to <YYYY-MM-DD>
- **Compiled by:** <handle>

## Official / first-party sources

| # | Title | URL | Type | Ownership | Directness | Accessed | Notes |
| - | ----- | --- | ---- | --------- | ---------- | -------- | ----- |
| 1 | e.g. Help Center: What is X | https://… | help-centre | first-party | vendor-self-reported | YYYY-MM-DD | |

## Independent / third-party sources (used only for corroboration/context)

| # | Title | URL | Type | Ownership | Directness | Accessed | Notes |
| - | ----- | --- | ---- | --------- | ---------- | -------- | ----- |
| | | | reporting | third-party | independent-reporting | | |

## Access constraints encountered

Record any pages that could not be accessed (403, login-walled, region-gated, paywalled) and
how that limits the research. These become evidence gaps, not guesses.

| Source attempted | URL | Barrier | Effect on research |
| ---------------- | --- | ------- | ------------------ |
| | | e.g. HTTP 403 to direct fetch | Read via in-app browser instead / marked untested |

## Source-to-evidence map

For traceability, list which evidence records (`evidence/<product>/*.yaml`) derive from which
sources above.

| Source # | Evidence record id(s) |
| -------- | --------------------- |
| 1 | <record-id> |
