# Lighthouse Technology Detection Engineering Use Case Template

# Detection Use Case Specification

---

# Document Information

| Field | Value |
|---|---|
| Use Case ID | LHT-DET-UC-001 |
| Detection ID | DET-001 |
| Use Case Name | Suspicious PowerShell Execution Detection |
| Detection Category | Endpoint Security Monitoring |
| Document Type | Detection Engineering Use Case |
| Version | 1.0 |
| Creation Date | 2026-07-22 |
| Owner | Lighthouse Technology Detection Engineering Team |
| Reviewer | Enterprise Security Governance Team |
| Status | Approved |
| Classification | Internal Security Engineering Documentation |

---

# 1. Use Case Overview

## 1.1 Purpose

This detection use case defines the security monitoring requirements for identifying suspicious PowerShell execution activity associated with adversary behavior across enterprise environments.

The objective is to provide continuous visibility into PowerShell-based execution techniques commonly used during:

- Initial compromise
- Post-exploitation activity
- Malware execution
- Credential harvesting
- Discovery operations
- Lateral movement preparation

---

## 1.2 Business Objective

| Area | Description |
|---|---|
| Business Risk | Attackers abusing legitimate administrative tools to execute malicious commands |
| Security Objective | Detect and investigate unauthorized PowerShell activity |
| Protected Assets | Enterprise endpoints, servers, privileged systems |
| Expected Outcome | Early detection and response before significant compromise |

---

# 2. Threat Scenario

## Adversary Behavior

An attacker with access to an enterprise endpoint executes PowerShell commands to perform malicious activities while attempting to blend with legitimate administrative operations.

Common attacker behaviors:

- Encoded PowerShell execution
- Execution policy bypass
- Downloading remote payloads
- Script-based persistence
- Endpoint reconnaissance
- Credential access preparation

---

## Example Attack Flow

```text
Initial Access
        |
        ↓
Compromised User Account
        |
        ↓
PowerShell Execution
        |
        ↓
Command Execution
        |
        ↓
Discovery / Persistence / Lateral Movement
        |
        ↓
Detection & Response
````

---

# 3. MITRE ATT&CK Mapping

| Field                | Value                             |
| -------------------- | --------------------------------- |
| ATT&CK Tactic        | Execution                         |
| ATT&CK Technique     | Command and Scripting Interpreter |
| ATT&CK Sub-Technique | PowerShell                        |
| ATT&CK ID            | T1059.001                         |
| Platform             | Windows                           |
| Detection Priority   | High                              |

---

# 4. Detection Objective

## Primary Detection Goal

Identify suspicious PowerShell execution patterns indicating possible malicious activity.

---

## Detection Questions

The use case should answer:

| Question                             | Objective                                      |
| ------------------------------------ | ---------------------------------------------- |
| Who executed PowerShell?             | Identify responsible user account              |
| Where was PowerShell executed?       | Identify affected host                         |
| What command was executed?           | Analyze intent                                 |
| How was execution initiated?         | Determine process relationship                 |
| Was external communication involved? | Identify possible command and control activity |

---

# 5. Required Telemetry

| Data Source           | Event / Data Type           | Purpose            |
| --------------------- | --------------------------- | ------------------ |
| Sysmon                | Event ID 1 Process Creation | Process visibility |
| PowerShell Logging    | Script Block Logging        | Command visibility |
| Windows Security Logs | Authentication Events       | User attribution   |
| EDR Telemetry         | Endpoint Behavior           | Advanced analysis  |
| Network Logs          | Connections                 | C2 correlation     |

---

# 6. Detection Logic Summary

## Detection Conditions

The detection should trigger when:

1. PowerShell executes with suspicious parameters.
2. Encoded commands are detected.
3. PowerShell launches from abnormal parent processes.
4. PowerShell communicates with suspicious external resources.
5. Execution occurs from unusual user contexts.

---

## Detection Logic Example

```text
IF
Process = powershell.exe

AND

(CommandLine contains:
 -EncodedCommand
 -ExecutionPolicy Bypass
 -WindowStyle Hidden)

OR

Parent Process is suspicious

THEN

