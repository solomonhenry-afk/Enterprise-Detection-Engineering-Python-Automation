# Target Architecture

## Assessment Architecture

```text
Active Directory, DNS, GPO, LDAP, SMB, Kerberos, Windows endpoints
                              |
                              v
Collection and audit layer
ADRecon, PowerShell AD modules, GPO reports, PingCastle, Purple Knight,
BloodHound Community Edition or approved equivalent, Windows Event Logs, Sysmon
                              |
                              v
Evidence normalization layer
Raw exports, normalized CSV and JSON, metadata, hashes, manifests, screenshots
                              |
                              v
Analysis and risk-engineering layer
Asset inventory, Tier Zero model, privilege exposure, attack paths,
findings register, risk scoring, remediation mapping
                              |
                              v
Detection and Purple Team layer
Splunk searches, Sigma rules, event validation, ATT&CK mapping,
controlled validation matrix, detection outcomes, retests
                              |
                              v
Executive and governance layer
Technical report, executive summary, remediation roadmap, presentation,
evidence manifest, data-quality report, residual-risk narrative
```

## Core Data Flows

1. Approved tools collect configuration, identity, and telemetry evidence.
2. Raw outputs are preserved in `evidence/raw/`.
3. Normalized outputs are stored in `evidence/normalized/` and `data/`.
4. Findings reference stable Lighthouse Technology identifiers.
5. Detection validation links telemetry to attack-path and remediation records.
6. Reports consume approved, traceable evidence only.

## Tier Zero Working Definition

Tier Zero includes domain controllers, directory replication rights, privileged administrative accounts, privileged access workstations where available, identity-management infrastructure, and systems capable of controlling or materially altering Active Directory security.
