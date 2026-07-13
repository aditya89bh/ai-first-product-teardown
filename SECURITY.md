# Security and Responsible Disclosure Policy

This repository is primarily a research library, but it ships validation tooling (a Python
package and CI workflows) and handles third-party information. This policy covers both the
software and the research-integrity surface.

## Scope

In scope:

- Vulnerabilities in the `product_intelligence` Python package or its dependencies as
  pinned here.
- Vulnerabilities in the GitHub Actions workflows (for example, injection or privilege
  escalation via untrusted input).
- Exposure of sensitive information within the repository (secrets, personal data, or
  confidential third-party material that should not be present).

Out of scope:

- Vulnerabilities in the third-party products that this library analyses. Report those to
  the relevant vendor, not here.
- Findings that require access we do not grant, or that depend on already-compromised
  contributor machines.

## Reporting a vulnerability

Please report privately and give us a chance to fix the issue before public disclosure.

1. **Preferred:** open a GitHub private security advisory ("Report a vulnerability") on this
   repository. This keeps details confidential until a fix is ready.
2. If private advisories are unavailable to you, open a minimal public issue that says a
   security report exists and requests a private channel — **do not include exploit details
   in a public issue.**

In your report, please include: affected file or workflow, a description of the impact, and
reproduction steps or a proof of concept where practical.

## What to expect

- **Acknowledgement:** we aim to acknowledge a valid report within 5 working days.
- **Assessment:** we will confirm the issue, determine severity, and agree a remediation
  timeline with you.
- **Disclosure:** we prefer coordinated disclosure once a fix is available, and will credit
  reporters who wish to be named.

## Handling sensitive information in research

If you discover that the repository contains material that should not be public — leaked
credentials, personal data, or confidential third-party documents — treat it as a security
issue and report it privately using the process above. Do not open a public issue that
further exposes the material. Removal and history-scrubbing will be handled by maintainers
under the governance policy.

## Dependencies and supply chain

- Dependencies are pinned in [`pyproject.toml`](pyproject.toml).
- CI runs on pinned actions where practical and treats all external input as untrusted.
- We do not execute untrusted code from analysed products as part of research.
