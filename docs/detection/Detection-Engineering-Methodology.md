# Lighthouse Technology
# Detection Engineering Methodology

Version: 1.0
Project: Enterprise Security Evolution
Domain: Enterprise Active Directory Penetration Testing & Security Auditing
Phase: G — Detection Engineering & Coverage Measurement

---

# 1. Purpose

This methodology defines the engineering process for designing, validating, deploying, and continuously improving security detections throughout the Lighthouse Technology Enterprise Security Evolution program.

The objective is to convert security telemetry into reliable, repeatable, evidence-driven detections capable of identifying malicious activity while minimizing false positives and operational overhead.

The methodology aligns detection engineering with enterprise security operations, Purple Team validation, ATT&CK mapping, governance requirements, and continuous detection improvement.

---

# 2. Objectives

The methodology establishes a standardized process to:

- Identify attack behaviors requiring visibility
- Select appropriate telemetry sources
- Develop detection logic
- Validate detections safely
- Measure detection coverage
- Tune detections
- Document evidence
- Support incident response
- Improve detection maturity

---

# 3. Detection Engineering Lifecycle

The lifecycle consists of eight stages.

1. Threat Research

↓

2. ATT&CK Technique Mapping

↓

3. Telemetry Identification

↓

4. Detection Rule Design

↓

5. Validation

↓

6. False Positive Reduction

↓

7. Coverage Measurement

↓

8. Continuous Improvement

---

# 4. Threat Research

Detection development begins with understanding:

• Threat Actor TTPs

• MITRE ATT&CK

• Known adversary techniques

• Public threat intelligence

• CVEs

• Purple Team observations

• Incident investigations

• Internal security findings

The objective is to understand attacker behavior—not signatures alone.

---

# 5. Detection Requirements

Each detection should answer:

What attack is occurring?

Which attacker behavior is observable?

Which logs capture this activity?

What normal behavior may appear similar?

How will responders investigate it?

How will effectiveness be measured?

---

# 6. Detection Categories

The program develops detections across:

## Identity Security

Examples

Authentication anomalies

Privilege escalation

Kerberos abuse

Golden Ticket activity

Silver Ticket activity

Pass-the-Hash

NTLM abuse

Delegation abuse

Tier Zero access

---

## Endpoint Security

Examples

PowerShell execution

Encoded commands

Sysmon process creation

Registry persistence

Scheduled tasks

Service creation

Credential dumping

LSASS access

WMI abuse

---

## Network Security

Examples

SMB enumeration

Lateral movement

DNS anomalies

Firewall violations

Suspicious LDAP queries

RPC abuse

Remote service creation

RDP anomalies

---

## Active Directory

Examples

ACL abuse

Group modifications

GPO modification

AdminSDHolder

SID History

DCSync

DCSync preparation

Replication abuse

Trust abuse

---

## Infrastructure

Examples

VPN access

Administrative logons

Server authentication

Remote management

Certificate misuse

Privileged service execution

---

# 7. Detection Design

Every detection includes:

Detection ID

Detection Name

Objective

ATT&CK Technique

Severity

Telemetry Sources

Detection Logic

Required Fields

Validation Method

Expected Output

Known Limitations

False Positive Conditions

False Negative Conditions

Response Guidance

Evidence References

Owner

Review Date

---

# 8. Telemetry Sources

Detection logic may consume:

Windows Security Events

Sysmon

PowerShell Logs

Windows Defender Logs

Firewall Logs

Suricata Alerts

DNS Logs

Active Directory Logs

LDAP Events

Kerberos Events

NTLM Events

Authentication Logs

Splunk Searches

Sigma Rules

Operating System Logs

---

# 9. Validation Methodology

Every detection must be validated using controlled simulations.

Validation includes:

Safe attack simulation

Expected telemetry generation

Detection execution

Alert verification

Evidence collection

Coverage confirmation

Documentation

False-positive review

False-negative review

---

# 10. Detection Quality

Detection quality is evaluated using:

Accuracy

Precision

Coverage

Noise

Completeness

Response usefulness

Investigation value

Operational cost

---

# 11. False Positive Reduction

Each detection is tuned through:

Baseline analysis

Environment profiling

User behavior review

Known administrative activity

Service account exclusions

Infrastructure exclusions

Frequency analysis

Behavioral correlation

Threat correlation

---

# 12. Coverage Measurement

Coverage is measured using:

MITRE ATT&CK Techniques

ATT&CK Tactics

Identity coverage

Endpoint coverage

Network coverage

Authentication coverage

Privilege coverage

Cloud coverage

Infrastructure coverage

Detection maturity

---

# 13. Evidence Collection

Each validated detection produces evidence including:

Detection output

Raw logs

Screenshots

Splunk searches

Sigma rules

Alert IDs

Validation timestamps

Evidence hashes

Evidence manifests

Correlation references

---

# 14. Governance

Detection engineering follows:

Evidence Integrity Standard

Reporting Standard

Detection Lifecycle

Validation Safety Standard

Evidence Correlation Methodology

Repository Governance

Version Control

Peer Review

---

# 15. Deliverables

Phase G produces:

Detection Library

Splunk Detection Package

Sigma Rule Package

Coverage Matrix

Detection Validation Reports

Detection Register

Detection Metrics

Telemetry Mapping

Executive Coverage Summary

Technical Assessment Report

---

# 16. Success Criteria

Detection engineering is considered successful when:

Critical ATT&CK techniques are covered.

Validated detections consistently identify simulated attacks.

False positives remain within acceptable operational thresholds.

Detection logic is documented, reproducible, and version controlled.

Evidence supports every detection claim.

Coverage metrics demonstrate measurable improvements.

Detection engineering supports incident response and continuous security improvement.

---

