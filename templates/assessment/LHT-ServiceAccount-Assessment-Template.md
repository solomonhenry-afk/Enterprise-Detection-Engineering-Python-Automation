# Lighthouse Technology

# Enterprise Security Evolution

## Domain 5 — Enterprise Active Directory Penetration Testing & Security Auditing

# LHT Service Account Security Assessment Template

---

# Document Information

| Field | Value |
|--------|-------|
| Document ID | LHT-Assessment-005 |
| Assessment Area | Service Account Security |
| Assessment Type | Active Directory Identity Security Assessment |
| Evidence Classification | Proposed / Collected / Validated / Remediated |
| Version | 1.0 |
| Assessment Status | Planned |
| Security Assessor | Bassey Solomon Henry |
| Reviewer | Lighthouse Technology Security Team |
| Repository | Enterprise Security Evolution |

---

# 1. Assessment Objective

Assess the security posture of enterprise service accounts within the authorized Lighthouse Technology Active Directory laboratory.

The assessment evaluates service account lifecycle management, privilege assignment, credential protection, authentication dependencies, delegation configuration, ownership, monitoring coverage, and remediation opportunities.

The objective is to identify service account risks that may increase credential exposure, privilege escalation opportunities, or unauthorized access pathways.

---

# 2. Assessment Scope

The assessment includes:

- Domain service accounts
- Local service accounts
- Managed Service Accounts (MSA)
- Group Managed Service Accounts (gMSA)
- Application service identities
- Database service identities
- Scheduled task accounts
- Windows service accounts
- Privileged service accounts
- Tier Zero service accounts

---

# 3. Authorization Boundary

All assessment activities are restricted to the authorized Lighthouse Technology Active Directory laboratory.

The assessment focuses on:

- Identity inventory
- Configuration review
- Evidence collection
- Security validation
- Detection validation
- Risk analysis

No unauthorized credential access or service disruption activities are permitted.

---

# 4. Assessment Methodology

The service account assessment follows this workflow:

1. Identify service account inventory.
2. Map service accounts to systems and applications.
3. Review ownership and business purpose.
4. Analyze privileges.
5. Review credential management.
6. Assess authentication dependencies.
7. Review Kerberos configuration.
8. Review delegation settings.
9. Validate monitoring coverage.
10. Prioritize remediation.

---

# 5. Service Account Inventory Review

Document:

- Account name
- Account type
- Owner
- Business purpose
- Associated application
- Associated system
- Authentication protocol
- Privilege level
- Tier classification

---

# 6. Account Type Assessment

Evaluate:

## Standard Service Accounts

Review:

- Password management
- Ownership
- Privilege level
- Usage purpose

---

## Managed Service Accounts

Review:

- MSA deployment
- Credential automation
- Administrative management

---

## Group Managed Service Accounts

Review:

- gMSA adoption
- Password rotation
- Service compatibility
- Privileged usage

---

# 7. Credential Security Assessment

Evaluate:

- Password age
- Password expiration
- Manual password management
- Non-expiring passwords
- Credential ownership
- Shared account usage

Document:

| Account | Observation | Risk | Status |
|---------|-------------|------|--------|
| | | | |

---

# 8. Privilege Exposure Assessment

Review:

- Domain privileges
- Local administrator permissions
- Tier Zero access
- Group memberships
- Administrative roles
- Excessive permissions

Document:

| Account | Privilege | System | Risk |
|---------|-----------|--------|------|
| | | | |

---

# 9. Kerberos Dependency Review

Assess:

- Service Principal Names (SPNs)
- Encryption type
- Authentication protocol
- Ticket dependencies
- Service authentication paths

---

# 10. Delegation Assessment

Review:

- Unconstrained delegation
- Constrained delegation
- Resource-Based Constrained Delegation
- Business justification
- Approval status

Document:

| Account | Delegation Type | Target | Risk |
|---------|-----------------|--------|------|
| | | | |

