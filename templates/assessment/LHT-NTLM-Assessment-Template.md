# Lighthouse Technology

# Enterprise Security Evolution

## Domain 5 — Enterprise Active Directory Penetration Testing & Security Auditing

# LHT NTLM Exposure Assessment Template

---

# Document Information

| Field | Value |
|--------|-------|
| Document ID | LHT-Assessment-004 |
| Assessment Area | NTLM Exposure Security |
| Assessment Type | Active Directory Authentication Assessment |
| Evidence Classification | Proposed / Collected / Validated / Remediated |
| Version | 1.0 |
| Assessment Status | Planned |
| Security Assessor | Bassey Solomon Henry |
| Reviewer | Lighthouse Technology Security Team |
| Repository | Enterprise Security Evolution |

---

# 1. Assessment Objective

Assess the security exposure associated with NTLM authentication within the authorized Lighthouse Technology Active Directory laboratory.

The assessment evaluates where NTLM is used, why dependencies exist, whether security controls are applied, whether monitoring is available, and whether migration opportunities exist toward stronger authentication mechanisms.

The objective is to identify legacy authentication risks while supporting controlled enterprise modernization.

---

# 2. Assessment Scope

The assessment includes:

- NTLM authentication usage
- NTLM version configuration
- Legacy authentication dependencies
- SMB authentication
- LDAP authentication
- WinRM authentication
- Service account authentication
- User authentication scenarios
- Administrative authentication exposure
- Authentication policy configuration
- NTLM monitoring capability

---

# 3. Authorization Boundary

All assessment activities are restricted to the authorized Lighthouse Technology Active Directory laboratory.

Assessment activities are limited to:

- Configuration review
- Evidence collection
- Security validation
- Detection validation
- Risk assessment

No unauthorized credential testing or production authentication disruption activities are permitted.

---

# 4. Assessment Methodology

The NTLM assessment follows this workflow:

1. Identify NTLM authentication dependencies.
2. Collect authorized configuration evidence.
3. Normalize NTLM observations.
4. Review authentication context.
5. Evaluate legacy dependencies.
6. Assess security controls.
7. Validate monitoring coverage.
8. Map applicable ATT&CK techniques.
9. Prioritize remediation opportunities.
10. Validate improvements.

---

# 5. NTLM Architecture Review

Document:

- Domain authentication architecture
- Systems supporting NTLM
- Applications requiring NTLM
- Trust relationships
- Administrative authentication paths

---

# 6. NTLM Configuration Assessment

Review:

## NTLM Policy Controls

Evaluate:

- NTLM restriction settings
- Domain policy configuration
- Local security policies
- Authentication exceptions

Assessment Record:

| Configuration | Evidence | Status |
|---------------|----------|--------|
| | | |

---

# 7. NTLM Usage Assessment

Identify:

- Authentication sources
- Authentication targets
- Business applications
- Legacy systems
- Service dependencies

Document:

| Source | Target | Protocol Context | Risk |
|--------|--------|------------------|------|
| | | | |

---

# 8. Protocol Dependency Review

Assess NTLM usage within:

## SMB

Review:

- File services
- Administrative access
- Legacy compatibility requirements

---

## LDAP

Review:

- Directory authentication
- Secure LDAP availability
- Signing requirements

---

## WinRM

Review:

- Remote management authentication
- Administrative access requirements

---

# 9. Credential Exposure Assessment

Evaluate:

- Credential reuse risk
- Administrative account exposure
- Legacy authentication dependencies
- Authentication relay exposure considerations
- Identity privilege impact

---

# 10. Evidence Sources

Potential evidence sources:

- Windows Security Event Logs
- Sysmon
- Splunk Enterprise
- Group Policy Reports
- Active Directory PowerShell Module
- Security Baseline Reports
- ADRecon
- LHT-NTLM-Normalized.csv

---

# 11. Evidence Collection Register

| Evidence ID | Source | Collection Method | Status |
|-------------|--------|------------------|--------|
| LHT-Evidence-### | | | Proposed |

---

# 12. NTLM Findings Register

| Finding ID | Description | Risk | Evidence | Status |
|------------|-------------|------|----------|--------|
| LHT-Finding-### | | | | Proposed |

---

# 13. Detection Validation

Assess detection capability for:

- NTLM authentication activity
- Excessive failed authentication
- Legacy authentication usage
- Privileged NTLM authentication
- Authentication anomalies

Document:

| Detection ID | Source | Coverage | Result |
|--------------|--------|----------|--------|
| LHT-Detection-### | | | |

---

# 14. MITRE ATT&CK Mapping

Map applicable observations:

| Finding | ATT&CK Technique | Validation |
|---------|------------------|------------|
| | | |

Potential categories:

- Credential Access
- Lateral Movement
- Defense Evasion

---

# 15. Risk Assessment

Evaluate:

## Likelihood

Consider:

- Authentication exposure
- System accessibility
- Credential sensitivity
- Legacy dependency

## Impact

Consider:

- Privileged identity exposure
- Lateral movement potential
- Business service impact

## Detection Capability

Consider:

- Logging availability
- Alert coverage
- Investigation readiness

---

# 16. Remediation Strategy

Recommendations may include:

## Immediate Improvements

- Identify unnecessary NTLM usage
- Restrict high-risk authentication paths
- Improve monitoring

## Long-Term Improvements

- Migrate applications to modern authentication
- Reduce legacy dependencies
- Increase Kerberos adoption
- Strengthen authentication governance

---

# 17. Validation After Remediation

Confirm:

- NTLM usage reduced where appropriate
- Business applications remain functional
- Authentication telemetry remains available
- Detection coverage improves
- Risk rating decreases

---

# 18. Deliverables Produced

- NTLM Exposure Assessment Report
- NTLM Normalized Dataset
- Evidence Register Updates
- Finding Register Updates
- Detection Coverage Analysis
- Authentication Risk Assessment
- Remediation Recommendations

---

# 19. Cross-Domain Integration

## Domain 1 — SOC Operations

Integration:

- Windows authentication logs
- Splunk detection engineering
- Authentication monitoring

---

## Domain 2 — Purple Team Operations

Integration:

- Controlled authentication validation
- Detection testing
- ATT&CK mapping

---

## Domain 3 — Infrastructure Security

Integration:

- SMB security
- LDAP security
- Network authentication paths
- Legacy system dependencies

---

## Domain 4 — Governance & Risk

Integration:

- Risk scoring
- Evidence lineage
- Control maturity
- Executive reporting

---

# 20. Assessment Status

| Stage | Status |
|--------|--------|
| Planning | Complete |
| Evidence Collection | Pending |
| NTLM Discovery | Pending |
| Validation | Pending |
| Detection Review | Pending |
| Risk Assessment | Pending |
| Remediation | Pending |
| Executive Reporting | Pending |

---

# Document Control

This template provides a repeatable framework for evaluating NTLM exposure within an enterprise Active Directory environment.

It ensures NTLM observations are analyzed through a complete security lifecycle:

- Discovery
- Evidence collection
- Normalization
- Validation
- Detection engineering
- Risk assessment
- Remediation planning

The resulting assessment supports identity modernization, authentication hardening, and enterprise security decision-making while preserving operational 
awareness of legitimate legacy dependencies.
