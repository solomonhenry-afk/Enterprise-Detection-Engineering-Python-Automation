# Detection Tuning Methodology

**Document ID:** LHT-DET-METH-003 
**Project:** Lighthouse Technology – Enterprise Security Evolution 
**Phase:** G – Detection Engineering & Coverage Measurement 
**Domain:** Domain 5 – Enterprise Active Directory Penetration Testing & Security Auditing 
**Classification:** Internal – Detection Engineering Standard 
**Version:** 1.0

---

# 1. Purpose

This methodology defines the standardized process for tuning security detections after initial deployment to maximize detection fidelity while minimizing false positives and false negatives.

Detection tuning is a continuous engineering process that improves the operational effectiveness of a Security Operations Center (SOC) by ensuring alerts remain actionable, accurate, and aligned with current enterprise behavior.

---

# 2. Objectives

The tuning process aims to:

- Increase True Positive Rate (TPR)
- Reduce False Positive Rate (FPR)
- Minimize False Negatives
- Improve analyst efficiency
- Reduce alert fatigue
- Improve Mean Time To Detect (MTTD)
- Improve Mean Time To Respond (MTTR)
- Maintain ATT&CK coverage accuracy

---

# 3. Scope

Applies to:

- Splunk Detection Rules
- Sigma Rules
- Sysmon-based detections
- Windows Event detections
- Active Directory detections
- Suricata IDS alerts
- Firewall detections
- Endpoint detections
- Authentication detections
- Purple Team validation scenarios

---

# 4. Detection Lifecycle

```
Detection Created
        │
        ▼
Lab Validation
        │
        ▼
Purple Team Execution
        │
        ▼
Telemetry Review
        │
        ▼
False Positive Analysis
        │
        ▼
Rule Optimization
        │
        ▼
Revalidation
        │
        ▼
Production Candidate
        │
        ▼
Continuous Monitoring
```

---

# 5. Detection Quality Metrics

Each detection should be measured using standardized engineering metrics.

| Metric | Purpose |
|----------|----------|
| True Positives | Correct malicious detections |
| False Positives | Benign activity incorrectly alerted |
| False Negatives | Missed malicious activity |
| Precision | Alert accuracy |
| Recall | Detection completeness |
| Detection Latency | Time from event to alert |
| Alert Volume | Number of alerts generated |
| Analyst Validation Time | Investigation effort |
| ATT&CK Coverage | Technique mapping completeness |

---

# 6. Detection Tuning Workflow

## Phase 1

Collect detection telemetry.

Sources include

- Splunk
- Sysmon
- Windows Security Logs
- PowerShell Logs
- Suricata Alerts
- Firewall Logs
- Endpoint Events

---

## Phase 2

Execute known attack simulation.

Examples include

- Kerberoasting
- Pass-the-Hash
- Golden Ticket
- NTLM Authentication
- PowerShell Execution
- Lateral Movement
- Privilege Escalation

---

## Phase 3

Review generated alerts.

Validate:

- Alert accuracy
- Event correlation
- Required fields present
- ATT&CK mapping
- User context
- Host context

---

## Phase 4

Identify false positives.

Common examples

Administrative activity

Scheduled tasks

Backup software

Monitoring agents

Security scanners

Software deployment

System maintenance

---

## Phase 5

Identify false negatives.

Questions

Was telemetry collected?

Was logging enabled?

Was Sysmon configured?

Was the rule too restrictive?

Did field mapping fail?

Were timestamps synchronized?

---

## Phase 6

Modify detection logic.

Possible improvements

Additional conditions

Whitelist trusted activity

Threshold adjustments

Behavioral correlation

Process ancestry

User risk context

Asset criticality

Time-of-day logic

---

## Phase 7

Execute simulation again.

Detection must consistently identify:

- malicious behavior
- required ATT&CK technique
- correct host
- correct user
- correct timestamp

---

## Phase 8

Approve for production.

Detection enters continuous monitoring.

---

# 7. False Positive Reduction Strategy

## Validate Asset Context

Consider

- Domain Controllers
- Servers
- Workstations
- Administrative Systems

---

## Validate User Context

Differentiate

- Domain Admin
- Service Account
- Helpdesk
- Standard User
- Scheduled Task

---

## Validate Process Context

Examples

Expected

```
services.exe
lsass.exe
svchost.exe
```

Unexpected

```
powershell.exe
rundll32.exe
regsvr32.exe
certutil.exe
mshta.exe
```

---

## Validate Time Context

Examples

Business hours

Maintenance window

After-hours execution

Weekend activity

---

# 8. False Negative Reduction Strategy

Review:

Logging enabled

Sysmon configuration

Splunk ingestion

Forwarders

Field extraction

Correlation searches

Lookup tables

Asset inventory

Detection dependencies

---

# 9. ATT&CK Validation

Every tuned detection must map to ATT&CK.

Example

| Detection | ATT&CK |
|------------|---------|
| Kerberoasting | T1558.003 |
| Pass-the-Hash | T1550.002 |
| PowerShell | T1059.001 |
| Credential Dumping | T1003 |
| Lateral Movement | T1021 |
| Scheduled Task | T1053 |

---

# 10. Detection Tuning Decision Matrix

| Finding | Action |
|----------|---------|
| High False Positives | Tune immediately |
| Low Severity | Review during maintenance |
| Missing Telemetry | Improve logging |
| Incorrect Mapping | Update ATT&CK |
| Missing Context | Improve enrichment |
| Excessive Alerts | Threshold adjustment |

---

# 11. Validation Evidence

Evidence collected includes

Detection rule

Raw logs

Splunk search

Alert screenshot

Sysmon event

Windows Event

IDS alert

Timeline

ATT&CK mapping

Evidence hash

Evidence manifest

---

# 12. Success Criteria

A tuned detection should demonstrate

✓ High confidence

✓ Repeatable validation

✓ Low false positives

✓ Low false negatives

✓ Complete telemetry

✓ ATT&CK alignment

✓ Business context

✓ Analyst-ready alert

✓ Executive reporting compatibility

---

# 13. Deliverables

This methodology produces:

- Detection Validation Reports
- Detection Coverage Matrix
- Detection Performance Metrics
- False Positive Analysis
- False Negative Analysis
- ATT&CK Coverage Assessment
- Detection Improvement Recommendations
- Purple Team Validation Evidence
- SOC Readiness Assessment
- Continuous Detection Improvement Register

---

# 14. Integration with Enterprise Security Evolution

This methodology integrates directly with:

**Phase A**
- Assessment Architecture

**Phase B**
- Evidence Framework

**Phase C**
- Enterprise Asset Inventory

**Phase D**
- Identity Exposure Analysis

**Phase E**
- Authentication Security Assessment

**Phase F**
- Purple Team Validation

**Phase G**
- Detection Engineering

**Phase H**
- Detection Improvement

**Phase I**
- Executive Reporting

**Task 2**
- Hands-on Adversary Simulation & Detection Engineering

Detection tuning serves as the continuous feedback mechanism between controlled adversary simulations and production-ready security monitoring, ensuring validated 
detections remain accurate, resilient, and aligned with evolving enterprise threats.
