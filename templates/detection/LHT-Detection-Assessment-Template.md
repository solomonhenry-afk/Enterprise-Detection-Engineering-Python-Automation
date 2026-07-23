# Lighthouse Technology Detection Engineering Assessment Template

# Detection Engineering Assessment Report

---

# Document Information

| Field | Value |
|---|---|
| Assessment ID | LHT-DET-ASSESS-001 |
| Detection ID | DET-001 |
| Detection Name | Suspicious PowerShell Execution Detection |
| Assessment Type | Detection Engineering Validation |
| Version | 1.0 |
| Assessment Date | 2026-07-22 |
| Analyst | Lighthouse Technology Security Engineering Team |
| Reviewer | Detection Engineering Review Board |
| Status | Approved |

---

# 1. Assessment Overview

## 1.1 Detection Objective

The objective of this detection is to identify suspicious PowerShell execution patterns associated with adversary activity including command execution, script execution, payload delivery, and post-compromise operations.

The detection focuses on identifying abnormal PowerShell behaviors through endpoint telemetry and command-line analysis while maintaining operational visibility for legitimate administrative activities.

---

## 1.2 Business Security Objective

| Risk Area | Description |
|---|---|
| Threat | Malicious PowerShell execution by attackers after initial access |
| Business Impact | Unauthorized system access, malware execution, credential compromise, and potential domain compromise |
| Assets Protected | Enterprise endpoints, Active Directory systems, privileged accounts |
| Security Objective | Detect and respond to PowerShell-based attack activity before business impact occurs |

---

# 2. Detection Metadata

| Attribute | Value |
|---|---|
| Detection Name | Suspicious PowerShell Execution Detection |
| Detection Category | Endpoint Detection |
| Detection Type | Behavioral Correlation Rule |
| Severity | High |
| Priority | High |
| Detection Owner | Lighthouse Technology Detection Engineering Team |
| Lifecycle Status | Production Validated |

---

# 3. MITRE ATT&CK Mapping

| Field | Value |
|---|---|
| Tactic | Execution |
| Technique | Command and Scripting Interpreter: PowerShell |
| Technique ID | T1059.001 |
| Sub-Technique | PowerShell |
| ATT&CK Version | Enterprise ATT&CK v16 |

---

## Attack Scenario

An adversary gains access to an endpoint and uses PowerShell to execute commands, download tools, enumerate systems, establish persistence, or perform additional post-exploitation activities.

Common attacker behaviors include:

- Encoded PowerShell commands
- Hidden execution windows
- Download and execution of remote payloads
- PowerShell-based discovery
- Execution from suspicious parent processes

---

# 4. Detection Logic Overview

## 4.1 Detection Description

This detection identifies suspicious PowerShell activity by analyzing endpoint execution telemetry, command-line arguments, parent-child process relationships, and abnormal execution patterns.

The detection focuses on behaviors commonly associated with malicious PowerShell usage rather than blocking normal administrative activity.

Detection signals include:

- Encoded command execution
- Suspicious PowerShell flags
- Execution from unusual processes
- External network communication initiated by PowerShell
- Execution from temporary directories
- Abnormal user context

---

## 4.2 Detection Logic

