# Lighthouse Technology

# Enterprise Security Evolution

## Domain 5 — Enterprise Active Directory Penetration Testing & Security Auditing

# LHT Credential Security Assessment Template

---

## Document Information

| Field | Value |
|--------|-------|
| Document ID | LHT-Assessment-001 |
| Assessment Area | Credential Security |
| Assessment Type | Active Directory Security Assessment |
| Evidence Classification | Proposed / Collected / Validated / Remediated |
| Version | 1.0 |
| Assessment Status | Planned |
| Security Assessor | Bassey Solomon Henry |
| Reviewer | Self-Reviewed (Portfolio Project) |
| Repository | Enterprise Security Evolution |

---

# 1. Assessment Objective

Assess the security posture of enterprise credentials within the authorized Lighthouse Technology Active Directory laboratory by evaluating credential hygiene, password governance, authentication controls, privileged account protection, service account management, and credential-related attack surface.

The assessment is designed to identify identity security weaknesses, validate defensive controls, support detection engineering, and prioritize remediation activities using evidence-backed findings.

---

# 2. Assessment Scope

Include the following assessment areas:

- User account credential security
- Privileged account credential hygiene
- Service account credential management
- Password policy effectiveness
- Password expiration configuration
- Password age analysis
- Fine-Grained Password Policies (FGPP)
- LAPS deployment validation
- gMSA adoption review
- Legacy credential exposure
- NTLM authentication exposure
- Kerberos authentication configuration
- Credential storage risks
- Administrative credential separation
- Tier Zero credential protection

---

# 3. Authorization Boundary

This assessment applies exclusively to the authorized Lighthouse Technology enterprise laboratory.

Assessment activities shall remain within approved testing boundaries and shall not impact production systems or unauthorized environments.

---

# 4. Assessment Methodology

The assessment follows the Domain 5 methodology:

1. Define assessment objectives.
2. Collect authorized configuration evidence.
3. Normalize collected data.
4. Validate observations.
5. Assess credential exposure.
6. Identify identity risks.
7. Validate available detections.
8. Assign risk ratings.
9. Recommend remediation.
10. Reassess after remediation.

---

# 5. Evidence Sources

Potential evidence sources include:

- Active Directory PowerShell Module
- Windows Security Event Logs
- Sysmon
- Splunk Enterprise
- Group Policy Reports
- ADRecon
- PingCastle
- Purple Knight
- BloodHound Community Edition (graph analysis only)
- LHT Normalized Datasets

---

# 6. Assessment Activities

## Identity Review

Evaluate:

- User accounts
- Administrative accounts
- Service accounts
- Computer accounts
- Dormant accounts
- Disabled accounts

---

## Password Governance Review

Assess:

- Password length
- Password complexity
- Password history
- Password expiration
- Password reuse controls
- Fine-Grained Password Policies

---

## Credential Exposure Review

Assess:

- Non-expiring passwords
- Shared credentials
- Interactive service accounts
- Weak administrative practices
- Legacy authentication dependencies
- Credential reuse risks

---

## Authentication Review

Review:

- Kerberos configuration
- NTLM usage
- LAPS implementation
- gMSA implementation
- Privileged authentication controls

---

# 7. Evidence Collection Register

| Evidence ID | Evidence Source | Collection Method | Status |
|-------------|----------------|-------------------|--------|
| LHT-Evidence-### | | | Proposed |

---

# 8. Assessment Findings

| Finding ID | Description | Risk | Evidence | Status |
|------------|-------------|------|----------|--------|
| LHT-Finding-### | | | | Proposed |

---

# 9. Detection Validation

For each credential-related finding document:

- Detection availability
- Windows Event IDs
- Sysmon telemetry
- Splunk visibility
- Detection gaps
- False-positive considerations
- Validation status

---

# 10. MITRE ATT&CK Mapping

Document applicable techniques associated with credential security observations.

| Finding | ATT&CK Technique | Validation Status |
|----------|------------------|-------------------|
| | | |

---

# 11. Risk Assessment

Evaluate each observation using the Domain 5 risk methodology.

Consider:

- Likelihood
- Identity exposure
- Privilege level
- Business impact
- Detection maturity
- Remediation effort

---

# 12. Remediation Plan

For every finding document:

- Immediate remediation
- Long-term remediation
- Detection improvements
- Governance improvements
- Validation requirements
- Responsible owner

---

# 13. Validation Checklist

- [ ] Assessment completed
- [ ] Scope confirmed
- [ ] Evidence collected
- [ ] Evidence normalized
- [ ] Findings validated
- [ ] Detection reviewed
- [ ] MITRE mapping completed
- [ ] Risk scored
- [ ] Remediation documented
- [ ] Executive summary updated

---

# 14. Deliverables Produced

- Credential Security Assessment
- Normalized Authentication Dataset
- Evidence Register
- Finding Register
- Detection Coverage Updates
- Risk Register Updates
- Remediation Recommendations
- Executive Reporting Inputs

---

# 15. Cross-Domain Integration

## Domain 1

- Splunk telemetry
- Windows Event Logs
- Sysmon
- Detection engineering

## Domain 2

- Purple Team validation
- MITRE ATT&CK mapping
- Detection validation

## Domain 3

- Active Directory infrastructure
- DNS
- SMB
- LDAP
- Network segmentation

## Domain 4

- Risk scoring
- Governance
- Evidence lineage
- Executive reporting
- Control validation

---

# 16. Assessment Status

| Stage | Status |
|--------|--------|
| Planning | Complete |
| Evidence Collection | Pending |
| Validation | Pending |
| Detection Review | Pending |
| Risk Assessment | Pending |
| Remediation | Pending |
| Executive Reporting | Pending |

---

# Document Control

This template supports the standardized execution of credential security assessments throughout Domain 5. 
It provides a repeatable framework for evidence collection, technical validation, detection engineering, governance alignment, and 
remediation planning while maintaining traceability to normalized datasets and enterprise reporting artifacts.
