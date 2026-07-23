# Lighthouse Technology

# Enterprise Security Evolution

## Domain 5 — Enterprise Active Directory Penetration Testing & Security Auditing

# Authentication Collection Runbook

| Document Information | |
|----------------------|------------------------------------------------|
| Document ID | LHT-RUN-002 |
| Version | 1.0 |
| Status | Approved |
| Classification | Internal |
| Project | Enterprise Security Evolution |
| Domain | Domain 5 |
| Owner | Lighthouse Technology |
| Last Updated | 2026-07-13 |
| Related Documents | LHT-PLAN-003 Credential Security Assessment Plan, LHT-PLAN-004 Authentication Security Assessment Plan, LHT-PLAN-005 Delegation Security Assessment Plan, LHT-STD-002 Service Account Assessment Standard, LHT-STD-003 Kerberos Security Standard, LHT-STD-004 NTLM Exposure Assessment Standard, LHT-STD-005 Password Policy Assessment Standard |

---

# 1. Purpose

This runbook defines the operational procedure for collecting authentication security evidence from the authorized Lighthouse Technology Enterprise Active Directory laboratory.

The purpose of this runbook is to ensure authentication-related evidence is collected in a repeatable, controlled, and auditable manner.

The collection process supports assessment of:

- Credential security
- Authentication configuration
- Kerberos security
- NTLM exposure
- Password policy governance
- Service account security
- Delegation configuration
- Authentication telemetry

This document defines collection procedures only. It does not contain assessment findings.

---

# 2. Objectives

The authentication collection process aims to:

- Establish repeatable evidence collection procedures.
- Maintain evidence lifecycle integrity.
- Preserve source attribution.
- Support normalized authentication datasets.
- Enable security analysis.
- Support detection engineering.
- Provide traceable evidence for remediation decisions.

---

# 3. Scope

This runbook applies to authentication-related evidence collection activities.

Collection scope includes:

| Evidence Category | Purpose |
|-------------------|---------|
| Password Policies | Review authentication governance |
| Kerberos Configuration | Assess authentication security |
| NTLM Configuration | Identify legacy authentication dependencies |
| Service Accounts | Evaluate non-human identities |
| Delegation Configuration | Review identity trust relationships |
| Authentication Events | Support telemetry analysis |
| Group Policy Settings | Validate authentication controls |
| Identity Relationships | Support privilege analysis |

---

# 4. Authorization Boundary

All collection activities are limited to the authorized Lighthouse Technology Enterprise Active Directory laboratory.

The collection process excludes:

- Production identity systems
- External organizations
- Unauthorized credential repositories
- Unapproved authentication testing
- Any activity that impacts service availability

All activities must follow the approved Domain 5 Rules of Engagement.

---

# 5. Evidence Lifecycle

Authentication evidence follows the Lighthouse Technology evidence lifecycle.

| Status | Description |
|--------|-------------|
| Proposed | Planned evidence source |
| Collected | Retrieved from authorized environment |
| Validated | Reviewed for accuracy and completeness |
| Simulated | Artificially generated demonstration data |
| Remediated | Evidence collected after corrective action |

No evidence shall be considered validated until reviewed.

---

# 6. Collection Workflow

The authentication evidence workflow follows this sequence:

```text
Authorization Confirmation
          |
          ▼
Identify Assessment Objective
          |
          ▼
Select Evidence Source
          |
          ▼
Collect Authorized Evidence
          |
          ▼
Register Evidence Manifest Entry
          |
          ▼
Preserve Original Artifact
          |
          ▼
Normalize Data
          |
          ▼
Validate Evidence Quality
          |
          ▼
Prepare Assessment Dataset
```

---

# 7. Collection Preparation

Before collection begins, verify:

- Rules of Engagement approval.
- Authorized laboratory access.
- Repository readiness.
- Evidence manifest availability.
- Required templates exist.
- Collection objectives are documented.

---

# 8. Planned Evidence Sources

The following sources may support authentication assessment.

| Source | Purpose | Expected Artifact | Status |
|-------|---------|------------------|--------|
| Active Directory Configuration Data | Identity authentication context | CSV / JSON / XML | Proposed |
| PowerShell Active Directory Module | Directory information | CSV / JSON | Proposed |
| Group Policy Reports | Authentication policies | HTML / XML | Proposed |
| Windows Security Logs | Authentication telemetry | EVTX | Proposed |
| Sysmon Logs | Endpoint visibility | EVTX | Proposed |
| Splunk Reports | Detection validation | Reports / Searches | Proposed |

