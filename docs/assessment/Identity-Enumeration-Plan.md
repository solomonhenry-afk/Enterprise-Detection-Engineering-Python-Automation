# Lighthouse Technology

# Enterprise Security Evolution

## Domain 5 — Enterprise Active Directory Penetration Testing & Security Auditing

# Identity Enumeration Plan

| Document Information | |
|----------------------|------------------------------------------------|
| Document ID | LHT-PLAN-001 |
| Version | 1.0 |
| Status | Approved |
| Classification | Internal |
| Project | Enterprise Security Evolution |
| Domain | Domain 5 |
| Owner | Lighthouse Technology |
| Last Updated | 2026-07-13 |
| Related Documents | LHT-METH-001 Active Directory Baseline Audit Methodology, LHT-METH-002 Identity Inventory Methodology, LHT-METH-003 Evidence Normalization Workflow |

---

# 1. Purpose

This document defines the operational plan for enumerating identity-related objects within the authorized Lighthouse Technology Enterprise Active Directory lab.

The objective is to produce a complete, evidence-backed inventory of Active Directory identities and their relationships while maintaining evidence integrity, traceability, and repeatability.

This plan establishes **what will be collected**, **why it is collected**, **how it will be classified**, and **how the resulting datasets will support subsequent assessment phases**.

No inventory data, technical findings, or assessment conclusions are contained within this document.

---

# 2. Objectives

The identity enumeration process aims to:

- Identify all in-scope Active Directory identity objects.
- Build a normalized inventory for technical analysis.
- Establish identity relationships required for attack-path analysis.
- Identify privileged identities and Tier Zero assets.
- Support governance, detection engineering, and executive reporting.
- Maintain evidence traceability from collection through reporting.

---

# 3. Assessment Scope

The following object categories are included in the enumeration plan.

| Category | Collection Objective |
|----------|----------------------|
| Users | Identify standard and privileged user accounts |
| Groups | Enumerate security and distribution groups |
| Computers | Inventory all domain-joined systems |
| Service Accounts | Identify traditional and managed service accounts |
| Organizational Units | Document administrative boundaries |
| Group Policy Objects | Identify policies affecting identity security |
| Trust Relationships | Document domain and forest trusts |
| Delegation | Identify delegation configurations |
| Domain Controllers | Inventory authentication infrastructure |
| Tier Zero Assets | Identify critical identities and systems |
| Access Control Relationships | Support privilege exposure analysis |

---

# 4. Authorization Boundary

Enumeration activities shall be conducted only within the authorized Lighthouse Technology Enterprise Lab.

The following are explicitly excluded:

- Production environments
- Third-party Active Directory forests
- External identity providers
- Unauthorized systems
- Internet-facing infrastructure outside the approved assessment scope

All collection activities shall comply with the Rules of Engagement established during Phase A.

---

# 5. Enumeration Principles

The identity enumeration process is governed by the following principles:

## Evidence-Driven Collection

All inventory records shall originate from authorized evidence sources.

## Completeness

Enumeration shall include all in-scope identity objects required for the assessment.

## Least Assumption

Unknown or incomplete data shall be marked as pending validation rather than inferred.

## Traceability

Every inventory record shall reference supporting evidence.

## Repeatability

Enumeration activities shall be reproducible using the documented methodology and collection procedures.

---

# 6. Planned Enumeration Sequence

Identity enumeration shall proceed in the following order to maximize data quality and relationship accuracy.

| Phase | Activity | Expected Output |
|------|----------|-----------------|
| 1 | Enumerate Domains and Forest | Domain inventory |
| 2 | Enumerate Organizational Units | OU inventory |
| 3 | Enumerate Users | User inventory |
| 4 | Enumerate Groups | Group inventory |
| 5 | Enumerate Computers | Computer inventory |
| 6 | Enumerate Service Accounts | Service account inventory |
| 7 | Enumerate Group Policy Objects | GPO inventory |
| 8 | Enumerate Trust Relationships | Trust inventory |
| 9 | Enumerate Delegation Configurations | Delegation inventory |
| 10 | Identify Tier Zero Assets | Tier Zero inventory |
| 11 | Normalize Collected Data | Standardized datasets |
| 12 | Validate Inventory | Approved inventory for analysis |

---

# 7. Planned Evidence Sources

The following evidence sources may be used within the authorized assessment.

