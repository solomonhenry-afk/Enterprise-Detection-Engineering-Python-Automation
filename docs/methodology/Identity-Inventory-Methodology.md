# Lighthouse Technology

# Enterprise Security Evolution

## Domain 5 — Enterprise Active Directory Penetration Testing & Security Auditing

# Identity Inventory Methodology

| Document Information | |
|----------------------|------------------------------------------------|
| Document ID | LHT-METH-002 |
| Version | 1.0 |
| Status | Approved |
| Classification | Internal |
| Project | Enterprise Security Evolution |
| Domain | Domain 5 |
| Owner | Lighthouse Technology |
| Last Updated | 2026-07-12 |
| Related Documents | LHT-METH-001 Active Directory Baseline Audit Methodology, Evidence Lifecycle Standard, Assessment Plan |

---

# 1. Purpose

This document defines the standardized methodology for identifying, collecting, classifying, normalizing, validating, and maintaining the enterprise identity inventory used throughout the Domain 5 Active Directory security assessment.

The inventory serves as the authoritative source for:

- Active Directory security auditing
- Privilege exposure analysis
- Attack-path assessment
- Detection engineering
- Purple Team validation
- Remediation planning
- Governance and executive reporting

This methodology governs **how identity information is managed**. It does not contain inventory records or assessment findings.

---

# 2. Objectives

The objectives of the identity inventory methodology are to:

- Produce a complete and repeatable inventory of scoped Active Directory objects.
- Standardize identity data collected from multiple evidence sources.
- Enable correlation between identities, systems, groups, and privileged relationships.
- Support attack-path and privilege exposure analysis.
- Maintain evidence traceability from collection through reporting.
- Provide a consistent dataset for governance, remediation, and executive reporting.

---

# 3. Scope

The inventory includes the following Active Directory object categories:

## Identity Objects

- User Accounts
- Administrative Accounts
- Service Accounts
- Group Managed Service Accounts (gMSA)
- Computer Accounts

## Security Objects

- Security Groups
- Distribution Groups
- Privileged Groups

## Infrastructure Objects

- Organizational Units (OUs)
- Group Policy Objects (GPOs)
- Domain Controllers
- Tier Zero Assets

## Relationship Objects

- Group Memberships
- Trust Relationships
- Delegation Configurations
- Access Control Lists (ACLs)
- Service Principal Names (SPNs)

---

# 4. Authorization Boundary

Inventory collection is restricted to the authorized Lighthouse Technology Enterprise Lab.

No inventory data shall be collected from:

- Production environments
- Third-party Active Directory forests
- External organizations
- Systems outside the approved assessment scope

All inventory activities shall comply with the Rules of Engagement established in Phase A.

---

# 5. Inventory Principles

The inventory shall adhere to the following principles.

## Completeness

Collect all in-scope identity objects required for the assessment.

## Accuracy

Inventory records shall accurately reflect collected evidence.

## Consistency

Data from multiple collection sources shall be normalized into a common schema.

## Traceability

Every inventory record shall be traceable to its original evidence source.

## Repeatability

The inventory process shall be repeatable using the documented methodology.

## Governance

Inventory records shall support governance, risk analysis, and executive reporting.

---

# 6. Inventory Categories

The following inventory categories shall be maintained throughout the assessment.

| Category | Purpose |
|----------|---------|
| Users | Standard and privileged user accounts |
| Groups | Security and distribution groups |
| Computers | Domain-joined systems |
| Service Accounts | Traditional and managed service accounts |
| Organizational Units | Administrative boundaries |
| Group Policy Objects | Policy management |
| Trusts | Domain and forest trust relationships |
| Delegation | Delegation configurations |
| Tier Zero | Critical identities and systems |
| ACL Relationships | Security descriptor analysis |

---

# 7. Planned Evidence Sources

Inventory data may be collected from the following authorized sources.

| Source | Purpose | Expected Output | Initial Status |
|--------|---------|----------------|----------------|
| PowerShell Active Directory Module | Directory inventory | CSV / JSON / XML | Proposed |
| ADRecon | Configuration inventory | CSV / HTML | Proposed |
| BloodHound Community Edition | Relationship graph | JSON | Proposed |
| Group Policy Reports | GPO inventory | XML / HTML | Proposed |
| Windows Event Logs | Identity context | EVTX | Proposed |
| Sysmon | Supporting telemetry | EVTX | Proposed |

