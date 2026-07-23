# Sigma Rule Development Standard

**Document ID:** LHT-DET-STD-005 
**Domain:** Domain 5 – Enterprise Active Directory Penetration Testing & Security Auditing 
**Phase:** G – Detection Engineering & Coverage Measurement 
**Classification:** Internal Security Engineering Standard 
**Version:** 1.0 
**Status:** Approved

---

# 1. Purpose

This standard defines the engineering process for designing, developing, validating, documenting, tuning, and maintaining Sigma detection rules within the Lighthouse Technology Enterprise Security Evolution program.

The objective is to ensure that every Sigma rule is:

- technically accurate
- reproducible
- evidence-driven
- ATT&CK aligned
- portable across SIEM platforms
- validated through controlled Purple Team simulations

This standard provides a repeatable framework for producing enterprise-grade detection content suitable for security operations centers (SOC), MSSP environments, and enterprise detection engineering teams.

---

# 2. Scope

This standard applies to:

- Windows Event Logs
- Sysmon Events
- Active Directory Events
- PowerShell Logs
- Authentication Events
- Kerberos Events
- NTLM Events
- Process Creation
- Service Installation
- Registry Changes
- Network Connections
- Scheduled Tasks
- Account Management
- Group Membership Changes
- Privilege Escalation Activities

---

# 3. Objectives

The Sigma engineering process shall ensure:

- consistent detection logic
- normalized rule structure
- ATT&CK mapping
- reduced false positives
- repeatable validation
- evidence traceability
- long-term maintainability

---

# 4. Sigma Development Lifecycle

Every rule progresses through the following lifecycle.

```
Threat Research
        │
        ▼
Technique Identification
        │
        ▼
Telemetry Mapping
        │
        ▼
Sigma Rule Draft
        │
        ▼
Lab Validation
        │
        ▼
False Positive Review
        │
        ▼
Rule Tuning
        │
        ▼
Approval
        │
        ▼
Production Deployment
        │
        ▼
Continuous Improvement
```

---

# 5. Rule Development Inputs

Each Sigma rule shall begin with documented intelligence.

Required inputs include:

- MITRE ATT&CK Technique
- Threat Intelligence
- Purple Team Scenario
- Adversary Procedure
- Security Event IDs
- Sysmon Events
- Log Source
- Detection Goal
- Expected Evidence

---

# 6. Standard Sigma Rule Structure

Every rule shall contain:

## Metadata

- Title
- ID
- Status
- Description
- Author
- Date
- References

---

## Log Source

Example

```
product: windows
service: security
```

---

## Detection Logic

Detection conditions shall define:

- event IDs
- field matching
- keywords
- command lines
- parent processes
- hashes
- registry paths
- service names
- usernames

---

## Condition

Example

```
selection
```

or

```
selection and not whitelist
```

---

## False Positive Notes

Every rule must describe:

Possible administrator activity

Automation tools

Expected maintenance events

Known software behavior

---

## Severity

Example

```
low
medium
high
critical
```

---

## ATT&CK Mapping

Every rule shall include:

Technique ID

Technique Name

Tactic

Example

```
T1059

Command and Scripting Interpreter

Execution
```

---

# 7. Detection Design Principles

Detection logic should prioritize

behavior

instead of

single Indicators of Compromise.

Preferred

```
PowerShell spawning encoded commands
```

instead of

```
Specific malware hash
```

Preferred

```
Privilege escalation behavior
```

instead of

```
Known attacker username
```

---

# 8. Telemetry Mapping

Every rule must identify required telemetry.

Example

| Source | Purpose |
|---------|----------|
| Windows Security Logs | Authentication |
| Sysmon | Process Activity |
| PowerShell | Script Logging |
| DNS Logs | Beaconing |
| Firewall | Network Sessions |
| Suricata | IDS Events |
| Splunk | Correlation |

---

# 9. Rule Validation Requirements

A rule cannot be approved without validation.

Validation includes:

Controlled attack simulation

Expected detection

Evidence collection

Alert verification

False-positive review

False-negative review

Performance review

Analyst review

---

# 10. Rule Quality Checklist

Every Sigma rule shall answer:

✓ Does telemetry exist?

✓ Is ATT&CK mapped?

✓ Is behavior-based?

✓ Has it been tested?

✓ Can analysts investigate?

✓ Is evidence reproducible?

✓ Are false positives documented?

✓ Is severity justified?

---

# 11. False Positive Review

Every rule shall document

Expected legitimate activity

Administrative usage

Software installers

Automation tools

Backup software

Enterprise management agents

Developer activity

Maintenance windows

---

# 12. Rule Tuning

Tuning activities include

Field refinement

Additional conditions

Whitelisting

Process exclusions

Host exclusions

Account exclusions

Environment-specific filters

Noise reduction

---

# 13. Rule Performance Review

Detection engineers shall evaluate

Alert volume

Detection latency

Search efficiency

Correlation quality

Execution time

Index utilization

Resource consumption

Analyst workload

---

# 14. Evidence Collection

Each validation shall collect

Sigma Rule ID

Simulation ID

Detection Timestamp

Telemetry Source

Matching Events

Screenshots

Splunk Search

Raw Events

Analyst Notes

Evidence Hash

---

# 15. Required Documentation

Each rule shall have

Rule Description

Detection Objective

MITRE Mapping

Validation Results

Expected Behavior

Observed Behavior

False Positive Analysis

False Negative Analysis

Recommended Improvements

---

# 16. Version Control

Each rule shall maintain

Initial Version

Revision History

Validation Date

Reviewer

Approver

Deployment Status

Retirement Date

---

# 17. Success Metrics

Detection engineering quality shall measure

Detection Accuracy

False Positive Rate

False Negative Rate

Coverage %

ATT&CK Coverage

Mean Detection Time

Analyst Investigation Time

Rule Stability

Telemetry Availability

Validation Success Rate

---

# 18. Deliverables

This standard supports creation of

- Sigma Rules
- Detection Validation Reports
- Coverage Assessments
- ATT&CK Coverage Matrix
- Detection Register
- Validation Evidence Register
- Purple Team Reports
- SOC Detection Content
- Executive Detection Metrics

---

# 19. Expected Outputs

Implementation of this standard produces

- repeatable Sigma engineering
- portable detection content
- measurable ATT&CK coverage
- high-confidence detections
- lower analyst fatigue
- evidence-backed validation
- enterprise-ready detection libraries
- production-quality SOC content
- continuous detection improvement

---

# 20. Conclusion

The Sigma Rule Development Standard establishes a structured engineering methodology for producing high-quality, evidence-backed detection content. By integrating 
threat intelligence, ATT&CK mapping, telemetry validation, Purple Team testing, and continuous tuning, the Lighthouse Technology Enterprise Security Evolution program 
ensures every detection rule is portable, reproducible, and operationally effective across modern enterprise and MSSP environments.
