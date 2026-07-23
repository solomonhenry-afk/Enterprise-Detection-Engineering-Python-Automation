# Lighthouse Technology MITRE ATT&CK Detection Coverage Report

## Enterprise Adversary Technique Visibility Assessment

---

# Document Information

| Field | Value |
|---|---|
| Assessment ID | LHT-ATTACK-COVERAGE-001 |
| Report Name | MITRE ATT&CK Detection Coverage Report |
| Report Type | Adversary Technique Coverage Assessment |
| Assessment Type | Detection Engineering Coverage Measurement |
| Version | 1.0 |
| Assessment Date | 2026-07-22 |
| Analyst | Lighthouse Technology Detection Engineering Team |
| Reviewer | Enterprise Security Governance Team |
| Status | Approved |
| Classification | Internal Security Engineering Documentation |

---

# 1. Executive Summary

## Overview

This report evaluates Lighthouse Technology's detection capability against adversary behaviors mapped to the MITRE ATT&CK framework.

The purpose of this assessment is to measure:

- Detection visibility across attacker techniques.
- Coverage effectiveness against enterprise attack paths.
- Telemetry readiness.
- Detection engineering maturity.
- Purple-team validation results.

The assessment connects:
MITRE ATT&CK Technique
|
↓
Detection Use Case
|
↓
Sigma Rule
|
↓
SIEM Detection
|
↓
Validation Simulation
|
↓
Coverage Measurement


---

# 2. Assessment Objectives

The objectives are:

1. Identify ATT&CK techniques with active detection coverage.
2. Measure detection maturity by adversary behavior.
3. Identify coverage gaps.
4. Prioritize detection engineering improvements.
5. Support continuous security validation.

---

# 3. Scope

## ATT&CK Domains Assessed

| Domain | Included |
|---|---|
| Enterprise Techniques | Yes |
| Identity Attacks | Yes |
| Endpoint Execution | Yes |
| Credential Access | Yes |
| Privilege Escalation | Yes |
| Persistence | Yes |
| Lateral Movement | Yes |
| Command and Control | Partial |
| Cloud Techniques | Planned |

---

# 4. ATT&CK Coverage Summary

| Metric | Result |
|---|---|
| Total Techniques Reviewed | 50 |
| Fully Covered Techniques | 32 |
| Partially Covered Techniques | 12 |
| Missing Coverage | 6 |
| Overall Coverage Score | 76% |

---

# 5. Technique Coverage Matrix

| Technique ID | Technique Name | Tactic | Detection Status | Coverage Level |
|---|---|---|---|---|
| T1059.001 | PowerShell | Execution | Active | Full |
| T1059.003 | Windows Command Shell | Execution | Active | Partial |
| T1110 | Brute Force | Credential Access | Active | Full |
| T1558.003 | Kerberoasting | Credential Access | Active | Full |
| T1003.006 | DCSync | Credential Access | Development | Limited |
| T1078 | Valid Accounts | Defense Evasion | Active | Partial |
| T1021.001 | RDP | Lateral Movement | Active | Partial |
| T1021.002 | SMB/Windows Admin Shares | Lateral Movement | Development | Limited |
| T1098 | Account Manipulation | Persistence | Active | Full |
| T1053 | Scheduled Task/Job | Persistence | Partial | Medium |

---

# 6. Detection Mapping

| Detection ID | Detection Name | ATT&CK Technique | Status |
|---|---|---|---|
| DET-001 | Suspicious PowerShell Execution | T1059.001 | Validated |
| DET-002 | Authentication Brute Force | T1110 | Validated |
| DET-003 | Kerberos Service Ticket Abuse | T1558.003 | Validated |
| DET-004 | Privileged Account Modification | T1098 | Validated |
| DET-005 | Remote Access Abuse Detection | T1021 | Developing |

---

# 7. Adversary Simulation Alignment

## Purple-Team Validation Results

