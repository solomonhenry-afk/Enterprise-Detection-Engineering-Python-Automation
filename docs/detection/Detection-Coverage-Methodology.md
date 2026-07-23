# Detection Coverage Methodology

**Document ID:** LHT-DET-METH-004 
**Project:** Lighthouse Technology – Enterprise Security Evolution 
**Domain:** Domain 5 – Enterprise Active Directory Penetration Testing & Security Auditing 
**Phase:** G – Detection Engineering & Coverage Measurement 
**Version:** 1.0 
**Status:** Approved

---

# 1. Purpose

This methodology defines the standardized process used to measure, analyze, validate, and continuously improve security detection coverage across the Lighthouse Technology enterprise security environment.

Rather than simply counting alerts, detection coverage measures whether enterprise telemetry can reliably detect adversary behavior throughout the attack lifecycle while minimizing detection gaps.

Coverage analysis provides measurable evidence that security controls produce observable, validated security telemetry.

---

# 2. Objectives

The objectives of Detection Coverage Measurement are to:

- Measure visibility across the ATT&CK attack lifecycle
- Identify detection gaps
- Validate monitoring effectiveness
- Verify telemetry availability
- Measure detection quality
- Evaluate investigation readiness
- Support Purple Team validation
- Prioritize engineering improvements
- Produce executive reporting metrics

---

# 3. Coverage Philosophy

Detection coverage is evaluated using four layers.

Layer 1

Telemetry Coverage

Can the activity be logged?

Layer 2

Detection Coverage

Can the SIEM detect it?

Layer 3

Analyst Coverage

Can an analyst investigate it?

Layer 4

Response Coverage

Can containment actions be initiated?

---

# 4. Coverage Measurement Model

Each ATT&CK technique is evaluated using standardized criteria.

Example

Technique

Credential Dumping

Telemetry

Sysmon Event ID 10

Detection Rule

Splunk Analytics

Investigation Playbook

Credential Investigation Guide

Coverage Status

Covered

Confidence

High

Validation Status

Validated

---

# 5. Coverage Categories

Every detection is classified.

## Fully Covered

Required telemetry exists

Detection rule exists

Validated successfully

Investigation documented

Response available

---

## Partially Covered

Telemetry available

Detection incomplete

Limited investigation capability

Requires tuning

---

## Telemetry Only

Logs collected

No detection rule

No alert

Gap identified

---

## Detection Gap

No telemetry

No detection

No visibility

Engineering required

---

## False Positive Risk

Detection exists

Produces excessive alerts

Requires tuning

---

## False Negative Risk

Attack executed

Detection missed activity

Coverage improvement required

---

# 6. Coverage Dimensions

Coverage analysis includes:

Identity

Authentication

Privilege Escalation

Credential Access

Persistence

Lateral Movement

Execution

Discovery

Defense Evasion

Collection

Command and Control

Exfiltration

Impact

Cloud Activity

Network Activity

Endpoint Activity

---

# 7. MITRE ATT&CK Alignment

Every detection is mapped to:

ATT&CK Tactic

ATT&CK Technique

ATT&CK Sub-technique

Data Source

Detection Logic

Severity

Coverage Status

Validation Evidence

Residual Risk

---

# 8. Coverage Validation Process

Step 1

Execute approved Purple Team simulation.

↓

Step 2

Collect telemetry.

↓

Step 3

Verify telemetry integrity.

↓

Step 4

Execute SIEM detections.

↓

Step 5

Confirm alert generation.

↓

Step 6

Investigate generated alerts.

↓

Step 7

Record validation evidence.

↓

Step 8

Assign coverage rating.

↓

Step 9

Document engineering recommendations.

---

# 9. Coverage Scoring

Each detection receives a normalized score.

Example

Telemetry Availability

25 Points

Detection Accuracy

25 Points

Investigation Readiness

20 Points

False Positive Rate

10 Points

False Negative Rate

10 Points

Response Capability

10 Points

Total

100 Points

Coverage Rating

95–100

Excellent

80–94

Strong

60–79

Moderate

40–59

Limited

Below 40

Poor

---

# 10. Detection Gap Analysis

Every uncovered technique is documented with:

Missing telemetry

Missing logs

Missing SIEM rule

Missing ATT&CK mapping

Missing playbook

Missing analyst guidance

Missing response workflow

Required engineering actions

---

# 11. Coverage Metrics

Metrics include:

Coverage %

Detection Success Rate

Detection Accuracy

False Positive Rate

False Negative Rate

Alert Fidelity

Investigation Readiness

Mean Time to Detect (MTTD)

Mean Time to Investigate (MTTI)

Mean Time to Validate

Telemetry Completeness

Evidence Completeness

Engineering Backlog

Coverage Growth

MITRE Technique Coverage

---

# 12. Evidence Collection

Evidence collected includes:

Splunk searches

Windows Event Logs

Sysmon Events

PowerShell Logs

Security Alerts

Detection Results

Timeline Correlation

ATT&CK Mapping

Validation Screenshots

Simulation Results

Analyst Notes

Coverage Reports

---

# 13. Deliverables

This methodology produces:

Detection Coverage Register

Coverage Matrix

Detection Validation Report

Coverage Dashboard

Coverage Metrics

ATT&CK Coverage Map

Gap Analysis Report

Engineering Recommendations

Executive Coverage Summary

---

# 14. Quality Assurance

Coverage assessments require:

Evidence validation

Independent verification

Repeatable execution

Analyst review

Detection tuning review

Peer approval

Document version control

Evidence integrity validation

---

# 15. Continuous Improvement

Coverage measurement is iterative.

Every validation cycle shall:

Improve telemetry

Improve detections

Reduce false positives

Reduce false negatives

Expand ATT&CK coverage

Improve analyst investigations

Improve automation

Strengthen enterprise visibility

Increase overall detection maturity

---

# 16. Expected Outputs

Successful execution of this methodology produces:

- Enterprise Detection Coverage Matrix
- MITRE ATT&CK Coverage Assessment
- Detection Gap Register
- Detection Quality Metrics
- Coverage Validation Report
- Coverage Improvement Roadmap
- Detection Engineering Backlog
- Executive Coverage Dashboard
- Evidence Package for Purple Team Validation

These outputs provide measurable assurance that enterprise security controls generate reliable, validated, and actionable detections capable of supporting threat 
detection, incident response, and continuous security improvement.
