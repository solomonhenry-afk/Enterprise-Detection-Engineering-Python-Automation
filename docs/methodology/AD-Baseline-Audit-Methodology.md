# Lighthouse Technology

# Enterprise Security Evolution

## Domain 5 — Enterprise Active Directory Penetration Testing & Security Auditing

# Active Directory Baseline Audit Methodology

| Document Information | |
|----------------------|------------------------------------------------|
| Document ID | LHT-METH-001 |
| Version | 1.0 |
| Status | Approved |
| Classification | Internal |
| Project | Enterprise Security Evolution |
| Domain | Domain 5 |
| Owner | Lighthouse Technology |
| Last Updated | 2016-07-12 |
| Related Documents | Domain 5 Charter, Assessment Plan, Evidence Lifecycle Standard, Risk Scoring Methodology |

---

# 1. Purpose

This document defines the standardized methodology for performing a comprehensive Active Directory baseline security 
assessment within the authorized Lighthouse Technology Enterprise Lab.

The methodology establishes a repeatable, evidence-driven approach for assessing the security posture of 
an enterprise Active Directory environment through structured auditing, identity enumeration, 
privilege exposure analysis, attack-path preparation, evidence normalization, and governance-aligned reporting.

This document defines **how** the assessment is conducted. It does not contain assessment findings or evidence.

---

# 2. Assessment Objectives

The objectives of this methodology are to:

- Establish a trusted security baseline for the Active Directory environment.
- Produce a normalized inventory of identity and infrastructure assets.
- Assess Active Directory configuration and security posture.
- Identify privileged identities and Tier Zero assets.
- Support later attack-path and privilege exposure analysis.
- Enable evidence-backed detection validation.
- Produce repeatable, auditable outputs suitable for governance and executive reporting.

---

# 3. Scope

## In Scope

The following components are included in the assessment:

- Active Directory Forest
- Active Directory Domains
- Domain Controllers
- Organizational Units (OUs)
- Users
- Groups
- Computers
- Service Accounts
- Group Policy Objects (GPOs)
- DNS
- LDAP
- Kerberos
- SMB
- Trust Relationships
- Delegation Configurations
- Administrative Groups
- Tier Zero Assets
- Identity Governance Controls

## Out of Scope

The following are explicitly excluded:

- Production environments
- Third-party Active Directory forests
- External identity providers
- Internet-facing infrastructure
- Cloud identity platforms (unless separately scoped)
- Systems outside the authorized Lighthouse Technology lab

---

# 4. Authorization Boundary

All activities performed under this methodology are restricted to the Lighthouse Technology Enterprise Lab.

The assessment shall only be conducted against systems, identities, and infrastructure that have been explicitly authorized.

This methodology does not authorize testing against production systems or external organizations.

Techniques that could affect credentials, authentication, replication, or directory integrity are treated as controlled validation activities within the lab. The focus of this assessment is on evidence collection, detection validation, and remediation planning rather than uncontrolled offensive operations.

---

# 5. Assessment Principles

The assessment is governed by the following principles:

## Evidence First

Assessment conclusions shall be supported by verifiable evidence.

## Least Assumption

No conclusions shall be drawn without supporting technical evidence.

## Repeatability

Assessment activities shall be repeatable by another assessor using the documented methodology.

## Evidence Integrity

Collected evidence shall retain traceability to its original source.

## Data Normalization

Collected data shall be normalized before analysis to ensure consistency across tools and assessment phases.

## Governance Alignment

Assessment outputs shall support governance, risk management, and executive reporting.

## Risk Prioritization

Findings shall be prioritized based on business impact, likelihood, and privilege exposure.

---

# 6. Assessment Domains

The baseline audit covers the following assessment domains:

| Domain | Description |
|----------|-------------|
| Forest Health | Forest configuration and security posture |
| Domain Configuration | Domain-wide configuration review |
| Domain Controllers | Security posture of domain controllers |
| Organizational Units | OU structure and delegation review |
| DNS | Active Directory-integrated DNS assessment |
| LDAP | LDAP configuration and security review |
| Kerberos | Authentication configuration assessment |
| SMB | SMB configuration review |
| Group Policy | GPO configuration and security review |
| Identity Inventory | User, group, and computer inventory |
| Service Accounts | Service account assessment |
| Trust Relationships | Trust configuration review |
| Delegation | Delegation configuration assessment |
| Tier Zero | Identification and protection review |
| Administrative Exposure | Privileged identity assessment |
| Identity Governance | Governance and lifecycle review |

---

# 7. Planned Evidence Sources

Evidence may be collected from the following authorized sources.

No evidence is considered collected until acquired within the authorized lab.

