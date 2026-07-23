# Lighthouse Technology
# Enterprise Security Evolution
## Domain 5 — Enterprise Active Directory Penetration Testing & Security Auditing

# Detection Lifecycle Standard

**Document ID:** LHT-DL-001
**Version:** 1.0
**Classification:** Internal
**Owner:** Detection Engineering
**Phase:** G — Detection Engineering & Coverage Measurement

---

# 1. Purpose

This document defines the standardized lifecycle used to design, validate, deploy, monitor, maintain, and retire security detections throughout the Lighthouse Technology Enterprise Security Evolution program.

The objective is to ensure every detection:

- originates from a documented security problem
- maps to attacker behavior
- is supported by validated telemetry
- minimizes false positives
- produces actionable analyst investigations
- maintains complete evidence lineage

---

# 2. Objectives

The Detection Lifecycle enables:

- Repeatable engineering
- Consistent rule quality
- ATT&CK alignment
- Traceable evidence
- Continuous improvement
- Operational governance

---

# 3. Lifecycle Overview

```
Threat Intelligence
        │
        ▼
Detection Opportunity
        │
        ▼
Telemetry Validation
        │
        ▼
Rule Engineering
        │
        ▼
Lab Validation
        │
        ▼
False Positive Review
        │
        ▼
Coverage Mapping
        │
        ▼
Deployment
        │
        ▼
Operational Monitoring
        │
        ▼
Continuous Improvement
        │
        ▼
Retirement
```

---

# Stage 1 — Threat Identification

Sources include:

- MITRE ATT&CK
- CVEs
- Security Advisories
- Purple Team findings
- Threat Intelligence
- Internal incidents
- Red Team assessments

Deliverables

- Threat description
- ATT&CK mapping
- Detection objective
- Risk assessment

Evidence

- Threat reports
- ATT&CK references
- Research notes

---

# Stage 2 — Detection Opportunity Analysis

Determine:

Can this behavior be detected?

Questions

What activity occurs?

Which logs capture it?

Which systems generate evidence?

Can multiple telemetry sources validate it?

Output

Detection Opportunity Record

---

# Stage 3 — Telemetry Validation

Required telemetry may include

Windows Security Logs

Sysmon

PowerShell

DNS

Firewall

Suricata

Active Directory

LDAP

Kerberos

NTLM

Network Flow

Splunk Universal Forwarders

Objectives

Validate:

Completeness

Accuracy

Integrity

Availability

Time synchronization

Evidence

Telemetry validation report

---

# Stage 4 — Rule Engineering

Develop

Detection Logic

Components

Trigger conditions

Field mappings

Thresholds

Filters

Exceptions

Severity

Risk score

MITRE mapping

Rule metadata

Output

Detection Rule

Supported Formats

Sigma

Splunk SPL

KQL

EDR

SOAR

---

# Stage 5 — Controlled Validation

Execute detection inside the authorized lab.

Validation methods

Purple Team simulation

Atomic tests

Manual execution

Replay datasets

Known attack traces

Expected Results

Detection fires

Evidence collected

Telemetry complete

Alert generated

Investigation initiated

Evidence

Screenshots

Search results

Logs

Validation records

---

# Stage 6 — False Positive Review

Evaluate

False positives

False negatives

Noise

Duplicate alerts

Rule efficiency

Measure

Precision

Recall

Detection confidence

Analyst effort

Required Improvements

Threshold tuning

Additional conditions

Context enrichment

Allow lists

Suppression logic

---

# Stage 7 — Coverage Mapping

Map detection to

MITRE ATT&CK

Kill Chain

Security Controls

Business Assets

Identity

Cloud

Network

Coverage Categories

Prevented

Detected

Partially Detected

Not Covered

Output

Coverage Matrix

Coverage Heat Map

---

# Stage 8 — Deployment

Deploy into production SIEM.

Deployment checklist

Peer reviewed

Approved

Versioned

Documented

Rollback plan

Performance tested

Monitoring enabled

---

# Stage 9 — Operational Monitoring

Monitor

Alert volume

Rule health

Performance

False positive trends

Detection gaps

Analyst feedback

Metrics

Alerts/day

MTTD

False Positive Rate

Precision

Recall

Coverage %

Analyst investigation time

---

# Stage 10 — Continuous Improvement

Improve detections using

Purple Team exercises

Threat intelligence

Emerging CVEs

ATT&CK updates

Incident lessons learned

Customer feedback

SOC feedback

Review Frequency

Monthly

Quarterly

Following incidents

After major ATT&CK updates

---

# Stage 11 — Retirement

Retire detections when

Technology removed

Threat obsolete

Rule replaced

Unsupported telemetry

Duplicate detection

Retirement Requirements

Document reason

Archive evidence

Update coverage matrix

Maintain history

---

# Detection Metadata

Each rule should include

Detection ID

Rule Name

Author

Version

Date Created

Last Updated

Status

ATT&CK Techniques

Severity

Priority

Risk Score

Log Sources

Platforms

Detection Type

Validation Status

Coverage Status

Owner

---

# Detection Quality Gates

A rule progresses only after meeting each quality gate.

| Stage | Validation Required |
|---------|---------------------|
| Threat Identified | Threat documented |
| Telemetry Validated | Logs verified |
| Rule Developed | Logic complete |
| Lab Tested | Successful detection |
| Tuned | False positives acceptable |
| Coverage Mapped | ATT&CK mapping complete |
| Approved | Peer review completed |
| Deployed | Operational monitoring enabled |

---

# Evidence Requirements

Evidence collected throughout the lifecycle includes

Threat research

Detection specifications

Telemetry validation

Rule source code

Sigma rules

Splunk searches

Purple Team results

Coverage reports

Validation screenshots

SOC observations

Tuning history

Version history

Executive summaries

---

# Success Metrics

The lifecycle aims to achieve

High detection accuracy

Reduced false positives

Reduced false negatives

Repeatable validation

Comprehensive ATT&CK coverage

Faster investigations

Improved SOC efficiency

Evidence-backed detection engineering

---

# Deliverables

This lifecycle produces

Detection Register

Detection Coverage Matrix

Sigma Rules

Splunk Detection Library

Validation Reports

Purple Team Results

Evidence Register

MITRE ATT&CK Coverage Matrix

Detection Performance Metrics

Continuous Improvement Recommendations

Executive Reporting Inputs

---

# Relationship to Other Phase G Documents

This lifecycle integrates with:

- Detection-Engineering-Methodology.md
- Detection-UseCase-Development-Standard.md
- Detection-Tuning-Methodology.md
- Detection-Coverage-Methodology.md
- Sigma-Rule-Development-Standard.md
- Splunk-Detection-Engineering-Guide.md
- ATTACK-Coverage-Mapping.md

Together, these documents establish the governance framework for designing, validating, deploying, measuring, and continuously improving enterprise detection 
capabilities within the Lighthouse Technology Enterprise Security Evolution program.
