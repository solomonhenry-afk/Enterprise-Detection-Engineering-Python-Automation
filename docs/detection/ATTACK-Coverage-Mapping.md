# ATT&CK Coverage Mapping

**Document ID:** LHT-D5-PG-METH-007 
**Phase:** G — Detection Engineering & Coverage Measurement 
**Domain:** Domain 5 – Enterprise Active Directory Penetration Testing & Security Auditing 
**Classification:** Portfolio / Enterprise Security Engineering 
**Version:** 1.0 
**Status:** Approved 

---

# 1. Purpose

This document defines the standardized methodology for mapping enterprise detections to the MITRE ATT&CK® Framework.

The objective is to measure defensive visibility against adversary techniques, identify detection gaps, prioritize engineering efforts, and demonstrate measurable security coverage across the Lighthouse Technology Enterprise Security Evolution project.

Coverage mapping transforms individual detection rules into an enterprise detection capability model.

---

# 2. Objectives

The ATT&CK Coverage Mapping process aims to:

- Align detections with real adversary behavior
- Measure visibility across the attack lifecycle
- Identify blind spots
- Prioritize new detection engineering
- Improve Purple Team validation
- Support executive reporting
- Demonstrate security maturity

---

# 3. Business Value

Rather than asking:

> "How many detection rules do we have?"

Security leadership asks:

> "Which attacker techniques can we actually detect?"

Coverage mapping answers that question.

Benefits include:

- measurable detection capability
- engineering prioritization
- threat-informed defense
- reduced attacker dwell time
- improved SOC maturity
- evidence-driven security investment

---

# 4. Mapping Workflow

```
MITRE ATT&CK Technique

        │

        ▼

Threat Scenario

        │

        ▼

Telemetry Sources

        │

        ▼

Detection Rule

        │

        ▼

Validation Testing

        │

        ▼

Coverage Assessment

        │

        ▼

Gap Analysis

        │

        ▼

Coverage Dashboard
```

---

# 5. Coverage Categories

## Initial Access

Examples

- External Remote Services
- Valid Accounts
- Exploiting Public Facing Applications

Telemetry

- Firewall
- VPN Logs
- Windows Authentication
- Web Logs

---

## Execution

Examples

- PowerShell
- Command Shell
- Scheduled Task

Telemetry

- Sysmon
- PowerShell Logging
- Windows Security Events

---

## Persistence

Examples

- Services
- Startup Folder
- Registry Run Keys

Telemetry

- Sysmon
- Registry Auditing
- Windows Events

---

## Privilege Escalation

Examples

- Token Manipulation
- UAC Bypass
- Group Membership Changes

Telemetry

- Event ID 4672
- Event ID 4728
- Sysmon

---

## Defense Evasion

Examples

- Log Clearing
- AMSI Bypass
- Security Tool Disable

Telemetry

- Event 1102
- Defender Events
- Sysmon

---

## Credential Access

Examples

- Kerberoasting
- LSASS Dump
- NTLM Abuse

Telemetry

- Kerberos Events
- Sysmon
- Windows Security Logs

---

## Discovery

Examples

- LDAP Enumeration
- Account Discovery
- Network Share Discovery

Telemetry

- PowerShell
- Sysmon
- Windows Events

---

## Lateral Movement

Examples

- PsExec
- SMB
- Remote Service Creation

Telemetry

- Event 4624
- Event 7045
- Sysmon

---

## Collection

Examples

- Archive Collected Data
- Clipboard Capture

Telemetry

- Endpoint Logging
- DLP
- Sysmon

---

## Command & Control

Examples

- Beacon Traffic
- DNS Tunneling

Telemetry

- DNS Logs
- Firewall
- Proxy
- Suricata

---

## Exfiltration

Examples

- HTTP Upload
- Cloud Storage Abuse

Telemetry

- Proxy Logs
- Firewall
- Web Logs

---

## Impact

Examples

- Ransomware
- Data Destruction
- Service Stop

Telemetry

- Windows Events
- EDR
- Sysmon

---

# 6. Detection Mapping Fields

Each detection should include:

| Field | Description |
|----------|----------------|
| Detection ID | Unique Identifier |
| ATT&CK Tactic | ATT&CK Stage |
| ATT&CK Technique | Technique ID |
| Detection Name | Rule Name |
| Telemetry Source | Logs Required |
| Severity | Low–Critical |
| Validation Status | Tested/Untested |
| Coverage Rating | High/Medium/Low |
| False Positive Rate | Percentage |
| Confidence | Analyst Confidence |

---

# 7. Coverage Rating

## High

Detection reliably identifies technique.

Characteristics

- validated
- low false positives
- multiple telemetry sources

---

## Medium

Detection exists but requires tuning.

Characteristics

- moderate confidence
- partial visibility

---

## Low

Limited visibility.

Characteristics

- unreliable
- inconsistent
- requires engineering

---

## None

No current detection.

Immediate engineering candidate.

---

# 8. Mapping Example

| Technique | Detection | Telemetry | Coverage |
|------------|-----------|-----------|----------|
| T1558 Kerberoasting | Kerberos TGS Request Monitoring | Event 4769 | High |
| T1078 Valid Accounts | Excessive Logons | Event 4624 | High |
| T1003 LSASS Dump | Sysmon Process Access | Sysmon Event 10 | Medium |
| T1021 SMB Lateral Movement | Remote Service Detection | Event 7045 | High |
| T1059 PowerShell | Suspicious PowerShell | Script Block Logs | High |

---

# 9. Gap Identification

Coverage analysis should identify:

- unsupported ATT&CK techniques
- missing telemetry
- missing Sigma rules
- missing Splunk detections
- logging deficiencies
- Windows auditing gaps
- endpoint visibility gaps

Each gap should produce a remediation recommendation.

---

# 10. Purple Team Integration

Purple Team validation verifies whether mapped detections actually trigger.

Workflow

```
Adversary Simulation

        │

        ▼

Technique Executed

        │

        ▼

Telemetry Generated

        │

        ▼

Detection Triggered

        │

        ▼

SOC Review

        │

        ▼

Coverage Updated
```

Coverage is never considered complete until validated.

---

# 11. Coverage Metrics

Recommended KPIs

- ATT&CK Techniques Covered
- ATT&CK Techniques Missing
- Detection Validation Success %
- Mean Detection Time
- False Positive Rate
- Detection Confidence
- Sigma Rule Count
- Splunk Rule Count
- Validated Detection %
- Coverage by ATT&CK Tactic

---

# 12. Evidence Produced

Coverage mapping generates:

- ATT&CK Mapping Register
- Detection Inventory
- Coverage Matrix
- Gap Analysis
- Validation Results
- Engineering Recommendations
- Executive Coverage Dashboard

---

# 13. Integration with Other Phases

This methodology consumes outputs from:

- Phase C — Identity Inventory
- Phase D — Privilege Exposure Analysis
- Phase E — Authentication Security Assessment
- Phase F — Purple Team Validation

Its outputs become inputs into:

- Phase H — Remediation Engineering
- Phase I — Technical Reporting
- Phase J — Portfolio Publication

This establishes end-to-end traceability from enterprise assessment through detection engineering, validation, remediation, and executive reporting.

---

# 14. Expected Deliverables

Implementation of this methodology should produce:

- ATT&CK Coverage Matrix
- Sigma-to-ATT&CK Mapping
- Splunk Detection Mapping
- Detection Gap Register
- Coverage Dashboard
- Validation Evidence
- Coverage Metrics Report
- Detection Engineering Roadmap

These artifacts provide measurable evidence of enterprise detection capability and support continuous improvement of defensive security operations.