| Evidence Source | Intended Purpose | Expected Output | Initial Status |
|-----------------|------------------|-----------------|----------------|
| PowerShell Active Directory Module | Identity inventory | CSV / XML / JSON | Proposed |
| PingCastle | Forest and domain posture | HTML / XML | Proposed |
| ADRecon | Configuration assessment | HTML / CSV | Proposed |
| BloodHound Community Edition | Relationship analysis | JSON / ZIP | Proposed |
| Group Policy Reports | GPO review | XML / HTML | Proposed |
| Windows Event Logs | Security events | EVTX | Proposed |
| Sysmon | Endpoint telemetry | EVTX | Proposed |
| Splunk | Detection validation | Saved Searches / Reports | Proposed |

---

# 8. Evidence Lifecycle

All evidence shall follow the Lighthouse Technology evidence lifecycle.

| Status | Description |
|----------|-------------|
| Proposed | Planned but not yet collected |
| Collected | Acquired from an authorized source |
| Validated | Reviewed and confirmed for accuracy |
| Simulated | Artificially generated for demonstration purposes |
| Remediated | Evidence collected following remediation validation |

Evidence shall never be represented as validated unless verification has been completed.

---

# 9. Evidence Quality Requirements

All evidence shall satisfy the following requirements:

- Traceable to its source
- Timestamped
- Assigned a unique Lighthouse evidence identifier
- Preserved without unauthorized modification
- Reproducible where practical
- Clearly identified if simulated
- Referenced within the Evidence Manifest
- Linked to relevant findings and remediation activities

---

# 10. Assessment Workflow

The assessment follows a structured workflow.

1. Confirm authorization.
2. Define assessment scope.
3. Collect baseline evidence.
4. Normalize collected data.
5. Validate evidence integrity.
6. Perform technical analysis.
7. Correlate telemetry.
8. Assess identity risk.
9. Prioritize findings.
10. Develop remediation recommendations.
11. Validate remediation.
12. Produce executive and technical reporting.

---

# 11. Assessment Deliverables

This methodology supports the production of the following deliverables:

- Enterprise Active Directory Security Assessment Report
- Active Directory Security Audit Report
- Identity Inventory
- Privilege Exposure Report
- Attack Path Analysis
- Detection Coverage Matrix
- MITRE ATT&CK Mapping
- Purple Team Validation Report
- Enterprise Remediation Roadmap
- Executive Risk Summary
- Evidence Manifest
- Data Quality Report

---

# 12. Success Criteria

The baseline assessment shall be considered complete when:

- All scoped identity objects have been inventoried.
- All evidence has been assigned Lighthouse identifiers.
- Evidence has been normalized.
- Technical findings are traceable to supporting evidence.
- Risk ratings have been assigned.
- Detection opportunities have been identified.
- Remediation recommendations have been documented.
- Executive reporting can be produced from validated evidence.

---

# 13. Cross-Domain Integration

This methodology consumes outputs from previous Enterprise Security Evolution domains.

## Domain 1 — SOC Operations, Telemetry & Detection Engineering

Provides:

- Windows Event Logs
- Sysmon telemetry
- Splunk visibility
- Detection logic
- Security monitoring context

## Domain 2 — Enterprise Adversary Validation & Purple Team Operations

Provides:

- Controlled adversary validation
- MITRE ATT&CK mapping
- Detection testing methodology
- Purple Team validation framework

## Domain 3 — Network Security & Infrastructure Engineering

Provides:

- Network segmentation
- SMB exposure context
- LDAP exposure context
- DNS architecture
- Infrastructure security posture

## Domain 4 — Governance, Risk & Compliance Intelligence

Provides:

- Risk scoring methodology
- Governance controls
- Evidence lineage
- Remediation tracking
- Executive reporting standards

---

# 14. Roles and Responsibilities

| Role | Responsibility |
|------|----------------|
| Security Assessor | Conduct assessment activities within scope |
| Detection Engineer | Validate telemetry and detection coverage |
| Infrastructure Administrator | Support authorized data collection |
| Governance Analyst | Maintain evidence quality and traceability |
| Executive Stakeholder | Review strategic findings and remediation priorities |

---

# 15. Methodology Governance

This methodology serves as the authoritative assessment standard for Domain 5.

All assessment activities, templates, datasets, reports, dashboards, and executive deliverables shall align with this methodology.

Changes to this document shall be version controlled and reviewed prior to implementation.

---

# Document Approval

| Role | Name | Status |
|------|------|--------|
| Project Owner | Lighthouse Technology | Approved |
| Security Assessor | __________________ | B. Solomon Henry |
| Reviewer | __________________ | Lighthouse Technology Security Team |

---

**End of Document**
