# Citation and Source-Recording Standard

Every claim in the library must be traceable to a recorded source. This standard defines how
sources are recorded so that a reader — or an automated validator — can locate the evidence,
judge its strength, and check whether it still supports the claim. Consistent recording is
what turns a pile of links into a checkable evidence base.

## The principle

**If it is not recorded to this standard, it cannot be cited.** A claim whose source cannot
be located and re-examined is treated as unsupported, regardless of how plausible it is.

## Required fields for every source

Each source is stored as an [evidence record](../../templates/) and must include:

| Field           | Meaning                                                              |
| --------------- | ------------------------------------------------------------------- |
| `id`            | Stable identifier used to cite the record from teardowns.           |
| `type`          | Source type (observation, primary, reporting, research, user report).|
| `evidence_tier` | E-tier from the [evidence hierarchy](evidence-hierarchy.md).        |
| `title`         | Human-readable title or short description.                           |
| `origin`        | Where it came from: URL, publication, or "first-hand observation".  |
| `accessed_date` | ISO date the source was accessed or the observation was made.       |
| `published_date`| ISO date the source was published, if known.                        |
| `archived_ref`  | Dated archive copy or snapshot reference for volatile sources.       |
| `unit_ref`      | For observations, the unit of analysis under which it was made.      |
| `claim_support` | A short statement of exactly what this source does and does not show.|

## Recording rules

1. **One record, one source.** Do not bundle several sources into one record; atomic records
   are easier to cite and correct.
2. **Dates are ISO 8601** (`YYYY-MM-DD`). Every source has at least an `accessed_date`.
3. **Volatile web sources are archived.** Provide `archived_ref` so the evidence survives the
   original moving or changing.
4. **Observations name their unit.** A first-hand observation without a `unit_ref` is not
   reproducible and is not admissible.
5. **State the scope of support.** `claim_support` must say what the source shows *and* its
   limits, so no one over-reads it.

## Citing a source from a teardown

- Teardowns cite by the evidence record `id`, never by pasting a raw URL inline.
- Each cited claim links to exactly the record(s) that support it.
- If a claim needs multiple sources to hold (triangulation), it cites all of them.

## Quotation limits

- Quote sparingly, briefly, and with attribution; never reproduce long passages, and never
  reproduce material we are not licensed to quote.
- Prefer paraphrase-with-citation over quotation, and never reconstruct a source from many
  small quotes.

## Why this rigour

Sources move, disappear, and change. Products change silently. Recording sources to a fixed
standard — with dates and archives — is the difference between analysis that can be checked
years later and analysis a reader has to take on faith. This library takes nothing on faith.
