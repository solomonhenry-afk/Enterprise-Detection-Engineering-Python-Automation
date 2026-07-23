# Lighthouse Technology

# Enterprise Security Evolution

## Domain 5 — Enterprise Active Directory Penetration Testing & Security Auditing

# Evidence Normalization Workflow

| Document Information | |
|----------------------|------------------------------------------------|
| Document ID | LHT-METH-003 |
| Version | 1.0 |
| Status | Approved |
| Classification | Internal |
| Project | Enterprise Security Evolution |
| Domain | Domain 5 |
| Owner | Lighthouse Technology |
| Last Updated | 2026-07-12 |
| Related Documents | LHT-METH-001 Active Directory Baseline Audit Methodology, LHT-METH-002 Identity Inventory Methodology, Evidence Lifecycle Standard, Assessment Plan |

---

# 1. Purpose

This document defines the standardized workflow for collecting, registering, normalizing, validating, storing, and governing assessment evidence generated throughout Domain 5.

The workflow ensures that all evidence used to support technical findings, attack-path analysis, detection validation, remediation engineering, and executive reporting is:

- Traceable
- Consistent
- Verifiable
- Reproducible where practical
- Governed throughout its lifecycle

This document governs the handling of evidence. It does not contain assessment findings or collected evidence.

---

# 2. Objectives

The objectives of the evidence normalization workflow are to:

- Standardize evidence collected from multiple tools and sources.
- Preserve evidence integrity and provenance.
- Enable reliable correlation across technical and governance activities.
- Support repeatable assessments.
- Improve data quality for reporting and analytics.
- Ensure all findings are backed by verifiable evidence.

---

# 3. Scope

This workflow applies to all evidence collected within the authorized Lighthouse Technology Enterprise Lab for Domain 5.

Examples include:

- Active Directory inventories
- Forest and domain configuration data
- Group Policy reports
- PowerShell exports
- ADRecon outputs
- PingCastle assessments
- BloodHound Community Edition exports
- Windows Event Logs
- Sysmon logs
- Splunk search results
- Configuration snapshots
- Screenshots
- Technical notes
- Validation records

---

# 4. Authorization Boundary

Evidence shall only be collected from assets and identities explicitly authorized within the Lighthouse Technology Enterprise Lab.

No evidence shall be collected from:

- Production environments
- External organizations
- Third-party forests
- Cloud tenants outside scope
- Unauthorized systems

All evidence collection activities shall comply with the Rules of Engagement established in Phase A.

---

# 5. Evidence Lifecycle

All evidence shall progress through the following lifecycle.

| Status | Description |
|----------|-------------|
| Proposed | Planned for collection but not yet acquired |
| Collected | Acquired from an authorized source |
| Validated | Reviewed and confirmed for accuracy and completeness |
| Simulated | Artificially generated for demonstration purposes and clearly labeled |
| Remediated | Collected after corrective actions to verify remediation effectiveness |

Evidence shall not advance to the next lifecycle stage until the required validation criteria have been met.

---

# 6. Evidence Categories

Evidence shall be classified according to its purpose.

| Category | Examples |
|----------|----------|
| Identity | Users, Groups, Computers, Service Accounts |
| Configuration | DNS, LDAP, Kerberos, SMB, GPOs |
| Privilege | Administrative groups, ACLs, Delegation |
| Telemetry | Windows Event Logs, Sysmon, Splunk |
| Attack Path | Relationship graphs, privilege paths |
| Detection | Detection logic, Sigma rules, Splunk searches |
| Governance | Risk registers, remediation plans, executive summaries |
| Validation | Test results, screenshots, retest evidence |

---

# 7. Evidence Registration

Every evidence item shall receive a unique Lighthouse Technology identifier.

Example format:

- LHT-Evidence-001
- LHT-Evidence-002
- LHT-Evidence-003

Each registered item shall include:

- Evidence ID
- Evidence Name
- Source
- Collection Method
- Collection Date
- Collector
- Status
- Validation Status
- Related Finding(s)
- Related Asset(s)
- Related Identity(ies)

---

# 8. Evidence Sources

Evidence may originate from the following planned sources.

| Source | Expected Output | Initial Status |
|---------|-----------------|----------------|
| PowerShell Active Directory Module | CSV / JSON / XML | Proposed |
| ADRecon | HTML / CSV | Proposed |
| PingCastle | HTML / XML | Proposed |
| BloodHound Community Edition | JSON / ZIP | Proposed |
| Group Policy Reports | XML / HTML | Proposed |
| Windows Event Logs | EVTX | Proposed |
| Sysmon | EVTX | Proposed |
| Splunk | Saved Searches / Reports | Proposed |
| Manual Observation | Markdown Notes | Proposed |

