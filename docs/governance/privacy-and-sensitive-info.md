# Privacy and Sensitive-Information Handling

Studying AI-first products often means interacting with systems that ingest input and, at
times, surfacing content that touches real people. This policy defines how contributors
handle personal and sensitive information so that research never comes at the cost of
someone's privacy or safety.

## What counts as sensitive information

- **Personal data**: names, contact details, identifiers, or anything that could identify a
  living individual, whether about a contributor, a third party, or a user of a product.
- **Credentials and secrets**: passwords, API keys, tokens, or access details of any kind.
- **Confidential material**: non-public documents, internal communications, or anything
  obtained under confidentiality.
- **Special-category data**: health, financial, biometric, or other data whose exposure
  carries heightened risk.

## Core rules

1. **Minimise.** Do not collect or record personal or sensitive data unless it is genuinely
   necessary for a specific, defensible research purpose. Default to not collecting it.
2. **Do not publish personal data.** Evidence records and teardowns must not contain
   third-party personal data. Redact or aggregate before recording.
3. **Never commit secrets.** No credentials, tokens or keys in the repository, ever. If one
   is committed, treat it as a security incident (see [SECURITY.md](../../SECURITY.md)).
4. **Use synthetic data for examples.** Illustrative inputs and outputs use clearly labelled
   synthetic data, never real personal information.
5. **Do not use private or confidential material as evidence** (see
   [source types](../methodology/source-types.md)).

## Handling product outputs that contain personal data

When a product, during observation, produces content that includes real personal data:

- Do **not** record the raw output verbatim if it exposes an identifiable person.
- Describe the *behaviour* ("the agent surfaced a third party's contact details") without
  reproducing the sensitive content itself.
- If the behaviour is itself the finding (for example, a privacy failure), report it
  responsibly: enough to substantiate the claim, redacted so it does not further expose the
  individual, and never in a form that functions as a lookup for others.

## Researcher's own data

- Prefer dedicated research accounts over personal accounts when studying a product.
- Assume anything entered into a third-party product may be retained or used by that product;
  do not enter sensitive personal information as part of research.
- Record the account context in the [unit of analysis](../methodology/unit-of-analysis.md)
  without exposing the account's real credentials or identity.

## If sensitive information reaches the repository

1. Treat it as an incident and follow the private reporting path in
   [SECURITY.md](../../SECURITY.md); do not discuss specifics in a public issue.
2. Maintainers remove the material and, where necessary, scrub it from history.
3. If a data breach affecting a third party is involved, act to limit harm first.

## Principle

Curiosity is not a licence to expose people. The library studies *products*, not the private
information of the individuals who happen to appear in their inputs or outputs. When research
value and someone's privacy conflict, privacy wins.
