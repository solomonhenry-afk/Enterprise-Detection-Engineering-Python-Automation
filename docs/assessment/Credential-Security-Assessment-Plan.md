# Lighthouse Technology

# Enterprise Security Evolution

## Domain 5 — Enterprise Active Directory Penetration Testing & Security Auditing

# Credential Security Assessment Plan

| Document Information | |
|----------------------|------------------------------------------------|
| Document ID | LHT-PLAN-003 |
| Version | 1.0 |
| Status | Approved |
| Classification | Internal |
| Project | Enterprise Security Evolution |
| Domain | Domain 5 |
| Owner | Lighthouse Technology |
| Last Updated | 2026-07-12 |
| Related Documents | LHT-METH-001, LHT-METH-002, LHT-METH-003, LHT-PLAN-001, LHT-PLAN-002, LHT-STD-001 |

---

# 1. Purpose

This document defines the assessment strategy for evaluating credential security within the authorized Lighthouse Technology Enterprise Active Directory laboratory.

The assessment focuses on the security of enterprise credentials, authentication mechanisms, privileged identities, and credential governance controls.

Its objective is to identify credential-related exposure, validate security controls, prioritize risk, and support remediation planning using verified assessment evidence.

This document defines the assessment process only. It does not contain assessment findings or technical conclusions.

---

# 2. Assessment Objectives

The credential security assessment aims to:

- Evaluate enterprise password policy configuration.
- Review privileged credential governance.
- Assess service account credential hygiene.
- Validate implementation of managed credential technologies.
- Review legacy authentication exposure.
- Assess credential storage and protection controls.
- Identify identity configurations that may increase credential risk.
- Support attack-path analysis and detection engineering.
- Provide evidence-backed recommendations for remediation.

---

# 3. Assessment Scope

The assessment includes the following credential security areas.

| Assessment Area | Objective |
|-----------------|-----------|
| Password Policy | Review enterprise password controls |
| Fine-Grained Password Policies | Evaluate differentiated credential policies |
| Service Accounts | Assess credential management and lifecycle |
| Group Managed Service Accounts (gMSA) | Validate managed credential implementation |
| Local Administrator Password Solution (LAPS) | Review local administrator password management |
| Privileged Accounts | Assess administrative credential hygiene |
| Kerberos Authentication | Evaluate secure authentication configuration |
| NTLM Authentication | Assess legacy authentication exposure |
| Credential Storage | Review protection of authentication secrets |
| Legacy Authentication | Identify deprecated authentication mechanisms |

---

# 4. Authorization Boundary

Credential security assessment activities shall be conducted exclusively within the authorized Lighthouse Technology Enterprise Lab.

The assessment excludes:

- Production environments
- External identity providers
- Third-party Active Directory environments
- Unauthorized credential stores
- Systems outside the approved Rules of Engagement

Any controlled validation involving credentials shall remain low-risk, reversible, and fully authorized.

---

# 5. Assessment Principles

The assessment is governed by the following principles.

## Evidence-Driven Assessment

All observations shall be supported by validated evidence collected from authorized sources.

## Least Privilege

Credential exposure shall be evaluated against the principle of least privilege.

## Credential Confidentiality

Sensitive credential material shall not be unnecessarily exposed, copied, or retained.

## Governance Alignment

Assessment activities shall align with organizational security governance and evidence lifecycle requirements.

## Repeatability

Assessment activities shall be repeatable using documented procedures and approved tools.

---

# 6. Planned Assessment Areas

The following areas will be reviewed during the assessment.

| Area | Assessment Focus |
|------|------------------|
| Password Policy | Complexity, length, history, lockout, expiration |
| Privileged Credentials | Administrative account protection |
| Service Accounts | Password age, ownership, privilege level |
| gMSA | Deployment and operational usage |
| LAPS | Implementation and configuration validation |
| Kerberos | Secure authentication configuration |
| NTLM | Legacy protocol exposure |
| Authentication Secrets | Storage and protection mechanisms |
| Credential Governance | Lifecycle management and ownership |

---

# 7. Planned Evidence Sources

