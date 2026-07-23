# Lighthouse Technology

# Enterprise Security Evolution

## Domain 5 — Enterprise Active Directory Penetration Testing & Security Auditing

# Service Account Assessment Standard

| Document Information | |
|----------------------|------------------------------------------------|
| Document ID | LHT-STD-002 |
| Version | 1.0 |
| Status | Approved |
| Classification | Internal |
| Project | Enterprise Security Evolution |
| Domain | Domain 5 |
| Owner | Lighthouse Technology |
| Last Updated | 2026-07-13 |
| Related Documents | LHT-METH-001, LHT-METH-002, LHT-METH-003, LHT-PLAN-001, LHT-PLAN-002, LHT-PLAN-003, LHT-PLAN-004, LHT-PLAN-005, LHT-STD-001 |

---

# 1. Purpose

This standard establishes the methodology for identifying, classifying, assessing, and governing service accounts within the authorized Lighthouse Technology Enterprise Active Directory laboratory.

Service accounts frequently support critical business services and enterprise infrastructure. Poor governance, excessive privilege, unmanaged credentials, or legacy configurations can significantly increase identity-related risk.

The purpose of this standard is to ensure that service account assessments are performed consistently, are evidence-backed, and support remediation planning without disrupting production-like services in the authorized laboratory.

This document defines assessment standards only. It does not contain assessment findings.

---

# 2. Objectives

The service account assessment aims to:

- Establish a consistent service account classification model.
- Identify enterprise service account types.
- Review credential management practices.
- Evaluate privilege assignments.
- Assess authentication configuration.
- Review ownership and lifecycle management.
- Support privilege exposure analysis.
- Support attack-path analysis.
- Provide evidence-backed remediation recommendations.

---

# 3. Scope

This standard applies to service identities used within the authorized Active Directory laboratory, including:

| Service Identity | Assessment Focus |
|------------------|------------------|
| Traditional Service Accounts | Governance and credential management |
| Group Managed Service Accounts (gMSA) | Deployment and operational usage |
| Managed Service Accounts (MSA) | Configuration review |
| Application Service Accounts | Business application support |
| Scheduled Task Accounts | Authentication and privilege review |
| IIS Application Pool Identities | Configuration and permissions |
| SQL Server Service Accounts | Administrative scope |
| Infrastructure Service Accounts | Enterprise service dependencies |

---

# 4. Authorization Boundary

Assessment activities are restricted to the authorized Lighthouse Technology Enterprise Active Directory laboratory.

The assessment excludes:

- Production environments
- External identity providers
- Third-party infrastructure
- Unauthorized credential stores
- Credential modification outside approved validation activities

All assessment activities shall comply with the Rules of Engagement established during Phase A.

---

# 5. Service Account Classification

Service accounts shall be classified using the following categories.

| Classification | Description |
|----------------|-------------|
| Standard Service Account | Traditional account supporting a service |
| Managed Service Account (MSA) | Managed service identity |
| Group Managed Service Account (gMSA) | Enterprise managed service identity |
| Application Service Account | Supports enterprise applications |
| Infrastructure Service Account | Supports Active Directory or infrastructure services |
| Privileged Service Account | Possesses elevated administrative privileges |
| Tier Zero Service Account | Supports Tier Zero systems or identity infrastructure |

Classification shall be evidence-based and documented.

---

# 6. Assessment Principles

The service account assessment is governed by the following principles.

## Evidence-Driven Assessment

All observations shall be supported by validated evidence.

## Least Privilege

Service accounts shall possess only the permissions necessary for their operational purpose.

## Ownership

Every service account shall have an identified owner or responsible team.

## Credential Governance

Credential lifecycle management shall be reviewed as part of the assessment.

## Operational Stability

Assessment activities shall avoid unnecessary disruption to services within the authorized laboratory.

---

# 7. Assessment Areas

The assessment will evaluate:

