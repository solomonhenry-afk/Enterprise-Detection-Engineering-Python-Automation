# Lighthouse Technology Detection Engineering Coverage Assessment Template

# Detection Coverage Assessment Report

---

# Document Information

| Field | Value |
|---|---|
| Assessment ID | LHT-COVERAGE-ASSESS-001 |
| Detection Coverage ID | COV-001 |
| Assessment Name | Enterprise Detection Coverage Assessment |
| Assessment Type | Detection Engineering Coverage Measurement |
| Version | 1.0 |
| Assessment Date | 2026-07-22 |
| Analyst | Lighthouse Technology Detection Engineering Team |
| Reviewer | Enterprise Security Governance Team |
| Status | Approved |
| Classification | Internal Security Engineering Documentation |

---

# 1. Assessment Overview

## 1.1 Purpose

This assessment measures the effectiveness and completeness of Lighthouse Technology's detection engineering capability across enterprise security domains.

The objective is to determine:

- Which adversary behaviors are detectable.
- Which MITRE ATT&CK techniques have monitoring coverage.
- Where telemetry gaps exist.
- Where additional detection engineering investment is required.
- How effectively security operations can identify attacker activity.

---

# 2. Coverage Objective

## Business Security Objective

| Area | Description |
|---|---|
| Threat Visibility | Maintain continuous visibility into adversary behavior |
| Detection Capability | Identify malicious activity across enterprise environments |
| Risk Reduction | Reduce attacker dwell time and business impact |
| Security Operations | Improve SOC investigation effectiveness |

---

# 3. Coverage Scope

## Assessment Domains

| Domain | Coverage Area | Status |
|---|---|---|
| Endpoint Security | Process and execution monitoring | Active |
| Identity Security | Authentication and privilege monitoring | Active |
| Network Security | Communication and lateral movement monitoring | Active |
| Active Directory | Domain attack detection | Active |
| Cloud Security | Cloud audit monitoring | Planned |

---

# 4. MITRE ATT&CK Coverage Mapping

| ATT&CK ID | Technique | Detection Status | Coverage Level |
|---|---|---|---|
| T1059.001 | PowerShell | Covered | Full |
| T1110 | Brute Force | Covered | Full |
| T1558.003 | Kerberoasting | Covered | Partial |
| T1078 | Valid Accounts | Covered | Partial |
| T1021 | Remote Services | Covered | Partial |
| T1003.006 | DCSync | Under Development | Limited |
| T1098 | Account Manipulation | Covered | Full |

---

# 5. Detection Coverage Matrix

| Detection ID | Detection Name | Data Source | ATT&CK Coverage | Status |
|---|---|---|---|---|
| DET-001 | Suspicious PowerShell Execution | Sysmon / PowerShell Logs | T1059.001 | Active |
| DET-002 | Authentication Brute Force | Windows Security Logs | T1110 | Active |
| DET-003 | Kerberoasting Detection | Kerberos Logs | T1558.003 | Active |
| DET-004 | Privileged Group Modification | AD Audit Logs | T1098 | Active |
| DET-005 | Valid Account Abuse | Authentication Logs | T1078 | Active |

---

# 6. Telemetry Coverage Assessment

## Required Telemetry

| Telemetry Source | Available | Quality |
|---|---|---|
| Windows Security Logs | Yes | High |
| Sysmon Logs | Yes | High |
| PowerShell Logs | Yes | High |
| Active Directory Audit Logs | Yes | Medium |
| Network Telemetry | Partial | Medium |
| Cloud Audit Logs | Planned | Low |

---

# 7. Detection Gap Analysis

## Identified Gaps

| Gap ID | Description | Risk | Priority |
|---|---|---|---|
| GAP-001 | Limited cloud workload visibility | High | High |
| GAP-002 | Incomplete lateral movement detection | Medium | Medium |
| GAP-003 | Missing advanced behavioral analytics | Medium | Medium |
| GAP-004 | Limited automated enrichment | Low | Low |

---

# 8. Coverage Scoring

## Coverage Calculation

| Metric | Result |
|---|---|
| Total ATT&CK Techniques Assessed | 50 |
| Fully Covered Techniques | 32 |
| Partially Covered Techniques | 12 |
| Missing Coverage | 6 |
| Overall Coverage Score | 76% |

---

# 9. Detection Maturity Assessment

| Capability | Maturity Level |
|---|---|
| Detection Development | Level 4 - Managed |
| MITRE ATT&CK Mapping | Level 4 - Managed |
| Telemetry Management | Level 3 - Defined |
| Detection Validation | Level 4 - Managed |
| Continuous Improvement | Level 3 - Defined |

---

# 10. Purple Team Validation Alignment

## Validation Mapping

| Simulation ID | Technique Tested | Detection Result |
|---|---|---|
| SIM-001 | PowerShell Execution | Pass |
| SIM-002 | Authentication Attack | Pass |
| SIM-003 | Kerberoasting | Pass |
| SIM-004 | Privilege Escalation | Pass |

---

# 11. Coverage Improvement Recommendations

## Immediate Actions

1. Expand endpoint telemetry collection.
2. Increase Active Directory attack detection coverage.
3. Validate missing ATT&CK techniques through simulation.

---

## Long-Term Actions

1. Integrate additional behavioral analytics.
2. Expand cloud detection capabilities.
3. Automate ATT&CK coverage reporting.
4. Implement continuous purple-team validation.

---

# 12. Coverage Evidence Register

| Evidence ID | Description | Location | Status |
|---|---|---|---|
| EVD-COV-001 | ATT&CK Coverage Matrix | evidence/validation/coverage/ | Verified |
| EVD-COV-002 | Detection Mapping Report | evidence/validation/coverage/ | Verified |
| EVD-COV-003 | Telemetry Assessment Results | evidence/validation/coverage/ | Verified |

---

# 13. Governance Approval

| Role | Name | Date | Approval |
|---|---|---|---|
| Detection Engineer | Lighthouse Technology Security Engineering Team | 2026-07-22 | Approved |
| Security Lead | Enterprise Security Governance Team | 2026-07-22 | Approved |
| Reviewer | Security Architecture Review Board | 2026-07-22 | Approved |

---

# Appendix A: References

| Artifact | Location |
|---|---|
| Detection Coverage Dataset | data/normalized/detection/LHT-DetectionCoverage-Normalized.csv |
| ATT&CK Coverage Dataset | data/normalized/detection/LHT-ATTACKCoverage-Normalized.csv |
| Detection Metadata | data/normalized/detection/LHT-DetectionMetadata.csv |
| Detection Rules | data/normalized/detection/LHT-DetectionRules-Normalized.csv |
| Detection Assessment | templates/detection/LHT-Detection-Assessment-Template.md |
| Purple Team Validation | templates/validation/LHT-PurpleTeam-Assessment-Template.md |

---

# Appendix B: Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-07-22 | Initial enterprise detection coverage assessment template creation | Lighthouse Technology Security Engineering Team |