No inventory data shall be considered collected until acquired from the authorized laboratory.

---

# 8. Identity Classification

Each inventory record shall be classified using standardized attributes.

## Identity Type

Examples include:

- Standard User
- Administrative User
- Service Account
- gMSA
- Computer
- Group
- Domain Controller

## Tier Classification

Identity records shall be assigned to the appropriate security tier.

Examples include:

- Tier Zero
- Tier One
- Tier Two
- Unclassified (Pending Validation)

## Privilege Classification

Each identity shall be categorized as:

- Privileged
- Standard
- Delegated
- Unknown (Pending Validation)

---

# 9. Data Normalization Standards

Data collected from multiple tools shall be normalized into a consistent structure.

Normalization shall include:

- Standardized object naming
- Consistent attribute naming
- Uniform date and time formats
- Normalized boolean values
- Removal of duplicate records
- Source attribution
- Evidence identifier assignment

Normalization improves data quality and enables correlation across assessment phases.

---

# 10. Inventory Validation

Inventory records shall undergo validation before being used for technical analysis.

Validation includes:

- Duplicate detection
- Missing attribute review
- Source verification
- Object classification review
- Evidence linkage verification
- Metadata completeness

Records failing validation shall be flagged for review before analysis.

---

# 11. Evidence Traceability

Each inventory record shall reference:

- Lighthouse Evidence ID
- Collection Method
- Collection Date
- Source Tool
- Validation Status
- Evidence Lifecycle Status

Inventory records shall never exist without supporting evidence references.

---

# 12. Data Quality Requirements

Inventory data shall satisfy the following quality requirements:

- Accurate
- Complete
- Consistent
- Traceable
- Reproducible where practical
- Timestamped
- Properly classified
- Version controlled

Any derived data shall remain linked to its originating evidence.

---

# 13. Inventory Workflow

The inventory lifecycle consists of the following stages.

1. Confirm assessment scope.
2. Collect inventory evidence.
3. Register evidence.
4. Normalize collected data.
5. Validate inventory records.
6. Classify identities.
7. Correlate relationships.
8. Publish normalized datasets.
9. Support technical analysis.
10. Maintain inventory throughout the assessment.

---

# 14. Inventory Deliverables

This methodology supports the production of:

- Normalized Identity Inventory
- Computer Inventory
- Service Account Inventory
- Group Inventory
- GPO Inventory
- Delegation Inventory
- Tier Zero Inventory
- Relationship Inventory
- Evidence Manifest
- Data Quality Report

---

# 15. Cross-Domain Integration

## Domain 1 — SOC Operations, Telemetry & Detection Engineering

Identity inventories provide context for Windows Event Logs, Sysmon telemetry, and Splunk detections by linking events to known users, systems, and privileged accounts.

## Domain 2 — Enterprise Adversary Validation & Purple Team Operations

The normalized inventory identifies the identities and systems that may be referenced during authorized Purple Team validation and attack-path analysis.

## Domain 3 — Network Security & Infrastructure Engineering

Inventory records correlate identity objects with infrastructure components such as Domain Controllers, DNS, LDAP, SMB services, and segmented network assets.

## Domain 4 — Governance, Risk & Compliance Intelligence

Inventory datasets support evidence lineage, asset governance, risk scoring, remediation planning, and executive reporting.

---

# 16. Roles and Responsibilities

| Role | Responsibility |
|------|----------------|
| Security Assessor | Coordinate inventory collection and validation |
| Infrastructure Administrator | Provide authorized access to inventory sources |
| Detection Engineer | Correlate identity data with telemetry |
| Governance Analyst | Verify evidence quality and traceability |
| Executive Stakeholder | Review inventory-driven risk summaries |

---

# 17. Methodology Governance

This document serves as the authoritative methodology for identity inventory management within Domain 5.

All inventory templates, normalized datasets, privilege assessments, attack-path analyses, and remediation activities shall align with this methodology.

Changes to this methodology shall be documented, reviewed, and version controlled.

---

# Document Approval

| Role | Name | Status |
|------|------|--------|
| Project Owner | Lighthouse Technology | Approved |
| Security Assessor | __________________ | B. Solomon Henry |
| Reviewer | __________________ | Lighthouse TechnologySecurity Team |

---

**End of Document**