| Source | Purpose | Expected Output | Initial Status |
|---------|---------|----------------|----------------|
| PowerShell Active Directory Module | Directory object inventory | CSV / JSON / XML | Proposed |
| ADRecon | Configuration inventory | HTML / CSV | Proposed |
| BloodHound Community Edition | Identity relationships | JSON / ZIP | Proposed |
| Group Policy Reports | Policy inventory | XML / HTML | Proposed |
| Windows Event Logs | Supporting identity context | EVTX | Proposed |
| Sysmon | Endpoint telemetry | EVTX | Proposed |

Evidence shall remain in the **Proposed** lifecycle state until collected within the authorized laboratory.

---

# 8. Inventory Classification

Each enumerated object shall be classified using standardized attributes.

## Identity Classification

- Standard User
- Administrative User
- Service Account
- Group Managed Service Account (gMSA)
- Computer
- Domain Controller
- Security Group
- Distribution Group

## Tier Classification

- Tier Zero
- Tier One
- Tier Two
- Unclassified (Pending Validation)

## Privilege Classification

- Standard
- Privileged
- Delegated
- Pending Validation

---

# 9. Data Normalization

Collected identity information shall be normalized before technical analysis.

Normalization activities include:

- Standardized naming conventions
- Unified attribute names
- Consistent timestamp formats
- Duplicate detection and removal
- Source attribution
- Evidence identifier assignment
- Metadata enrichment

Normalized data shall preserve references to the original evidence source.

---

# 10. Evidence Management

Each inventory record shall include:

- Lighthouse Evidence ID
- Collection Method
- Source Tool
- Collection Date
- Validation Status
- Evidence Lifecycle Status
- Related Asset(s)
- Related Identity(ies)

Evidence shall be managed in accordance with the Evidence Normalization Workflow.

---

# 11. Validation Criteria

Enumeration shall be considered complete when:

- All scoped identity categories have been collected.
- Inventory records have been normalized.
- Duplicate records have been reviewed.
- Classification has been completed.
- Evidence references are present.
- Validation status has been assigned.
- Data quality checks have been completed.

Records failing validation shall be flagged for review before use in technical analysis.

---

# 12. Expected Deliverables

This plan supports the production of:

- Identity Inventory
- Computer Inventory
- Group Inventory
- Service Account Inventory
- Delegation Inventory
- GPO Inventory
- Tier Zero Inventory
- Relationship Inventory
- Normalized Identity Dataset
- Evidence Manifest
- Data Quality Report

---

# 13. Dependencies

The identity enumeration process depends upon:

- Assessment authorization (Phase A)
- Repository governance framework (Phase B)
- Methodology documents (Phase C)
- Availability of authorized evidence sources
- Evidence registration and lifecycle management

No enumeration activities shall commence until these prerequisites have been satisfied.

---

# 14. Cross-Domain Integration

## Domain 1 — SOC Operations, Telemetry & Detection Engineering

The normalized identity inventory will enrich Windows Event Logs, Sysmon telemetry, and Splunk detections by providing authoritative identity and asset context.

## Domain 2 — Enterprise Adversary Validation & Purple Team Operations

Enumerated identities, privileged groups, and systems establish the scope for controlled Purple Team validation and MITRE ATT&CK mapping.

## Domain 3 — Network Security & Infrastructure Engineering

Identity objects will be correlated with Domain Controllers, DNS, LDAP, SMB services, and segmented infrastructure to support exposure analysis.

## Domain 4 — Governance, Risk & Compliance Intelligence

Inventory datasets become governed assets that support evidence lineage, risk scoring, remediation planning, compliance reporting, and executive decision-making.

---

# 15. Success Criteria

The Identity Enumeration Plan shall be considered successfully executed when:

- All in-scope Active Directory identity objects have been inventoried.
- Inventory data has been normalized and validated.
- Evidence is fully traceable.
- Identity relationships support subsequent attack-path analysis.
- Tier Zero assets have been identified.
- The inventory is suitable for privilege exposure assessment, detection validation, remediation engineering, and executive reporting.

---

# Document Approval

| Role | Name | Status |
|------|------|--------|
| Project Owner | Lighthouse Technology | Approved |
| Security Assessor | __________________ | B. Solomon Henry |
| Reviewer | __________________ | Lighthouse Technology Security Team |

---

**End of Document**