The following evidence sources may support the assessment.

| Source | Purpose | Expected Output | Initial Status |
|---------|---------|----------------|----------------|
| PowerShell Active Directory Module | Credential-related configuration | CSV / XML / JSON | Proposed |
| Group Policy Reports | Password policy review | XML / HTML | Proposed |
| ADRecon | Active Directory configuration | HTML / CSV | Proposed |
| Windows Security Event Logs | Authentication activity | EVTX | Proposed |
| Sysmon | Authentication telemetry | EVTX | Proposed |
| Splunk | Detection correlation | Reports / Searches | Proposed |

Evidence shall remain in the **Proposed** lifecycle state until collected within the authorized laboratory.

---

# 8. Planned Credential Security Controls

The assessment will evaluate the implementation and effectiveness of the following controls.

- Enterprise password policies
- Fine-Grained Password Policies
- Administrative account separation
- Password history enforcement
- Account lockout controls
- Service account governance
- Managed service account deployment
- LAPS implementation
- Credential lifecycle management
- Legacy authentication reduction
- Administrative credential protection

---

# 9. Risk Evaluation Criteria

Credential-related exposure will be evaluated using the Domain 4 risk methodology.

Risk assessment factors include:

- Credential privilege level
- Likelihood of misuse
- Authentication dependency
- Business impact
- Detection coverage
- Existing compensating controls
- Remediation complexity

Risk ratings shall only be assigned after evidence validation.

---

# 10. Evidence Requirements

Every assessment observation shall reference:

- Lighthouse Evidence ID
- Collection Method
- Source Tool
- Collection Date
- Validation Status
- Related Identity
- Related Asset
- Related Finding
- Related Remediation

No technical finding shall exist without supporting evidence.

---

# 11. Assessment Workflow

Credential security assessment shall follow the sequence below.

1. Confirm assessment authorization.
2. Review password policy configuration.
3. Assess privileged account governance.
4. Review service account security.
5. Validate gMSA deployment.
6. Validate LAPS implementation.
7. Review Kerberos configuration.
8. Assess NTLM exposure.
9. Evaluate legacy authentication controls.
10. Correlate authentication telemetry.
11. Register evidence.
12. Assess risk.
13. Recommend remediation.
14. Validate corrective actions.

---

# 12. Expected Deliverables

Execution of this assessment plan supports the production of:

- Credential Security Assessment Report
- Password Policy Assessment
- Service Account Assessment
- Kerberos Security Assessment
- NTLM Exposure Assessment
- LAPS Validation Report
- gMSA Validation Report
- Authentication Risk Register
- Enterprise Remediation Roadmap
- Executive Risk Summary

---

# 13. Cross-Domain Integration

## Domain 1 — SOC Operations, Telemetry & Detection Engineering

Credential assessment results enrich Windows Security Events, Sysmon telemetry, and Splunk detections by identifying high-value authentication events and privileged identities.

## Domain 2 — Enterprise Adversary Validation & Purple Team Operations

Validated credential controls establish the baseline for later Purple Team validation of identity-focused ATT&CK techniques within the authorized lab.

## Domain 3 — Network Security & Infrastructure Engineering

Credential security is assessed alongside Kerberos, LDAP, SMB, WinRM, and other enterprise infrastructure components to understand authentication dependencies.

## Domain 4 — Governance, Risk & Compliance Intelligence

Assessment outputs contribute to evidence lineage, risk scoring, remediation prioritization, compliance reporting, and executive decision-making.

---

# 14. Success Criteria

This assessment plan shall be considered successfully executed when:

- Credential security controls have been evaluated.
- Evidence has been collected and validated.
- Credential-related risks have been documented.
- Findings support attack-path analysis and detection engineering.
- Remediation recommendations are evidence-backed.
- Outputs are suitable for executive reporting and governance.

---

# Document Approval

| Role | Name | Status |
|------|------|--------|
| Project Owner | Lighthouse Technology | Approved |
| Security Assessor | __________________ | B. Solomon Henry |
| Reviewer | __________________ | Lighthouse Technology Security Team |

---

