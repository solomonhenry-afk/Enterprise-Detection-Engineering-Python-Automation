# Splunk Detection Engineering Guide

**Document ID:** LHT-PHASE-G-SPLUNK-001 
**Project:** Lighthouse Technology – Enterprise Security Evolution 
**Phase:** G – Detection Engineering & Coverage Measurement 
**Classification:** Internal – Detection Engineering Standard 
**Version:** 1.0 
**Status:** Approved 

---

# 1. Purpose

This guide defines the standard methodology for engineering, validating, tuning, and maintaining Splunk detections throughout the Lighthouse Technology Enterprise Security Evolution project.

The objective is to create detections that are:

- Accurate
- Repeatable
- Low-noise
- ATT&CK-aligned
- Evidence-driven
- Operationally useful

rather than creating searches that merely generate alerts.

---

# 2. Scope

This methodology applies to all Splunk detection content including:

- Enterprise Security Correlation Searches
- SPL Detection Searches
- Scheduled Searches
- Dashboard Panels
- Risk-Based Alerting (RBA)
- Investigation Searches
- Hunting Queries
- Detection Validation
- Purple Team Validation

---

# 3. Objectives

The detection engineering program aims to:

- Detect adversary behavior
- Minimize false positives
- Improve detection coverage
- Increase analyst efficiency
- Produce repeatable detections
- Support Purple Team validation
- Support ATT&CK coverage measurement
- Produce evidence suitable for governance reporting

---

# 4. Detection Engineering Lifecycle

Every Splunk detection follows the same lifecycle.

```
Threat Intelligence
        │
        ▼
Detection Requirement
        │
        ▼
Telemetry Review
        │
        ▼
SPL Development
        │
        ▼
Lab Validation
        │
        ▼
Purple Team Testing
        │
        ▼
False Positive Review
        │
        ▼
Tuning
        │
        ▼
Production Approval
        │
        ▼
Continuous Improvement
```

---

# 5. Detection Sources

Detections may originate from:

- MITRE ATT&CK
- Purple Team exercises
- Incident response
- Threat hunting
- CVE research
- Vendor advisories
- Microsoft security guidance
- Sigma rules
- Security research
- Red Team findings
- Internal observations

---

# 6. Detection Categories

## Authentication

Examples

- Failed logons
- Password spraying
- Kerberos abuse
- NTLM usage
- Service account misuse
- Delegation abuse

---

## Endpoint

Examples

- PowerShell
- Sysmon
- Process creation
- Parent-child anomalies
- Registry persistence
- Scheduled Tasks

---

## Active Directory

Examples

- Privilege escalation
- Group modifications
- Tier Zero access
- DC authentication
- GPO modification
- DCSync indicators

---

## Network

Examples

- IDS alerts
- Firewall events
- DNS anomalies
- SMB abuse
- Lateral movement
- Beaconing

---

## Cloud

Examples

- Azure Sign-In Logs
- AWS CloudTrail
- IAM changes
- MFA bypass
- Conditional Access failures

---

# 7. Required Telemetry

Detection development begins only after confirming telemetry availability.

Typical data sources include:

| Source | Purpose |
|---------|----------|
| Windows Security | Authentication |
| Sysmon | Endpoint behavior |
| PowerShell | Script execution |
| DNS | Resolution activity |
| Firewall | Network traffic |
| Suricata | IDS alerts |
| Active Directory | Identity events |
| Splunk Forwarders | Log collection |
| Linux Syslog | Server monitoring |

---

# 8. SPL Development Standard

Each detection should answer:

- What attacker behavior exists?
- Which logs contain evidence?
- Which fields identify the activity?
- How should normal activity be filtered?
- What threshold triggers investigation?

Example workflow:

```
Threat

↓

ATT&CK Technique

↓

Required Logs

↓

Relevant Fields

↓

SPL Query

↓

Validation

↓

Tuning

↓

Deployment
```

---

# 9. Detection Metadata

Every detection must include:

- Detection ID
- Name
- Description
- ATT&CK Technique
- ATT&CK Tactic
- Data Sources
- Required Logs
- SPL Query
- Validation Status
- Severity
- Analyst Notes
- False Positive Guidance
- Tuning History
- Owner
- Review Date

---

# 10. Validation Process

Each detection is validated using controlled adversary simulation.

Validation includes:

- Attack execution
- Telemetry verification
- SPL execution
- Alert confirmation
- Evidence capture
- Analyst review

Validation artifacts include:

- Screenshots
- Raw logs
- Search output
- Event IDs
- Detection metadata
- Evidence register

---

# 11. False Positive Review

Each detection must document:

Expected benign activity

Potential false positives

Business exceptions

Whitelisting decisions

Filtering logic

Residual detection risk

---

# 12. False Negative Review

Detection engineering also evaluates:

Missing telemetry

Logging gaps

Unsupported attack variants

Field normalization issues

Parsing failures

Collection delays

Coverage limitations

---

# 13. Detection Tuning

After validation:

Adjust thresholds

Improve filters

Normalize fields

Reduce duplicate alerts

Improve performance

Document changes

Revalidate detection

---

# 14. Risk-Based Prioritization

Detections are prioritized according to business impact.

Example factors:

- Critical assets
- Tier Zero systems
- Domain Controllers
- Privileged accounts
- High-value servers
- Internet-facing systems

---

# 15. MITRE ATT&CK Mapping

Each detection must map to:

- Tactic
- Technique
- Sub-Technique
- Procedure (if known)

Example:

```
Credential Access

↓

OS Credential Dumping

↓

LSASS Access

↓

Sysmon Detection

↓

Splunk Alert
```

---

# 16. Performance Considerations

Detection searches should:

Minimize expensive wildcard searches

Use indexed fields

Reduce unnecessary joins

Limit historical search windows

Use accelerated data models where appropriate

Optimize scheduled search frequency

---

# 17. Documentation Requirements

Each detection produces:

Detection Specification

SPL Query

Validation Report

Evidence Register

Coverage Matrix Entry

ATT&CK Mapping

Tuning Record

Analyst Notes

---

# 18. Integration with Phase F

Purple Team validation provides:

Validated telemetry

Attack evidence

Detection effectiveness

Coverage gaps

False positives

False negatives

Recommendations

Phase G consumes these outputs to improve detection quality.

---

# 19. Integration with Phase H

Detection engineering outputs become remediation inputs.

Examples include:

Missing logging

Disabled Sysmon

Incorrect forwarding

Parser failures

Insufficient audit policy

Logging blind spots

Coverage weaknesses

Phase H uses these findings to improve enterprise detection maturity.

---

# 20. Expected Deliverables

This guide supports creation of:

- Splunk Detection Library
- Detection Catalog
- Detection Coverage Matrix
- SPL Search Repository
- Detection Validation Reports
- ATT&CK Coverage Report
- Purple Team Correlation Reports
- Detection Tuning Register
- Executive Detection Metrics

---

# 21. Success Criteria

The methodology is considered successful when:

- Detections consistently identify validated attack activity.
- False positives are reduced through structured tuning.
- Detection coverage aligns with prioritized MITRE ATT&CK techniques.
- Splunk searches are documented, repeatable, and evidence-backed.
- Detection content integrates with Purple Team validation and remediation workflows.
- Detection engineering outputs support governance reporting, executive metrics, and continuous security improvement across the enterprise.
