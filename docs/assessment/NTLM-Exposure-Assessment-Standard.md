# Lighthouse Technology

# Enterprise Security Evolution

## Domain 5 — Enterprise Active Directory Penetration Testing & Security Auditing

# NTLM Exposure Assessment Standard

| Document Information | |
|----------------------|------------------------------------------------|
| Document ID | LHT-STD-004 |
| Version | 1.0 |
| Status | Approved |
| Classification | Internal |
| Project | Enterprise Security Evolution |
| Domain | Domain 5 |
| Owner | Lighthouse Technology |
| Last Updated | 2026-07-13 |
| Related Documents | LHT-PLAN-003 Credential Security Assessment Plan, LHT-PLAN-004 Authentication Security Assessment Plan, LHT-STD-003 Kerberos Security Standard, LHT-STD-002 Service Account Assessment Standard |

---

# 1. Purpose

This standard establishes the methodology for assessing NTLM authentication exposure within the authorized Lighthouse Technology Enterprise Active Directory laboratory.

NTLM remains present in many enterprise environments due to application dependencies, legacy systems, and compatibility requirements. However, unmanaged NTLM usage may increase identity risk by introducing weaker authentication dependencies and reducing visibility into modern authentication controls.

The purpose of this standard is to define how NTLM usage, configuration, dependencies, and security controls are assessed in a consistent, evidence-driven manner.

This document defines assessment standards only. It does not contain assessment findings or technical conclusions.

---

# 2. Objectives

The NTLM exposure assessment aims to:

- Identify where NTLM authentication is present.
- Evaluate NTLM dependency across enterprise systems.
- Assess NTLM-related security configurations.
- Identify legacy authentication risks.
- Review authentication monitoring capabilities.
- Determine opportunities for reducing unnecessary NTLM usage.
- Support risk prioritization and remediation planning.

---

# 3. Scope

This standard applies to NTLM-related authentication components within the authorized Active Directory environment.

Assessment scope includes:

| Component | Assessment Focus |
|-----------|------------------|
| Domain Controllers | NTLM configuration and authentication support |
| Workstations | NTLM usage and dependencies |
| Servers | Application and service dependencies |
| Service Accounts | Authentication requirements |
| Applications | Legacy authentication requirements |
| Group Policy | NTLM-related security controls |
| Authentication Logs | NTLM visibility |
| Administrative Systems | Privileged authentication pathways |

---

# 4. Authorization Boundary

NTLM assessment activities are restricted to the authorized Lighthouse Technology Enterprise Active Directory laboratory.

The assessment excludes:

- Production environments
- External organizations
- Unauthorized authentication systems
- Unapproved configuration changes
- Any activity that may disrupt authentication availability

All activities shall follow the Domain 5 Rules of Engagement.

---

# 5. NTLM Security Principles

The assessment follows these principles.

## Authentication Modernization

Organizations should reduce unnecessary dependence on legacy authentication mechanisms.

## Business Awareness

NTLM dependencies shall be evaluated in relation to operational requirements.

## Least Privilege

Authentication privileges and service dependencies should be minimized.

## Visibility

Authentication activity should be observable through security telemetry.

## Evidence-Based Assessment

All conclusions must be supported by validated evidence.

---

# 6. NTLM Assessment Areas

The assessment will evaluate:

| Area | Assessment Objective |
|------|----------------------|
| NTLM Configuration | Review enterprise authentication settings |
| NTLM Usage | Identify authentication dependencies |
| Legacy Applications | Identify systems requiring NTLM |
| Service Dependencies | Review service authentication requirements |
| Group Policy Controls | Evaluate NTLM security policies |
| Administrative Authentication | Review privileged authentication usage |
| Monitoring Coverage | Validate NTLM visibility |
| Migration Readiness | Identify modernization opportunities |

---

# 7. Planned Evidence Sources

The following sources may support NTLM assessment.

| Source | Purpose | Expected Output | Status |
|--------|---------|----------------|--------|
| Group Policy Reports | NTLM configuration review | HTML / XML | Proposed |
| PowerShell Active Directory Module | Identity context | CSV / JSON / XML | Proposed |
| Windows Security Event Logs | Authentication activity | EVTX | Proposed |
| Sysmon | Endpoint telemetry | EVTX | Proposed |
| Splunk | Detection validation | Searches / Reports | Proposed |
| Application Documentation | Dependency analysis | Documents | Proposed |

Evidence remains **Proposed** until collected and validated.

---

# 8. NTLM Control Categories

The following controls shall be assessed.

## NTLM Configuration Management

Review authentication policies governing NTLM usage.

## Legacy Dependency Identification

Identify applications, services, and systems requiring NTLM.

## Administrative Authentication Review

Assess whether privileged identities depend on legacy authentication.

## Monitoring and Detection

Evaluate visibility into NTLM authentication activity.

## Risk Reduction Planning

Identify opportunities to reduce unnecessary NTLM dependency.

---

# 9. Risk Evaluation Criteria

NTLM exposure shall be evaluated using the Domain 4 risk methodology.

Assessment factors include:

- Authentication sensitivity
- Identity privilege level
- System criticality
- Legacy dependency
- Business impact
- Detection coverage
- Remediation complexity

Risk ratings shall only be assigned after evidence validation.

---

# 10. Evidence Requirements

Each NTLM assessment observation shall reference:

- Lighthouse Evidence ID
- Source System
- Collection Method
- Collection Date
- Validation Status
- Related Identity
- Related Application or System
- Related Finding
- Related Remediation

No NTLM exposure finding shall exist without supporting evidence.

---

# 11. Assessment Workflow

The NTLM assessment shall follow this workflow:

1. Confirm authorization.
2. Review authentication architecture.
3. Identify NTLM configuration sources.
4. Collect approved evidence.
5. Review NTLM dependencies.
6. Analyze authentication visibility.
7. Validate evidence quality.
8. Document observations.
9. Assess business impact.
10. Recommend remediation.
11. Validate security improvements.

---

# 12. Expected Deliverables

Implementation of this standard supports:

- NTLM Exposure Assessment Report
- Authentication Security Assessment Report
- Credential Security Assessment Report
- Detection Coverage Matrix
- Risk Register Updates
- Enterprise Remediation Roadmap
- Executive Risk Summary

---

# 13. Cross-Domain Integration

## Domain 1 — SOC Operations, Telemetry & Detection Engineering

NTLM assessment improves authentication monitoring by identifying required telemetry sources, detection opportunities, and visibility gaps.

## Domain 2 — Enterprise Adversary Validation & Purple Team Operations

NTLM exposure analysis provides context for controlled authentication security validation activities.

## Domain 3 — Network Security & Infrastructure Engineering

NTLM dependencies are evaluated alongside SMB, LDAP, WinRM, DNS, and enterprise infrastructure design.

## Domain 4 — Governance, Risk & Compliance Intelligence

NTLM findings support evidence lineage, risk scoring, remediation tracking, control validation, and executive communication.

---

# 14. Success Criteria

This standard is successfully implemented when:

- NTLM dependencies have been identified.
- Authentication evidence has been collected and validated.
- Legacy authentication risks have been documented.
- Detection requirements have been identified.
- Modernization opportunities have been prioritized.
- Remediation actions can be validated.

---

# Document Approval

| Role | Name | Status |
|------|------|--------|
| Project Owner | Lighthouse Technology | Approved |
| Security Assessor | B. Solomon Henry | Approved |
| Reviewer | Lighthouse Technology Security Team | Approved |

---
