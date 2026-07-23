# Lighthouse Technology

# Enterprise Security Evolution

## Domain 5 — Enterprise Active Directory Penetration Testing & Security Auditing

# Tier Zero Classification Standard

| Document Information | |
|----------------------|------------------------------------------------|
| Document ID | LHT-STD-001 |
| Version | 1.0 |
| Status | Approved |
| Classification | Internal |
| Project | Enterprise Security Evolution |
| Domain | Domain 5 |
| Owner | Lighthouse Technology |
| Last Updated | 2026-07-13 |
| Related Documents | LHT-METH-001 Active Directory Baseline Audit Methodology, LHT-METH-002 Identity Inventory Methodology, LHT-METH-003 Evidence Normalization Workflow, LHT-PLAN-001 Identity Enumeration Plan, LHT-PLAN-002 Privilege Exposure Assessment Plan |

---

# 1. Purpose

This document establishes the Lighthouse Technology standard for identifying, classifying, and governing Tier Zero assets within the authorized Enterprise Active Directory laboratory.

Tier Zero assets represent the highest-value identity and infrastructure components whose compromise could result in complete or near-complete control of the Active Directory environment.

This standard provides a consistent framework for identifying Tier Zero assets, prioritizing risk, guiding remediation, and supporting executive reporting.

This document defines classification criteria only. It does not identify or list specific Tier Zero assets.

---

# 2. Objectives

The objectives of this standard are to:

- Define the Tier Zero security boundary.
- Standardize Tier Zero classification across the assessment.
- Support consistent privilege exposure analysis.
- Prioritize remediation efforts based on identity criticality.
- Enable evidence-backed attack-path analysis.
- Improve governance and executive decision-making.

---

# 3. Scope

This standard applies to all identity and infrastructure objects included in the authorized Domain 5 assessment.

Applicable object categories include:

- Active Directory Forest
- Active Directory Domains
- Domain Controllers
- Administrative Accounts
- Privileged Groups
- Authentication Infrastructure
- Group Policy Objects
- Service Accounts
- Group Managed Service Accounts (gMSA)
- Delegation Configurations
- Access Control Relationships
- Administrative Workstations
- Identity Management Systems

---

# 4. Authorization Boundary

Tier Zero classification activities shall only be performed within the authorized Lighthouse Technology Enterprise Lab.

This standard shall not be applied to:

- Production environments
- Third-party Active Directory forests
- External organizations
- Unauthorized infrastructure

Classification activities shall comply with the Rules of Engagement established during Phase A.

---

# 5. Definition of Tier Zero

For the purposes of this assessment, a Tier Zero asset is any identity, system, service, or configuration that can directly or indirectly influence the security, integrity, or availability of the Active Directory environment.

Compromise of a Tier Zero asset may enable:

- Enterprise-wide privilege escalation
- Authentication compromise
- Administrative persistence
- Credential theft
- Directory replication abuse
- Group Policy manipulation
- Identity infrastructure compromise

---

# 6. Tier Zero Classification Principles

Classification shall be based on the following principles.

## Business Criticality

Assess the operational importance of the asset.

## Security Impact

Evaluate the potential impact of compromise on the enterprise identity infrastructure.

## Administrative Authority

Determine the level of control the asset has over authentication, authorization, or directory services.

## Attack Path Significance

Assess whether the asset enables or shortens privilege escalation or lateral movement paths.

## Evidence-Based Classification

Tier Zero designation shall only be assigned following evidence validation.

---

# 7. Tier Zero Classification Categories

The following categories may qualify as Tier Zero depending on validated evidence.

| Category | Description |
|----------|-------------|
| Domain Controllers | Systems hosting Active Directory Domain Services |
| Enterprise Administrative Accounts | Identities with enterprise-wide administrative authority |
| Domain Administrative Accounts | Identities with domain-wide administrative authority |
| Enterprise Administrative Groups | Groups controlling critical identity infrastructure |
| Authentication Services | Kerberos, LDAP, and related authentication components |
| Active Directory DNS | DNS services supporting Active Directory operations |
| Privileged Group Policy Objects | GPOs affecting Tier Zero assets |
| Administrative Service Accounts | High-privilege service identities |
| Identity Management Infrastructure | Systems responsible for identity administration |
| Delegated Administrative Components | Delegations providing effective Tier Zero control |

