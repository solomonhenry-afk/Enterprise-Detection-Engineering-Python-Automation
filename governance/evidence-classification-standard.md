# Evidence Classification Standard

## Purpose

This standard defines how Domain 5 evidence is handled, stored, redacted, and reported.

## Classification Levels

| Classification | Description                                                                        | Repository handling                                   |
| -------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------- |
| Public         | Safe for portfolio publication                                                     | May be committed after review                         |
| Internal       | Non-sensitive project material                                                     | May be committed if approved                          |
| Confidential   | Lab configuration, hostnames, internal architecture, detailed findings             | Store locally or redact before publication            |
| Restricted     | Credentials, hashes, tickets, secrets, sensitive logs, personally identifying data | Never commit; minimize collection and securely handle |

## Restricted Data Examples

* Passwords and password equivalents
* NTLM hashes
* Kerberos tickets
* Private keys and certificates
* API keys and tokens
* Full sensitive event logs
* Unredacted account identifiers where unnecessary
* Tool outputs containing credential material

## Handling Requirements

* Classify evidence before publication.
* Store raw sensitive evidence outside public source control where required.
* Create sanitized derivatives for reports and portfolio use.
* Redact secrets and unnecessary identifiers from screenshots.
* Do not place restricted data in issue trackers, commit messages, Markdown files, or presentation slides.
* Document redaction and transformation in the evidence manifest.

## Publication Review

Before committing an artifact, verify:

1. It contains no restricted data.
2. Hostnames, domains, IP addresses, usernames, and paths are appropriate for publication.
3. The evidence state is accurate.
4. The artifact supports a legitimate project claim.
5. Any redaction preserves the technical meaning of the evidence.
