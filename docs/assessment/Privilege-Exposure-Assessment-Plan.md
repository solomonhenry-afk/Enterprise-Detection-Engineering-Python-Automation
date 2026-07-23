# Lighthouse Technology

# Enterprise Security Evolution

## Domain 5 — Enterprise Active Directory Penetration Testing & Security Auditing

# Privilege Exposure Assessment Plan

| Document Information | |
|----------------------|------------------------------------------------|
| Document ID | LHT-PLAN-002 |
| Version | 1.0 |
| Status | Approved |
| Classification | Internal |
| Project | Enterprise Security Evolution |
| Domain | Domain 5 |
| Owner | Lighthouse Technology |
| Last Updated | 2026-07-13 |
| Related Documents | LHT-METH-001 Active Directory Baseline Audit Methodology, LHT-METH-002 Identity Inventory Methodology, LHT-METH-003 Evidence Normalization Workflow, LHT-PLAN-001 Identity Enumeration Plan |

---

# 1. Purpose

This document defines the structured approach for assessing identity-based privilege exposure within the authorized Lighthouse Technology Enterprise Active Directory laboratory.

The assessment evaluates how privileged identities, administrative relationships, delegation configurations, and access control assignments may increase enterprise identity risk.

The objective is to identify, classify, prioritize, and document privilege exposure using verified assessment evidence while maintaining complete traceability and governance.

This document defines the assessment process. It does not contain technical findings or assessment results.

---

# 2. Objectives

The privilege exposure assessment aims to:

- Identify privileged identities and administrative groups.
- Classify Tier Zero identities and systems.
- Evaluate delegated administrative rights.
- Assess access control relationships.
- Identify identity configurations that may increase attack surface.
- Prioritize identity risk using the Domain 4 risk scoring methodology.
- Support subsequent attack-path analysis, detection engineering, remediation planning, and executive reporting.

---

# 3. Assessment Scope

The following identity categories are included in the privilege exposure assessment.

| Category | Assessment Objective |
|----------|----------------------|
| Privileged Users | Review administrative assignments and privilege scope |
| Privileged Groups | Assess membership and administrative exposure |
| Tier Zero Assets | Validate critical identity infrastructure |
| Service Accounts | Review privilege levels and operational necessity |
| Group Managed Service Accounts (gMSA) | Validate deployment and privilege assignments |
| Domain Controllers | Assess administrative dependencies |
| Organizational Units | Review delegated administration |
| Group Policy Objects | Assess privileged policy management |
| Delegation Configurations | Review constrained, unconstrained, and resource-based delegation |
| Access Control Lists (ACLs) | Assess delegated permissions and administrative control |

---

# 4. Authorization Boundary

Privilege exposure assessment activities shall be conducted exclusively within the authorized Lighthouse Technology Enterprise Lab.

The assessment excludes:

- Production environments
- Third-party Active Directory forests
- External organizations
- Unauthorized systems
- Identity providers outside the approved assessment scope

Assessment activities shall remain non-destructive and aligned with the Rules of Engagement established during Phase A.

---

# 5. Assessment Principles

The privilege exposure assessment is governed by the following principles.

## Evidence-Driven Assessment

All observations shall be supported by collected and validated evidence.

## Least Privilege

Exposure shall be evaluated against the principle of least privilege.

## Business Context

Privilege shall be evaluated in relation to operational requirements.

## Risk Prioritization

Exposure shall be prioritized according to likelihood, business impact, and potential identity compromise.

## Traceability

Every assessment observation shall reference supporting evidence.

---

# 6. Planned Assessment Areas

The assessment will evaluate the following areas.

| Assessment Area | Objective |
|-----------------|-----------|
| Administrative Groups | Identify excessive administrative membership |
| Tier Zero | Identify exposure of critical assets and identities |
| Service Accounts | Evaluate privilege, ownership, and lifecycle |
| Password Governance | Assess privileged credential management |
| Delegation | Review delegation configurations |
| ACL Exposure | Assess delegated administrative rights |
| Trust Relationships | Review privilege implications of trusts |
| GPO Administration | Evaluate policy management permissions |
| Domain Controller Administration | Assess administrative dependencies |
| Authentication Services | Review Kerberos, LDAP, SMB, and related identity services |

---

# 7. Planned Evidence Sources

The following evidence sources may support the privilege exposure assessment.