Generate High Severity Detection Alert
```

---

# 7. Detection Implementation

## SIEM Mapping

| Platform           | Reference |
| ------------------ | --------- |
| Splunk             | SPL-001   |
| Microsoft Sentinel | Planned   |
| QRadar             | Planned   |

---

## Detection Rule Mapping

| Artifact          | Reference |
| ----------------- | --------- |
| Detection Rule ID | RULE-001  |
| Sigma Rule ID     | SIG-001   |
| Search ID         | SPL-001   |

---

# 8. Alert Classification

| Field                | Value                     |
| -------------------- | ------------------------- |
| Severity             | High                      |
| Priority             | High                      |
| Confidence           | High                      |
| Category             | Endpoint Threat Detection |
| Response Requirement | SOC Investigation         |

---

# 9. Investigation Workflow

## Analyst Investigation Steps

### Step 1: Validate Alert

Review:

* Host
* User
* Timestamp
* Command line
* Parent process

---

### Step 2: Analyze Execution Context

Determine:

* Legitimate administrative activity?
* User authorization?
* Suspicious behavior?
* Malware indicators?

---

### Step 3: Correlate Additional Evidence

Review:

* Authentication logs
* Network activity
* EDR telemetry
* Threat intelligence

---

### Step 4: Determine Response

Possible outcomes:

* Close as legitimate
* Tune detection
* Escalate incident
* Initiate containment

---

# 10. Validation Requirements

## Purple Team Validation

| Field             | Value                              |
| ----------------- | ---------------------------------- |
| Simulation ID     | SIM-001                            |
| Validation Type   | Adversary Simulation               |
| Expected Outcome  | Detection alert generated          |
| Evidence Required | Alert logs, screenshots, telemetry |

---

# 11. False Positive Management

## Known Legitimate Activities

Examples:

* Enterprise administration scripts
* Software deployment systems
* Security automation tools

---

## Tuning Strategy

| Action                           | Purpose                       |
| -------------------------------- | ----------------------------- |
| Baseline administrative activity | Reduce noise                  |
| Validate trusted accounts        | Prevent unnecessary alerts    |
| Maintain behavioral indicators   | Preserve detection capability |

---

# 12. Metrics and Success Criteria

| Metric              | Target    |
| ------------------- | --------- |
| Detection Accuracy  | >90%      |
| False Positive Rate | <10%      |
| Alert Generation    | Confirmed |
| Evidence Collection | Complete  |
| ATT&CK Coverage     | Full      |

---

# 13. Ownership and Governance

| Role               | Responsibility                 |
| ------------------ | ------------------------------ |
| Detection Engineer | Develop and maintain detection |
| SOC Analyst        | Investigate alerts             |
| Security Lead      | Approve lifecycle changes      |
| Governance Team    | Validate compliance            |

---

# 14. Lifecycle Management

| Stage                   | Status    |
| ----------------------- | --------- |
| Requirements Definition | Completed |
| Detection Development   | Completed |
| Validation Testing      | Completed |
| Production Deployment   | Approved  |
| Continuous Improvement  | Active    |

---

# 15. Evidence References

| Evidence           | Location                                                      |
| ------------------ | ------------------------------------------------------------- |
| Detection Metadata | data/normalized/detection/LHT-DetectionMetadata.csv           |
| Detection Rules    | data/normalized/detection/LHT-DetectionRules-Normalized.csv   |
| Sigma Rules        | data/normalized/detection/LHT-SigmaRules-Normalized.csv       |
| Splunk Searches    | data/normalized/detection/LHT-SplunkSearches-Normalized.csv   |
| Alert Validation   | data/normalized/detection/LHT-AlertValidation-Normalized.csv  |
| Detection Metrics  | data/normalized/detection/LHT-DetectionMetrics-Normalized.csv |

---

# Appendix A: References

* MITRE ATT&CK Enterprise Framework
* Sigma Detection Rule Framework
* Splunk Detection Engineering Framework
* Lighthouse Technology Detection Engineering Methodology
* Lighthouse Technology Purple Team Validation Framework

---

# Appendix B: Change History

| Version | Date       | Change                                                  | Author                                          |
| ------- | ---------- | ------------------------------------------------------- | ----------------------------------------------- |
| 1.0     | 2026-07-22 | Initial enterprise detection use case template creation | Lighthouse Technology Security Engineering Team |