Evidence status shall remain Proposed until collected.

---

# 9. Authentication Evidence Categories

## Password Policy Evidence

Examples:

- Domain password configuration
- Account lockout configuration
- Fine-grained policy documentation

Purpose:

Validate enterprise password governance.

---

## Kerberos Evidence

Examples:

- Authentication configuration
- Service relationships
- Policy settings
- Authentication telemetry

Purpose:

Evaluate Kerberos security posture.

---

## NTLM Evidence

Examples:

- Configuration settings
- Authentication visibility
- Legacy dependencies

Purpose:

Identify opportunities for authentication modernization.

---

## Service Account Evidence

Examples:

- Service identity inventory
- Ownership information
- Authentication dependencies

Purpose:

Evaluate non-human identity governance.

---

## Delegation Evidence

Examples:

- Delegation configuration records
- Administrative relationships
- Identity dependencies

Purpose:

Assess delegated authentication exposure.

---

# 10. Evidence Registration Requirements

Every collected artifact must include:

- Lighthouse Evidence ID
- Evidence Name
- Evidence Category
- Source System
- Collection Method
- Collection Date
- Collector
- Validation Status
- Lifecycle Status
- Related Assessment Area

Example naming convention:

```
LHT-Evidence-###
```

---

# 11. Data Normalization Requirements

Collected authentication evidence should be normalized into structured datasets where applicable.

Normalization goals:

- Remove duplicate records.
- Standardize identity names.
- Maintain source references.
- Preserve timestamps.
- Maintain relationship context.
- Support analysis workflows.

Normalized outputs shall preserve linkage to original evidence.

---

# 12. Quality Assurance Checks

Before analysis, verify:

- Evidence is readable.
- Metadata is complete.
- Collection source is documented.
- Evidence ID is assigned.
- Duplicate records are reviewed.
- Lifecycle status is accurate.
- Data transformations are documented.

---

# 13. Evidence Storage

Authentication evidence shall follow the repository evidence model.

Example:

```
evidence/
├── proposed/
├── collected/
├── validated/
├── remediated/
└── manifests/
```

Original artifacts shall remain preserved.

Normalized datasets shall be stored separately.

---

# 14. Validation Process

Collected authentication evidence shall be validated by:

- Reviewing source integrity.
- Confirming expected fields exist.
- Verifying relationship accuracy.
- Reviewing collection metadata.
- Confirming assessment relevance.

Validation outcomes shall be documented.

---

# 15. Expected Outputs

Successful execution of this runbook supports:

- Authentication Evidence Repository
- Credential Security Dataset
- Kerberos Assessment Dataset
- NTLM Assessment Dataset
- Service Account Dataset
- Delegation Dataset
- Authentication Findings Register
- Detection Engineering Inputs
- Remediation Planning Inputs

---

# 16. Cross-Domain Integration

## Domain 1 — SOC Operations, Telemetry & Detection Engineering

Authentication evidence provides the foundation for Windows Event analysis, Sysmon visibility, Splunk searches, and detection validation.

## Domain 2 — Enterprise Adversary Validation & Purple Team Operations

Validated authentication datasets establish the baseline for controlled identity-security validation exercises.

## Domain 3 — Network Security & Infrastructure Engineering

Authentication evidence is correlated with Domain Controllers, DNS, LDAP, SMB, WinRM, and enterprise infrastructure dependencies.

## Domain 4 — Governance, Risk & Compliance Intelligence

Evidence collection supports lineage, risk scoring, control validation, remediation tracking, and executive reporting.

---

# 17. Success Criteria

This runbook is successfully implemented when:

- Authentication evidence collection is repeatable.
- Evidence artifacts are traceable.
- Lifecycle status is maintained.
- Data quality checks are completed.
- Authentication datasets support analysis.
- Findings can be mapped back to validated evidence.

---

# Document Approval

| Role | Name | Status |
|------|------|--------|
| Project Owner | Lighthouse Technology | Approved |
| Security Assessor | B. Solomon Henry | Approved |
| Reviewer | Lighthouse Technology Security Team | Approved |

---