Inclusion in these categories does not automatically confer Tier Zero status; validation is required.

---

# 8. Classification Criteria

An asset may be classified as Tier Zero if one or more of the following conditions apply.

- Direct administrative control over Active Directory.
- Authority to modify authentication mechanisms.
- Ability to manage privileged identities or groups.
- Ability to alter Group Policy affecting enterprise security.
- Ability to influence directory replication.
- Control of enterprise authentication infrastructure.
- Effective administrative authority through delegated permissions.
- Significant role within validated attack paths.

Classification decisions shall be documented and supported by evidence.

---

# 9. Planned Evidence Sources

Tier Zero classification may be informed by the following authorized evidence sources.

| Source | Purpose | Initial Status |
|---------|---------|----------------|
| PowerShell Active Directory Module | Administrative object inventory | Proposed |
| BloodHound Community Edition | Privilege relationship analysis | Proposed |
| ADRecon | Active Directory configuration review | Proposed |
| Group Policy Reports | Administrative policy review | Proposed |
| Windows Event Logs | Administrative activity context | Proposed |
| Sysmon | Endpoint telemetry | Proposed |
| Splunk | Detection validation | Proposed |

No source shall be considered collected evidence until acquired within the authorized laboratory.

---

# 10. Classification Workflow

Tier Zero classification shall follow the process below.

1. Confirm authorization.
2. Review normalized identity inventory.
3. Identify candidate Tier Zero assets.
4. Validate supporting evidence.
5. Assess administrative authority.
6. Evaluate identity relationships.
7. Determine attack-path significance.
8. Assign Tier Zero classification.
9. Register supporting evidence.
10. Document classification rationale.

---

# 11. Evidence Requirements

Each Tier Zero classification shall reference:

- Lighthouse Evidence ID
- Source Tool
- Collection Method
- Collection Date
- Validation Status
- Related Identity
- Related Asset
- Supporting Relationships
- Assessment Notes

No Tier Zero classification shall exist without supporting evidence.

---

# 12. Risk Considerations

Tier Zero assets represent the highest priority for:

- Identity protection
- Detection engineering
- Administrative monitoring
- Remediation planning
- Security hardening
- Executive oversight

Compromise scenarios involving Tier Zero assets shall receive priority consideration during subsequent assessment phases.

---

# 13. Expected Deliverables

Execution of this standard supports the production of:

- Tier Zero Inventory
- Privilege Exposure Report
- Attack Path Analysis
- Detection Coverage Matrix
- Enterprise Remediation Roadmap
- Executive Risk Summary
- MITRE ATT&CK Mapping
- Purple Team Validation Report

---

# 14. Cross-Domain Integration

## Domain 1 — SOC Operations, Telemetry & Detection Engineering

Tier Zero classifications enrich Windows Event Logs, Sysmon telemetry, and Splunk detections by identifying the highest-value identities and systems requiring enhanced monitoring.

## Domain 2 — Enterprise Adversary Validation & Purple Team Operations

Tier Zero assets define the protected identity boundary used during authorized Purple Team validation and ATT&CK-based detection testing.

## Domain 3 — Network Security & Infrastructure Engineering

Tier Zero identities are correlated with Domain Controllers, DNS, LDAP, SMB, WinRM, and segmented infrastructure to understand enterprise attack paths and administrative dependencies.

## Domain 4 — Governance, Risk & Compliance Intelligence

Tier Zero classifications support governance processes including risk scoring, evidence lineage, remediation prioritization, compliance reporting, and executive communication.

---

# 15. Success Criteria

This standard shall be considered successfully implemented when:

- Tier Zero classification criteria have been consistently applied.
- Classification decisions are supported by validated evidence.
- Tier Zero assets are traceable to normalized inventory records.
- Classification outputs support privilege exposure analysis, attack-path assessment, detection engineering, and remediation planning.

---

# Document Approval

| Role | Name | Status |
|------|------|--------|
| Project Owner | Lighthouse Technology | Approved |
| Security Assessor | __________________ | B. Solomon Henry |
| Reviewer | __________________ | Lighthouse Technology Security Team |

---

**End of Document**
