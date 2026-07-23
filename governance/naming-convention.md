# Lighthouse Technology Naming Convention

## Purpose

This convention creates stable, traceable identifiers across evidence, assets, identities, findings, detections, and remediations.

## Identifier Patterns

| Record type            | Pattern               | Example               |
| ---------------------- | --------------------- | --------------------- |
| Active Directory asset | `LHT-AD-Asset-###`    | `LHT-AD-Asset-001`    |
| Identity               | `LHT-Identity-###`    | `LHT-Identity-014`    |
| Finding                | `LHT-Finding-###`     | `LHT-Finding-007`     |
| Detection              | `LHT-Detection-###`   | `LHT-Detection-012`   |
| Remediation            | `LHT-Remediation-###` | `LHT-Remediation-005` |
| Evidence               | `LHT-Evidence-###`    | `LHT-Evidence-031`    |
| Validation             | `LHT-Validation-###`  | `LHT-Validation-008`  |
| Report                 | `LHT-Report-###`      | `LHT-Report-003`      |

## File Naming Standard

Use lowercase, hyphen-separated filenames:

```text
YYYY-MM-DD_lht-evidence-###_short-description.ext
```

Example:

```text
2026-07-10_lht-evidence-031_domain-controller-gpo-report.html
```

## Naming Rules

* Use sequential identifiers; do not reuse retired identifiers.
* Keep identifiers stable after a finding is remediated.
* Do not include credentials, hashes, tickets, sensitive usernames, or secrets in filenames.
* Use descriptive names that identify the artifact without exposing sensitive data.
* Record the identifier in the evidence manifest and linked registers.
* Use UTC timestamps where timestamps are included in filenames.

## Documentation Headings

Use the full identifier in the first heading of a record where applicable:

```text
# LHT-Finding-007 — Excessive Directory Replication Rights
```
