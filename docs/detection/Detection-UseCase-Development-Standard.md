# Lighthouse Technology
# Detection Use Case Development Standard

Version: 1.0 
Project: Enterprise Security Evolution 
Domain: Enterprise Active Directory Penetration Testing & Security Auditing 
Phase: G — Detection Engineering & Coverage Measurement

---

# 1. Purpose

This standard defines the process for developing high-quality security detection use cases within the Lighthouse Technology Enterprise Security Evolution program.

A detection use case describes **what attacker behavior should be detected, why it matters, how it is detected, which telemetry is required, how it is validated, and how analysts should investigate it.**

The objective is to produce repeatable, evidence-driven detections that improve visibility, reduce detection gaps, and support enterprise Security Operations Center (SOC) workflows.

---

# 2. Objectives

The Detection Use Case Development Standard enables security teams to:

- Detect malicious activity consistently
- Align detections with attacker behaviors
- Reduce false positives
- Improve detection quality
- Standardize engineering practices
- Support Purple Team validation
- Measure ATT&CK coverage
- Improve incident response efficiency

---

# 3. Detection Development Lifecycle

Every detection follows the same lifecycle.

```
Threat Research
        │
        ▼
ATT&CK Mapping
        │
        ▼
Telemetry Identification
        │
        ▼
Detection Logic Design
        │
        ▼
Rule Development
        │
        ▼
Validation
        │
        ▼
False Positive Tuning
        │
        ▼
Deployment
        │
        ▼
Continuous Improvement
```

---

# 4. Detection Use Case Components

Every use case must contain the following sections.

## Detection ID

Unique identifier.

Example

```
DET-001
```

---

## Detection Name

Clear descriptive title.

Example

```
Suspicious PowerShell Encoded Command Execution
```

---

## Objective

Explain what the detection identifies.

Example

```
Detect PowerShell processes launched using Base64-encoded commands.
```

---

## Business Risk

Explain why detection matters.

Example

```
Encoded PowerShell is frequently used by attackers to evade security controls and execute malicious payloads.
```

---

## Threat Scenario

Describe attacker behavior.

Example

```
An attacker gains user access and executes an encoded PowerShell payload to establish persistence.
```

---

# 5. MITRE ATT&CK Mapping

Every detection maps to ATT&CK.

Include:

Technique

Sub-Technique

Tactic

Procedure

Example

```
Technique:
T1059.001

Tactic:
Execution

Procedure:
PowerShell EncodedCommand
```

---

# 6. Detection Priority

Every detection receives a priority.

| Priority | Description |
|----------|-------------|
| Critical | Immediate response required |
| High | High-confidence malicious activity |
| Medium | Suspicious activity requiring investigation |
| Low | Monitoring only |
| Informational | Visibility enhancement |

---

# 7. Severity Rating

Severity reflects business impact.

| Severity | Meaning |
|-----------|---------|
| Critical | Enterprise compromise possible |
| High | Significant security impact |
| Medium | Potential compromise |
| Low | Limited impact |
| Informational | Audit visibility |

---

# 8. Data Sources

Every use case identifies required telemetry.

Examples include:

- Windows Security Logs
- Sysmon
- PowerShell Operational Logs
- Defender Logs
- Active Directory Logs
- Kerberos Events
- NTLM Events
- LDAP Events
- DNS Logs
- Firewall Logs
- IDS Alerts
- Splunk Indexed Events

---

# 9. Required Event IDs

Document required Windows Event IDs.

Example

| Event | Purpose |
|---------|----------|
| 4624 | Successful Logon |
| 4625 | Failed Logon |
| 4672 | Special Privileges Assigned |
| 4688 | Process Creation |
| 4697 | Service Installed |
| 4720 | User Created |
| 4728 | Group Membership Added |
| 4768 | Kerberos TGT |
| 4769 | Kerberos Service Ticket |

---

# 10. Detection Logic

Describe how detection works.

Include:

- Event conditions
- Correlation logic
- Time window
- Thresholds
- Required fields
- Exclusions

Example

```
IF

Process Name = powershell.exe

AND

CommandLine contains "-enc"

THEN

Generate High Severity Alert
```

---

# 11. Splunk Detection

Document SPL logic.

Include:

- Index
- Sourcetype
- Search
- Correlation
- Alert threshold

---

# 12. Sigma Rule

Where applicable, document Sigma detection.

Include:

- Title
- Log Source
- Detection
- Condition
- Level
- ATT&CK Mapping

---

# 13. Detection Dependencies

Identify prerequisites.

Examples

- Sysmon installed
- PowerShell logging enabled
- Audit Policy enabled
- Event forwarding configured
- Splunk ingestion verified

---

# 14. Validation Method

Every detection must be validated.

Validation includes:

- Controlled simulation
- Expected telemetry
- Alert generation
- Investigation
- Evidence capture
- Analyst review

---

# 15. Expected Telemetry

Document expected evidence.

Examples

- Event ID
- Username
- Hostname
- Source IP
- Destination IP
- Parent Process
- Command Line
- SID
- Logon Type

---

# 16. Investigation Guidance

Analysts should know what to investigate.

Example

Verify:

- Parent process
- User account
- Host history
- Authentication events
- Lateral movement
- Additional alerts
- Endpoint artifacts

---

# 17. Response Guidance

Recommended actions.

Examples

- Validate alert
- Isolate endpoint
- Disable account
- Reset credentials
- Block hash
- Collect forensic evidence
- Notify Incident Response

---

# 18. False Positive Analysis

Document expected benign activity.

Examples

- Administrator scripts
- Automation jobs
- Backup software
- Configuration management
- Security tooling

---

# 19. False Negative Analysis

Document detection limitations.

Examples

- Missing telemetry
- Logging disabled
- Obfuscated payloads
- Unsupported operating systems
- Encrypted communications

---

# 20. Detection Tuning

Review:

- Thresholds
- Whitelists
- Baselines
- Noise reduction
- Service account exclusions
- Scheduled task exclusions

---

# 21. Performance Considerations

Evaluate:

- Search efficiency
- CPU utilization
- Memory impact
- Query optimization
- Index performance
- Alert frequency

---

# 22. Evidence Requirements

Each validated detection produces:

- Detection ID
- Validation ID
- Evidence ID
- Screenshot
- Splunk results
- Raw logs
- Sigma rule
- Analyst notes
- Timestamp
- Integrity hash

---

# 23. Success Criteria

A detection is considered production-ready when:

- ATT&CK mapping is complete.
- Detection logic is documented.
- Validation is successful.
- Evidence is collected.
- False positives are acceptable.
- False negatives are understood.
- Investigation guidance is complete.
- Response actions are documented.
- Detection is peer reviewed.
- Detection is version controlled.

---

# 24. Deliverables

This standard supports production of:

- Detection Register
- Detection Catalog
- Sigma Rules
- Splunk Detection Library
- Validation Reports
- Coverage Matrix
- MITRE ATT&CK Mapping
- Detection Metrics
- Purple Team Validation Results
- Executive Detection Coverage Dashboard

---

# 25. Related Documents

- Detection Engineering Methodology
- Detection Validation Workflow
- Purple Team Validation Methodology
- Evidence Correlation Methodology
- Telemetry Collection Runbook
- Validation Safety Standard
- MITRE ATT&CK Coverage Matrix
- Detection Coverage Methodology

---