| Source | Purpose | Expected Output | Initial Status |
|---------|---------|----------------|----------------|
| PowerShell Active Directory Module | Identity and privilege inventory | CSV / JSON / XML | Proposed |
| BloodHound Community Edition | Relationship analysis | JSON / ZIP | Proposed |
| ADRecon | Configuration assessment | HTML / CSV | Proposed |
| Group Policy Reports | Administrative policy review | XML / HTML | Proposed |
| Windows Event Logs | Administrative activity context | EVTX | Proposed |
| Sysmon | Endpoint telemetry | EVTX | Proposed |
| Splunk | Detection validation | Reports / Searches | Proposed |

No evidence shall be considered collected until acquired from the authorized laboratory.

---

# 8. Privilege Classification Model

Each identity shall be classified according to privilege level.

| Classification | Description |
|----------------|-------------|
| Tier Zero | Critical enterprise identity or infrastructure asset |
| Highly Privileged | Enterprise-wide administrative authority |
| Delegated Administrative | Limited administrative authority |
| Standard User | No elevated administrative rights |
| Pending Validation | Classification awaiting evidence review |

---

# 9. Planned Exposure Indicators

The following conditions will be evaluated as potential indicators of elevated identity risk.

- Excessive privileged group membership
- Stale privileged accounts
- Dormant administrative accounts
- Privileged service accounts
- Excessive delegated permissions
- Weak separation of administrative duties
- Broad ACL assignments
- High-value authentication dependencies
- Legacy administrative configurations
- Incomplete identity governance controls

The presence of an indicator does not constitute a confirmed finding until validated.

---

# 10. Risk Assessment Approach

Privilege exposure will be assessed using the governance framework established in Domain 4.

Risk evaluation will consider:

- Likelihood of misuse
- Potential business impact
- Privilege level
- Scope of administrative access
- Identity criticality
- Existing compensating controls
- Detection coverage
- Remediation complexity

Risk ratings shall only be assigned following evidence validation.

---

# 11. Evidence Requirements

Each assessment observation shall reference:

- Lighthouse Evidence ID
- Collection Method
- Source Tool
- Collection Date
- Validation Status
- Related Identity
- Related Asset
- Related Finding
- Related Remediation

Assessment conclusions shall not be documented without supporting evidence.

---

# 12. Assessment Workflow

The privilege exposure assessment shall follow the sequence below.

1. Confirm assessment authorization.
2. Review normalized identity inventory.
3. Identify privileged identities.
4. Classify Tier Zero assets.
5. Evaluate group memberships.
6. Review delegated permissions.
7. Assess ACL relationships.
8. Review service account exposure.
9. Correlate telemetry where applicable.
10. Prioritize exposure.
11. Register technical findings.
12. Recommend remediation actions.
13. Validate corrective actions.
14. Update evidence records.

---

# 13. Expected Deliverables

Execution of this assessment plan supports the creation of:

- Privilege Exposure Report
- Tier Zero Assessment
- Administrative Exposure Analysis
- Identity Risk Register
- Detection Coverage Matrix
- Attack Path Assessment
- Enterprise Remediation Roadmap
- Executive Risk Summary

---

# 14. Cross-Domain Integration

## Domain 1 — SOC Operations, Telemetry & Detection Engineering

Privilege classifications enrich Windows Event Logs, Sysmon telemetry, and Splunk detections by identifying the significance of administrative identities and privileged activity.

## Domain 2 — Enterprise Adversary Validation & Purple Team Operations

The assessment establishes the baseline for controlled validation of identity-related attack techniques and ATT&CK mappings.

## Domain 3 — Network Security & Infrastructure Engineering

Privilege exposure is correlated with Domain Controllers, DNS, LDAP, SMB, WinRM, and segmented infrastructure to identify high-risk identity pathways.

## Domain 4 — Governance, Risk & Compliance Intelligence

Assessment results feed governance processes including evidence lineage, risk scoring, remediation prioritization, compliance reporting, and executive decision support.

---

# 15. Success Criteria

The privilege exposure assessment shall be considered complete when:

- Privileged identities have been classified.
- Tier Zero assets have been identified.
- Administrative relationships have been evaluated.
- Delegation configurations have been reviewed.
- Evidence has been validated and linked to observations.
- Risk ratings have been assigned.
- Findings are suitable for attack-path analysis, remediation engineering, and executive reporting.

---

# Document Approval

| Role | Name | Status |
|------|------|--------|
| Project Owner | Lighthouse Technology | Approved |
| Security Assessor | __________________ | B. Solomon Henry |
| Reviewer | __________________ | Lighthouse Technology Security Team |

---

**End of Document**