| Assessment Area | Objective |
|-----------------|-----------|
| Account Ownership | Verify accountability |
| Business Purpose | Validate operational necessity |
| Privilege Assignment | Assess administrative scope |
| Password Management | Review governance and lifecycle |
| Authentication Configuration | Review supported authentication mechanisms |
| gMSA Adoption | Evaluate managed identity usage |
| Interactive Logon Rights | Identify unnecessary interactive access |
| Service Dependencies | Review operational relationships |
| Tier Zero Association | Identify critical identity dependencies |

---

# 8. Planned Evidence Sources

The following evidence sources may support the assessment.

| Source | Purpose | Expected Output | Initial Status |
|---------|---------|----------------|----------------|
| PowerShell Active Directory Module | Service account inventory | CSV / JSON / XML | Proposed |
| ADRecon | Active Directory configuration | HTML / CSV | Proposed |
| Group Policy Reports | Security policy review | XML / HTML | Proposed |
| Windows Security Event Logs | Authentication activity | EVTX | Proposed |
| Sysmon | Endpoint telemetry | EVTX | Proposed |
| Splunk | Detection correlation | Reports / Searches | Proposed |

Evidence shall remain in the **Proposed** lifecycle state until collected and validated.

---

# 9. Evidence Requirements

Each assessment observation shall reference:

- Lighthouse Evidence ID
- Collection Method
- Source Tool
- Collection Date
- Validation Status
- Related Service Account
- Related System
- Related Finding
- Related Remediation

Assessment conclusions shall not be documented without supporting evidence.

---

# 10. Risk Evaluation Criteria

Service account risk will be evaluated using the Domain 4 enterprise risk methodology.

Assessment factors include:

- Privilege level
- Tier Zero association
- Credential management maturity
- Authentication configuration
- Ownership
- Detection coverage
- Business dependency
- Remediation complexity

Risk ratings shall only be assigned after evidence validation.

---

# 11. Assessment Workflow

The service account assessment shall follow the sequence below.

1. Confirm authorization.
2. Identify service accounts.
3. Classify service identities.
4. Review ownership.
5. Assess privilege assignments.
6. Review authentication configuration.
7. Evaluate credential governance.
8. Assess Tier Zero relationships.
9. Register evidence.
10. Validate findings.
11. Prioritize risk.
12. Recommend remediation.
13. Validate corrective actions.

---

# 12. Expected Deliverables

Execution of this standard supports the production of:

- Service Account Inventory
- Service Account Assessment Report
- Credential Security Assessment
- Privilege Exposure Report
- Attack Path Analysis
- Detection Coverage Matrix
- Enterprise Remediation Roadmap
- Executive Risk Summary

---

# 13. Cross-Domain Integration

## Domain 1 — SOC Operations, Telemetry & Detection Engineering

Service account classifications enrich Windows Security Events, Sysmon telemetry, and Splunk detections by identifying high-value identities requiring enhanced monitoring.

## Domain 2 — Enterprise Adversary Validation & Purple Team Operations

Validated service account inventories provide the baseline for authorized Purple Team validation of identity-focused techniques while maintaining clear authorization boundaries.

## Domain 3 — Network Security & Infrastructure Engineering

Service account assessments are correlated with Domain Controllers, LDAP, SMB, DNS, WinRM, and other infrastructure services to understand operational dependencies.

## Domain 4 — Governance, Risk & Compliance Intelligence

Assessment outputs contribute to evidence lineage, enterprise risk scoring, remediation prioritization, compliance reporting, and executive communication.

---

# 14. Success Criteria

This standard shall be considered successfully implemented when:

- Service accounts have been consistently classified.
- Supporting evidence has been collected and validated.
- Privilege and credential governance have been assessed.
- Findings support attack-path analysis and detection engineering.
- Remediation recommendations are evidence-backed.
- Outputs support enterprise governance and executive reporting.

---

# Document Approval

| Role | Name | Status |
|------|------|--------|
| Project Owner | Lighthouse Technology | Approved |
| Security Assessor | B. Solomon Henry | Approved |
| Reviewer | Lighthouse Technology Security Team | Approved |

---
