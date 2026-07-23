# Lighthouse Technology – Detection Validation Assessment Report

**Template ID:** LHT-DV-AT-001  
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
| Validation ID | |
| Detection Validation ID | |
| Detection Rule ID | |
| Detection Name | |
| Detection Category | |
| SIEM Platform | Splunk Enterprise |
| Assessment Date | |
| Assessment Status | Proposed / In Progress / Completed |
| Security Assessor | Bassey Solomon Henry |
| Reviewer | Lighthouse Technology Security Team |

---

# Executive Summary

## Purpose

This assessment validates whether the selected detection rule successfully identifies the intended adversary behavior during an authorized Purple Team exercise.

The assessment evaluates:

- Detection accuracy
- Alert generation
- Telemetry quality
- ATT&CK alignment
- False positives
- False negatives
- Detection tuning opportunities

---

# Detection Overview

| Attribute | Value |
|-----------|-------|
| Detection Name | |
| Detection Rule ID | |
| Detection Type | |
| Detection Objective | |
| Detection Logic | |
| Security Control | |
| Priority | |

---

# Threat Scenario

## Scenario Description

Document the simulated adversary activity that should trigger the detection.

---

## Target Systems

| Asset | Hostname | Criticality |
|--------|----------|-------------|
| | | |

---

## Target Identity

| Account | Account Type | Privilege Level |
|----------|--------------|-----------------|
| | | |

---

# ATT&CK Mapping

| ATT&CK Tactic | Technique ID | Technique |
|--------------|--------------|-----------|
| | | |

---

# Detection Logic

## Data Sources

- Windows Security Logs
- Sysmon
- PowerShell Logs
- Splunk Universal Forwarder
- Active Directory Logs
- Firewall Logs
- DNS Logs
- Authentication Logs

---

## Detection Conditions

Describe:

- Required events
- Event sequence
- Thresholds
- Correlation logic
- Time windows

---

# Telemetry Validation

| Telemetry Source | Status | Quality | Notes |
|-----------------|--------|---------|-------|
| Sysmon | | | |
| Windows Event Logs | | | |
| Splunk | | | |
| Authentication Logs | | | |

---

# Expected Results

Document:

- Expected alerts
- Expected Event IDs
- Expected log sources
- Expected ATT&CK mapping
- Expected analyst visibility

---

# Validation Results

| Validation Item | Result |
|-----------------|--------|
| Alert Generated | |
| Detection Triggered | |
| Telemetry Captured | |
| ATT&CK Mapped | |
| Investigation Enabled | |

---

# Detection Quality Assessment

| Metric | Result |
|--------|--------|
| Detection Accuracy | |
| Detection Confidence | |
| False Positive Rate | |
| False Negative Rate | |
| Rule Performance | |
| Coverage Rating | |

---

# Evidence Collected

| Evidence ID | Evidence Type | Repository |
|-------------|---------------|------------|
| | | |

---

# Findings

## Finding

### Description

---

### Supporting Evidence

---

### Business Risk

---

### Recommendation

---

# Detection Tuning Recommendations

Document improvements including:

- Threshold adjustments
- Correlation improvements
- Additional telemetry
- Rule optimization
- Alert enrichment
- Noise reduction

---

# Risk Assessment

| Risk | Severity | Priority |
|------|----------|----------|
| | | |

---

# Related Artifacts

## Normalized Datasets

- LHT-DetectionValidation-Normalized.csv
- LHT-Telemetry-Normalized.csv
- LHT-DetectionCoverage-Normalized.csv
- LHT-PurpleTeam-Normalized.csv

---

## Supporting Documentation

- Purple-Team-Validation-Methodology.md
- Detection-Validation-Workflow.md
- Evidence-Correlation-Methodology.md
- Telemetry-Collection-Runbook.md

---

# Lessons Learned

Document:

- Detection strengths
- Detection weaknesses
- Coverage gaps
- Engineering improvements
- Future validation opportunities

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

This report maps directly to my Phase F data model:

LHT-DetectionValidation-Normalized.csv → Core validation record.
LHT-Telemetry-Normalized.csv → Confirms required logs and events were generated.
LHT-DetectionCoverage-Normalized.csv → Measures detection effectiveness and ATT&CK coverage.
LHT-PurpleTeam-Normalized.csv → Links the validation back to the overall Purple Team exercise.

It also reflects the workflow used by mature Detection Engineering teams: simulate → observe telemetry → validate detections → tune rules → measure coverage → 
document findings, making it a strong portfolio artifact for Security Engineer, Detection Engineer, Purple Team, and MSSP roles.
