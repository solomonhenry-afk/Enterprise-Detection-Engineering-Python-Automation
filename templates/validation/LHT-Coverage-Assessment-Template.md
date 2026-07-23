# Lighthouse Technology – Detection Coverage Assessment Report

**Template ID:** LHT-CA-AT-001 
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
| Coverage Assessment ID | |
| Validation ID | |
| Assessment Date | |
| Assessment Status | Proposed / In Progress / Completed |
| Security Assessor | Bassey Solomon Henry |
| Reviewer | Lighthouse Technology Security Team |

---

# Executive Summary

## Purpose

This assessment evaluates the effectiveness of security monitoring by measuring detection coverage across enterprise assets, security controls, telemetry sources, and MITRE ATT&CK techniques.

The objective is to determine whether security monitoring provides sufficient visibility to detect, investigate, and respond to simulated adversary activity while identifying detection gaps requiring engineering improvements.

---

# Assessment Scope

## Included Assets

| Asset | Criticality | Coverage Status |
|--------|-------------|-----------------|
| | | |

---

## Included Security Controls

| Control | Status |
|----------|--------|
| Active Directory Monitoring | |
| Authentication Monitoring | |
| Sysmon | |
| Windows Event Logs | |
| Splunk SIEM | |
| Suricata IDS | |
| Firewall Logging | |
| DNS Logging | |
| PowerShell Logging | |

---

# Detection Inventory

| Detection ID | Detection Name | Status | Priority |
|--------------|----------------|--------|----------|
| | | | |

---

# Telemetry Coverage

| Telemetry Source | Available | Quality | Coverage |
|------------------|-----------|---------|----------|
| Windows Security Logs | | | |
| Sysmon | | | |
| Active Directory | | | |
| Kerberos | | | |
| NTLM | | | |
| DNS | | | |
| Firewall | | | |
| Suricata IDS | | | |
| PowerShell | | | |

---

# MITRE ATT&CK Coverage

| ATT&CK Tactic | Techniques Tested | Detections | Coverage |
|---------------|-------------------|------------|----------|
| Initial Access | | | |
| Execution | | | |
| Persistence | | | |
| Privilege Escalation | | | |
| Defense Evasion | | | |
| Credential Access | | | |
| Discovery | | | |
| Lateral Movement | | | |
| Collection | | | |
| Command and Control | | | |
| Exfiltration | | | |
| Impact | | | |

---

# Coverage Metrics

| Metric | Result |
|---------|--------|
| Assets Monitored | |
| Assets Covered | |
| Detection Rules Validated | |
| Successful Detections | |
| Missed Detections | |
| Coverage Percentage | |
| ATT&CK Techniques Covered | |
| ATT&CK Techniques Missing | |
| Critical Assets Protected | |

---

# Detection Performance

| Metric | Result |
|---------|--------|
| Detection Accuracy | |
| False Positive Rate | |
| False Negative Rate | |
| Mean Detection Time | |
| Alert Quality | |
| Correlation Effectiveness | |

---

# Coverage Gaps

## Gap ID

### Description

---

### Affected Assets

---

### Missing Telemetry

---

### Security Impact

---

### Recommendation

---

# Engineering Recommendations

Document improvements such as:

- Additional detection rules
- New telemetry sources
- Improved log collection
- Enhanced ATT&CK coverage
- Correlation rule optimization
- SIEM tuning
- Endpoint logging improvements

---

# Risk Assessment

| Risk | Severity | Priority |
|------|----------|----------|
| | | |

---

# Related Evidence

| Evidence ID | Description | Status |
|-------------|-------------|--------|
| | | |

---

# Related Normalized Datasets

- LHT-DetectionCoverage-Normalized.csv
- LHT-DetectionValidation-Normalized.csv
- LHT-Telemetry-Normalized.csv
- LHT-PurpleTeam-Normalized.csv
- LHT-AttackSimulation-Normalized.csv

---

# Supporting Documentation

- Purple-Team-Validation-Methodology.md
- Detection-Validation-Workflow.md
- Telemetry-Collection-Runbook.md
- Evidence-Correlation-Methodology.md

---

# Lessons Learned

Document:

- Detection strengths
- Coverage limitations
- Visibility improvements
- ATT&CK gaps
- Engineering priorities
- Future validation objectives

---

# Assessment Conclusion

Summarize the overall defensive visibility, identify remaining monitoring gaps, and determine whether the organization's detection capability provides adequate coverage for the assessed attack scenarios.

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


For Phase F, LHT-Coverage-Assessment-Template measure security visibility and detection coverage, not simply whether detections fired. 
This is the document that demonstrates to employers (especially MSSPs, Detection Engineering teams, and Purple Teams) that I understand how to quantify defensive 
capability, identify blind spots, and prioritize engineering improvements.

It consume outputs from:

LHT-DetectionCoverage-Normalized.csv
LHT-DetectionValidation-Normalized.csv
LHT-Telemetry-Normalized.csv
LHT-PurpleTeam-Normalized.csv

and answer questions like:

Are ATT&CK techniques covered?
Which telemetry supports each technique?
Where are the visibility gaps?
What should be engineered next?

Within your Phase F architecture, this document answers "How much of the attack lifecycle can we actually see?" rather than "Did a specific rule fire?" 
It connects attack simulations, telemetry, detections, and ATT&CK coverage into measurable defensive capability.

It also lays the foundation for Phase G – Detection Engineering and Coverage Measurement, where you'll develop and tune Splunk detections, Sigma rules, 
coverage matrices, and detection quality metrics. That continuity makes your Enterprise Security Evolution portfolio resemble the workflows used by mature SOCs, 
Purple Teams, and MSSPs.
