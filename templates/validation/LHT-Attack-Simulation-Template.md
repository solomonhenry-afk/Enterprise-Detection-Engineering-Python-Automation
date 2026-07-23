# Lighthouse Technology – Attack Simulation Assessment Report

**Template ID:** LHT-AS-AT-001 
**Project:** Enterprise Security Evolution 
**Domain:** Domain 5 – Enterprise Active Directory Penetration Testing & Security Auditing 
**Phase:** Phase F – Safe Purple Team Validation 
**Classification:** Internal Use 
**Version:** 1.0

---

# Assessment Information

| Field | Value |
|---------|-------|
| Assessment ID | |
| Simulation ID | |
| Purple Team Exercise ID | |
| Assessment Name | |
| Assessment Date | |
| Assessment Status | Proposed / In Progress / Completed |
| Security Assessor | Bassey Solomon Henry |
| Reviewer | Lighthouse Technology Security Team |

---

# Executive Summary

## Purpose

This assessment documents the planning, execution, and validation of an authorized attack simulation performed within the Lighthouse Technology Enterprise Security Evolution laboratory.

The objective is to safely emulate adversary behavior to evaluate:

- Security monitoring effectiveness
- Detection engineering quality
- Telemetry collection
- Incident visibility
- ATT&CK coverage
- Security control effectiveness
- Remediation opportunities

---

# Simulation Scope

## Objective

Document the business and security objective of the simulation.

---

## Target Environment

| Asset | Hostname | Operating System | Criticality |
|--------|----------|------------------|-------------|
| | | | |

---

## Target Accounts

| Account | Type | Privilege |
|----------|------|-----------|
| | | |

---

## Included Security Controls

| Control | Status |
|----------|--------|
| Active Directory | |
| Authentication Monitoring | |
| Splunk SIEM | |
| Sysmon | |
| Windows Event Logs | |
| Firewall | |
| Suricata IDS | |
| DNS Logging | |

---

# Attack Scenario

## Scenario Description

Provide a detailed description of the simulated adversary activity.

---

## Simulation Category

- Initial Access
- Execution
- Persistence
- Privilege Escalation
- Credential Access
- Discovery
- Lateral Movement
- Defense Evasion
- Collection
- Command and Control
- Exfiltration

---

# MITRE ATT&CK Mapping

| ATT&CK Tactic | Technique ID | Technique |
|--------------|--------------|-----------|
| | | |

---

# Preconditions

Document:

- Required configurations
- Test accounts
- Target systems
- Logging enabled
- Detection rules enabled
- Safety controls verified

---

# Safety Controls

| Control | Status |
|----------|--------|
| Written Authorization | |
| Laboratory Environment | |
| Production Isolation | |
| Snapshot Available | |
| Rollback Plan | |
| Data Protection Verified | |
| Recovery Procedures Tested | |

---

# Simulation Execution

| Step | Description | Expected Outcome | Result |
|------|-------------|------------------|--------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |

---

# Telemetry Generated

| Source | Event Type | Collected |
|---------|------------|-----------|
| Sysmon | | |
| Windows Security Logs | | |
| Splunk | | |
| Active Directory | | |
| Kerberos | | |
| NTLM | | |
| DNS | | |
| Firewall | | |

---

# Detection Results

| Detection Rule | Expected | Observed | Status |
|----------------|----------|----------|--------|
| | | | |

---

# Evidence Collected

| Evidence ID | Evidence Type | Repository |
|-------------|---------------|------------|
| | | |

---

# Findings

## Finding ID

### Description

---

### Supporting Evidence

---

### Security Impact

---

### Recommendation

---

# Control Effectiveness

| Security Control | Rating | Notes |
|------------------|--------|-------|
| Authentication Controls | | |
| Identity Monitoring | | |
| Endpoint Monitoring | | |
| Network Monitoring | | |
| Detection Engineering | | |
| Logging | | |

---

# Lessons Learned

Document:

- Successful detections
- Missed detections
- Telemetry gaps
- Process improvements
- Engineering recommendations
- Future simulation opportunities

---

# Risk Assessment

| Risk | Severity | Priority |
|------|----------|----------|
| | | |

---

# Related Normalized Datasets

- LHT-AttackSimulation-Normalized.csv
- LHT-PurpleTeam-Normalized.csv
- LHT-Telemetry-Normalized.csv
- LHT-DetectionValidation-Normalized.csv
- LHT-DetectionCoverage-Normalized.csv
- LHT-Validation-Metadata.csv

---

# Supporting Documentation

- Purple-Team-Validation-Methodology.md
- Validation-Safety-Standard.md
- Detection-Validation-Workflow.md
- Telemetry-Collection-Runbook.md
- Evidence-Correlation-Methodology.md

---

# Assessment Conclusion

Summarize whether the simulated attack achieved its objective, evaluate the effectiveness of security controls and detections, identify residual risks, and outline the next engineering actions required to strengthen enterprise security.

---

# Assessment Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Security Assessor | Bassey Solomon Henry | | |
| Reviewer | Lighthouse Technology Security Team | | |

---

# Document Control

| Version | Date | Author | Change Summary |
|----------|------|--------|----------------|
| 1.0 | | Bassey Solomon Henry | Initial template |

---


This template document the execution of an authorized attack simulation. Unlike the Detection Validation or Coverage templates, its primary purpose is to 
define what was simulated, why it was simulated, how it was executed safely, and what evidence was generated.

It becomes the source artifact that feeds:

LHT-PurpleTeam-Normalized.csv
LHT-AttackSimulation-Normalized.csv
LHT-Telemetry-Normalized.csv
LHT-DetectionValidation-Normalized.csv
LHT-DetectionCoverage-Normalized.csv

Attack Simulation
        │
        ▼
Telemetry Collection
        │
        ▼
Detection Validation
        │
        ▼
Coverage Measurement
        │
        ▼
Evidence Correlation
        │
        ▼
Executive Reporting

This template serves as the entry point for every Purple Team exercise:

- Plan the simulation with defined scope, objectives, and safety controls.
- Execute the authorized attack scenario in the lab.
- Capture telemetry from Sysmon, Windows Event Logs, Active Directory, Splunk, Suricata, and network controls.
- Validate detections and correlate evidence across telemetry sources.
- Measure ATT&CK coverage, detection performance, and control effectiveness.
- Document findings, lessons learned, and remediation recommendations.

This mirrors the workflow used by enterprise Purple Teams and MSSPs, reinforcing the evidence-driven 
methodology that runs consistently through my Enterprise Security Evolution portfolio.