---

# 11. Interactive Logon Assessment

Evaluate:

- Interactive logon permissions
- Remote access permissions
- Administrative usage
- Human account replacement opportunities

---

# 12. Evidence Sources

Potential evidence sources:

- Active Directory PowerShell Module
- Windows Security Event Logs
- Sysmon
- Splunk Enterprise
- Group Policy Reports
- ADRecon
- PingCastle
- BloodHound Community Edition
- LHT-ServiceAccount-Normalized.csv

---

# 13. Evidence Collection Register

| Evidence ID | Source | Collection Method | Status |
|-------------|--------|------------------|--------|
| LHT-Evidence-### | | | Proposed |

---

# 14. Service Account Findings

| Finding ID | Description | Risk | Evidence | Status |
|------------|-------------|------|----------|--------|
| LHT-Finding-### | | | | Proposed |

---

# 15. Detection Validation

Assess detection coverage for:

- Service account authentication
- Privileged service activity
- Abnormal authentication behavior
- Service account misuse indicators
- Delegation-related activity

Document:

| Detection ID | Telemetry Source | Coverage | Result |
|--------------|------------------|----------|--------|
| LHT-Detection-### | | | |

---

# 16. MITRE ATT&CK Mapping

Document applicable techniques:

| Finding | ATT&CK Technique | Validation |
|---------|------------------|------------|
| | | |

Potential categories:

- Credential Access
- Persistence
- Privilege Escalation
- Lateral Movement

---

# 17. Risk Assessment

Evaluate:

## Identity Risk

- Privilege level
- Credential sensitivity
- Authentication exposure

## Operational Risk

- Business dependency
- Service availability impact

## Security Risk

- Attack path contribution
- Detection maturity
- Remediation complexity

---

# 18. Remediation Strategy

Recommendations may include:

## Credential Management

- Implement gMSA where appropriate
- Rotate service credentials
- Remove shared credentials

---

## Privilege Reduction

- Remove unnecessary administrative permissions
- Apply least privilege
- Enforce tier separation

---

## Governance Improvements

- Assign ownership
- Document business purpose
- Review lifecycle regularly

---

# 19. Validation After Remediation

Confirm:

- Ownership documented
- Credentials managed securely
- Privileges reduced
- Delegation reviewed
- Monitoring improved
- Risk score reduced

---

# 20. Deliverables Produced

- Service Account Security Assessment
- Service Account Normalized Dataset
- Privilege Exposure Updates
- Attack Path Analysis Inputs
- Detection Coverage Updates
- Risk Register Updates
- Remediation Recommendations

---

# 21. Cross-Domain Integration

## Domain 1 — SOC Operations

Integration:

- Authentication telemetry
- Splunk detections
- Windows Event Logs
- Sysmon visibility

---

## Domain 2 — Purple Team Operations

Integration:

- Identity attack-path validation
- ATT&CK mapping
- Detection validation

---

## Domain 3 — Infrastructure Security

Integration:

- Windows servers
- Applications
- SMB
- LDAP
- Kerberos dependencies

---

## Domain 4 — Governance & Risk

Integration:

- Identity governance
- Risk scoring
- Evidence lineage
- Executive reporting

---

# 22. Assessment Status

| Stage | Status |
|--------|--------|
| Planning | Complete |
| Inventory Collection | Pending |
| Credential Review | Pending |
| Privilege Review | Pending |
| Validation | Pending |
| Detection Review | Pending |
| Remediation | Pending |
| Executive Reporting | Pending |

---

# Document Control

This template establishes a repeatable service account security assessment framework for Domain 5.

It connects service account inventory, credential governance, privilege exposure, Kerberos dependencies, delegation analysis, telemetry validation, and remediation 
engineering into an evidence-driven identity security workflow.

The completed assessment supports enterprise identity hardening, attack-path reduction, and executive-level security risk communication.