No source shall be treated as collected evidence until acquired within the authorized lab.

---

# 9. Evidence Normalization Standards

Raw evidence shall be transformed into standardized formats to support analysis and reporting.

Normalization activities include:

- Standardized naming conventions
- Consistent date and time formatting
- Unified attribute names
- Removal of duplicate records
- Metadata enrichment
- Source attribution
- Evidence ID assignment
- Relationship mapping
- Validation status assignment

Normalization shall preserve the original evidence without modification.

---

# 10. Data Quality Requirements

Normalized evidence shall satisfy the following quality requirements.

- Accurate
- Complete
- Consistent
- Traceable
- Timestamped
- Source-attributed
- Version controlled
- Free from unauthorized modification

Any limitations or assumptions identified during normalization shall be documented.

---

# 11. Evidence Validation

Evidence shall be reviewed before being used in technical analysis or reporting.

Validation activities include:

- Source verification
- File integrity review
- Metadata verification
- Duplicate detection
- Format validation
- Relationship verification
- Evidence lifecycle review

Evidence failing validation shall be flagged and excluded from formal findings until resolved.

---

# 12. Evidence Storage

Evidence shall be organized according to the repository structure.

```text
evidence/
├── proposed/
├── collected/
├── normalized/
├── validated/
├── remediated/
└── manifests/
```

Original evidence shall be preserved separately from normalized datasets and derived analysis.

---

# 13. Evidence Traceability

Every technical finding shall reference supporting evidence.

Traceability shall include:

- Lighthouse Evidence ID
- Source Tool
- Collection Date
- Validation Status
- Related Asset
- Related Identity
- Related Finding
- Related Remediation

No finding shall exist without traceable supporting evidence.

---

# 14. Evidence Workflow

The standard evidence workflow consists of the following stages.

1. Confirm authorization.
2. Identify required evidence.
3. Collect evidence.
4. Register evidence.
5. Preserve original artifacts.
6. Normalize collected data.
7. Validate evidence quality.
8. Correlate related datasets.
9. Support technical analysis.
10. Produce findings.
11. Validate remediation.
12. Archive evidence.

---

# 15. Deliverables Supported

This workflow supports the production of:

- Evidence Manifest
- Data Quality Report
- Active Directory Security Assessment Report
- Identity Inventory
- Attack Path Analysis
- Privilege Exposure Report
- Detection Coverage Matrix
- Purple Team Validation Report
- Enterprise Remediation Roadmap
- Executive Risk Summary

---

# 16. Cross-Domain Integration

## Domain 1 — SOC Operations, Telemetry & Detection Engineering

Telemetry collected through Windows Event Logs, Sysmon, and Splunk is normalized and correlated with identity and infrastructure evidence to validate detection coverage.

## Domain 2 — Enterprise Adversary Validation & Purple Team Operations

Controlled validation activities generate evidence that follows the same normalization and traceability process, enabling consistent analysis and ATT&CK mapping.

## Domain 3 — Network Security & Infrastructure Engineering

Infrastructure configuration data, including DNS, LDAP, SMB, and network segmentation, is normalized alongside identity evidence to support comprehensive attack-path analysis.

## Domain 4 — Governance, Risk & Compliance Intelligence

Normalized evidence feeds governance processes including evidence lineage, risk scoring, remediation tracking, compliance reporting, and executive decision support.

---

# 17. Roles and Responsibilities

| Role | Responsibility |
|------|----------------|
| Security Assessor | Collect and register evidence |
| Detection Engineer | Validate telemetry-related evidence |
| Governance Analyst | Verify evidence quality and traceability |
| Infrastructure Administrator | Support authorized evidence collection |
| Executive Stakeholder | Review evidence-backed risk reporting |

---

# 18. Workflow Governance

This document serves as the authoritative workflow for evidence normalization within Domain 5.

All assessment artifacts, technical findings, dashboards, reports, and executive deliverables shall reference normalized evidence produced in accordance with this workflow.

Changes to this workflow shall be documented, version controlled, and approved prior to implementation.

---

# Document Approval

| Role | Name | Status |
|------|------|--------|
| Project Owner | Lighthouse Technology | Approved |
| Security Assessor | __________________ | B. Solomon Henry |
| Reviewer | __________________ | Lighthouse Technology Security Team |

---

**End of Document**