| Simulation ID | Technique Tested | Detection Result |
|---|---|---|
| SIM-001 | PowerShell Execution | PASS |
| SIM-002 | Credential Attack Simulation | PASS |
| SIM-003 | Kerberos Abuse Simulation | PASS |
| SIM-004 | Privilege Escalation Simulation | PASS |
| SIM-005 | Lateral Movement Simulation | PARTIAL |

---

# 8. Coverage by ATT&CK Tactic

| Tactic | Coverage |
|---|---|
| Initial Access | 70% |
| Execution | 90% |
| Persistence | 75% |
| Privilege Escalation | 80% |
| Defense Evasion | 70% |
| Credential Access | 85% |
| Discovery | 60% |
| Lateral Movement | 65% |
| Collection | 50% |
| Command and Control | 45% |

---

# 9. Coverage Gaps

## Identified Gaps

| Gap ID | ATT&CK Area | Description | Risk |
|---|---|---|---|
| ATTACK-GAP-001 | Discovery | Limited host discovery detection | Medium |
| ATTACK-GAP-002 | Lateral Movement | SMB abuse visibility improvement required | High |
| ATTACK-GAP-003 | Cloud | Cloud ATT&CK coverage incomplete | High |
| ATTACK-GAP-004 | Collection | Data access monitoring requires expansion | Medium |

---

# 10. Detection Engineering Recommendations

## Immediate Actions

- Increase lateral movement detection.
- Expand Active Directory attack coverage.
- Improve discovery technique visibility.
- Validate missing ATT&CK mappings.

---

## Strategic Actions

- Build automated ATT&CK coverage dashboards.
- Integrate threat intelligence.
- Expand cloud detection engineering.
- Implement continuous adversary simulation.

---

# 11. Coverage Measurement Model

## Coverage Classification

| Level | Definition |
|---|---|
| Full | Detection exists and validated through simulation |
| Partial | Detection exists but requires improvement |
| Limited | Detection exists with insufficient validation |
| Missing | No detection capability available |

---

# 12. Business Impact Assessment

Improved ATT&CK coverage enables:

## Reduced Risk

- Earlier attacker identification.
- Reduced attack dwell time.
- Improved incident containment.

## Operational Benefits

- Better SOC investigation workflows.
- Increased analyst confidence.
- Improved security prioritization.

## Governance Benefits

- Measurable security effectiveness.
- Evidence-based investment decisions.
- Executive visibility.

---

# 13. Evidence References

| Artifact | Location |
|---|---|
| ATT&CK Coverage Dataset | data/normalized/detection/LHT-ATTACKCoverage-Normalized.csv |
| Detection Coverage Dataset | data/normalized/detection/LHT-DetectionCoverage-Normalized.csv |
| Detection Rules Dataset | data/normalized/detection/LHT-DetectionRules-Normalized.csv |
| Purple-Team Validation | data/normalized/validation/LHT-PurpleTeam-Normalized.csv |
| Attack Simulation Dataset | data/normalized/validation/LHT-AttackSimulation-Normalized.csv |
| Detection Evidence Register | templates/detection/LHT-Detection-Evidence-Register.csv |

---

# Appendix A: ATT&CK Coverage Categories

| Category | Description |
|---|---|
| Execution | Ability to identify attacker code execution |
| Credential Access | Ability to detect credential theft attempts |
| Persistence | Ability to detect attacker persistence mechanisms |
| Privilege Escalation | Ability to detect privilege abuse |
| Lateral Movement | Ability to detect internal movement |
| Defense Evasion | Ability to detect attacker concealment |

---

# Appendix B: Change History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-07-22 | Initial MITRE ATT&CK Detection Coverage Report creation | Lighthouse Technology Security Engineering Team |


NOTE: Phase G reporting layer now becomes:

reports/detection/
├── Detection-Coverage-Assessment.md
├── Detection-Maturity-Assessment.md
└── ATTACK-Coverage-Report.md

This report is the artifact that demonstrates adversary-informed detection engineering, connecting:

Task 2 Adversary Simulation
            ↓
MITRE ATT&CK Techniques
            ↓
Detection Engineering
            ↓
Validation Evidence
            ↓
Coverage Measurement
            ↓
Executive Security Reporting