```text
Detection Conditions:

1. Monitor process creation events involving powershell.exe.

2. Analyze command-line parameters for suspicious indicators:
   -EncodedCommand
   -ExecutionPolicy Bypass
   -Hidden
   -NoProfile

3. Identify suspicious parent-child relationships:
   - Office application spawning PowerShell
   - Browser spawning PowerShell
   - Script interpreters spawning PowerShell

4. Correlate PowerShell execution with:
   - User identity
   - Host reputation
   - Network activity
   - Previous security events

5. Generate alert when suspicious execution patterns exceed defined confidence threshold.
````

---

## 4.3 Detection Data Sources

| Source                | Event/Data Type                 | Required    |
| --------------------- | ------------------------------- | ----------- |
| Sysmon                | Event ID 1 Process Creation     | Yes         |
| PowerShell Logs       | Script Block Logging            | Yes         |
| Windows Security Logs | Process and User Activity       | Yes         |
| EDR Telemetry         | Endpoint Behavior Data          | Recommended |
| Network Logs          | Outbound Connection Correlation | Recommended |

---

# 5. Detection Implementation

## SIEM Implementation

| Platform           | Rule/Search Reference |
| ------------------ | --------------------- |
| Splunk             | SPL-001               |
| Microsoft Sentinel | N/A                   |
| QRadar             | N/A                   |

---

## Sigma Mapping

| Field               | Value                                   |
| ------------------- | --------------------------------------- |
| Sigma Rule ID       | SIG-001                                 |
| Rule Name           | Suspicious PowerShell Execution         |
| Status              | Production                              |
| Repository Location | detections/sigma/SIG-001-powershell.yml |

---

## Detection Rule Reference

| Field               | Value                      |
| ------------------- | -------------------------- |
| Rule ID             | RULE-001                   |
| Detection Framework | Sigma + Splunk Correlation |
| Severity            | High                       |
| Validation Status   | Passed                     |

---

# 6. Validation Methodology

## Validation Objective

Validate that the detection identifies simulated adversary PowerShell execution while maintaining acceptable false-positive levels.

---

## Test Scenario

| Field           | Value                                           |
| --------------- | ----------------------------------------------- |
| Simulation ID   | SIM-001                                         |
| Attack Scenario | Encoded PowerShell Execution                    |
| Execution Date  | 2026-07-22                                      |
| Tester          | Lighthouse Technology Security Engineering Team |

---

## Expected Result

The SIEM should generate a high-confidence alert containing:

* Host information
* User identity
* PowerShell command line
* Process relationship
* Supporting telemetry

---

## Observed Result

The detection generated an alert successfully and collected supporting endpoint telemetry.

The alert contained sufficient context for analyst investigation.

---

## Validation Outcome

| Result                          | Status |
| ------------------------------- | ------ |
| Detection Triggered             | Pass   |
| Evidence Collected              | Pass   |
| Analyst Investigation Completed | Pass   |
| ATT&CK Coverage Confirmed       | Pass   |

---

# 7. Alert Analysis

## Alert Details

| Field            | Value                |
| ---------------- | -------------------- |
| Alert ID         | ALT-001              |
| Timestamp        | 2026-07-22T09:10:00Z |
| Source Host      | LAB-WIN-ENDPOINT01   |
| User Account     | Test Administrator   |
| Severity         | High                 |
| Analyst Assigned | SOC Analyst          |

---

## Investigation Workflow

1. Review initial SIEM alert.
2. Validate process execution details.
3. Review PowerShell command content.
4. Correlate endpoint and authentication telemetry.
5. Determine malicious or legitimate behavior.
6. Document investigation outcome.

---

# 8. False Positive Analysis

## False Positive Review

| Question                                    | Response                                                 |
| ------------------------------------------- | -------------------------------------------------------- |
| Can legitimate activity trigger this alert? | Yes                                                      |
| Known benign scenarios?                     | Administrative scripting and automation                  |
| Required exclusions?                        | Approved administration accounts and signed scripts      |
| Tuning recommendations?                     | Apply behavioral filtering and baseline trusted activity |

---

## Tuning Actions

| Action                                   | Owner                      | Status    |
| ---------------------------------------- | -------------------------- | --------- |
| Review trusted PowerShell administrators | Detection Engineering Team | Completed |
| Validate automation accounts             | Identity Team              | Completed |
| Adjust suspicious argument detection     | Detection Engineering Team | Completed |

---

# 9. Detection Performance Metrics

| Metric                      | Value      |
| --------------------------- | ---------- |
| Alerts Generated            | 48         |
| True Positives              | 46         |
| False Positives             | 2          |
| False Negatives             | 0          |
| Precision                   | 95.83%     |
| Recall                      | 100%       |
| Detection Accuracy          | 95.83%     |
| Mean Time To Detect (MTTD)  | 3 Minutes  |
| Mean Time To Respond (MTTR) | 18 Minutes |

---

# 10. Coverage Assessment

## MITRE Coverage

| Technique            | Coverage |
| -------------------- | -------- |
| T1059.001 PowerShell | Full     |

---

## Detection Gaps

Current limitations:

* Advanced in-memory PowerShell activity may require additional EDR telemetry.
* Encrypted PowerShell communication requires network correlation.
* User behavior analytics can improve confidence scoring.

---

# 11. Evidence Register

| Evidence ID | Description                 | Location                    | Status   |
| ----------- | --------------------------- | --------------------------- | -------- |
| EVD-DET-001 | SIEM Alert Screenshot       | evidence/validation/alerts/ | Verified |
| EVD-DET-002 | Sysmon Process Event        | evidence/validation/logs/   | Verified |
| EVD-DET-003 | Simulation Execution Record | evidence/simulated/         | Verified |

---

# 12. Recommendations

## Immediate Improvements

1. Continue monitoring PowerShell execution across enterprise endpoints.
2. Maintain Sysmon process visibility.
3. Improve correlation with identity telemetry.

---

## Long-Term Improvements

1. Integrate machine-learning based behavior analytics.
2. Expand detection coverage across cloud workloads.
3. Automate investigation workflows using SOAR.

---

# 13. Approval

| Role               | Name                                            | Date       | Approval |
| ------------------ | ----------------------------------------------- | ---------- | -------- |
| Detection Engineer | Lighthouse Technology Security Engineering Team | 2026-07-22 | Approved |
| Security Lead      | Detection Engineering Review Board              | 2026-07-22 | Approved |
| Reviewer           | Enterprise Security Governance Team             | 2026-07-22 | Approved |

---

# Appendix A: References

## Related Artifacts

| Artifact           | Reference                                                      |
| ------------------ | -------------------------------------------------------------- |
| Detection Use Case | data/normalized/detection/LHT-DetectionUseCases-Normalized.csv |
| Detection Rule     | data/normalized/detection/LHT-DetectionRules-Normalized.csv    |
| Sigma Rule         | data/normalized/detection/LHT-SigmaRules-Normalized.csv        |
| Splunk Search      | data/normalized/detection/LHT-SplunkSearches-Normalized.csv    |
| ATT&CK Coverage    | data/normalized/detection/LHT-ATTACKCoverage-Normalized.csv    |
| Alert Validation   | data/normalized/detection/LHT-AlertValidation-Normalized.csv   |
| Detection Metrics  | data/normalized/detection/LHT-DetectionMetrics-Normalized.csv  |

---

# Appendix B: Change History

| Version | Date       | Change                                            | Author                                          |
| ------- | ---------- | ------------------------------------------------- | ----------------------------------------------- |
| 1.0     | 2026-07-22 | Initial detection engineering assessment creation | Lighthouse Technology Security Engineering Team |

