# Lighthouse Technology
# Enterprise Security Evolution
## Domain 5 — Enterprise Active Directory Penetration Testing & Security Auditing

# Detection Quality Standard

**Document ID:** LHT-DQS-001 
**Version:** 1.0 
**Classification:** Internal 
**Owner:** Detection Engineering & Security Operations 
**Phase:** G — Detection Engineering & Coverage Measurement

---

# 1. Purpose

This standard defines the quality requirements for all detection content developed within the Lighthouse Technology Enterprise Security Evolution program.

The objective is to ensure every detection is technically accurate, evidence-driven, validated through controlled testing, aligned with adversary behavior, and operationally effective within enterprise Security Operations Center (SOC) environments.

---

# 2. Scope

This standard applies to all detection content including:

- Splunk Detection Rules
- Sigma Rules
- SIEM Correlation Searches
- Detection Use Cases
- EDR/XDR Detection Logic
- IDS/IPS Signatures
- Threat Hunting Queries
- Purple Team Detection Validation
- Detection Coverage Assessments

---

# 3. Objectives

Detection quality should ensure:

- Reliable identification of malicious activity
- Minimal false positives
- Minimal false negatives
- Consistent engineering practices
- ATT&CK alignment
- Repeatable validation
- Evidence traceability
- Continuous improvement

---

# 4. Detection Quality Principles

Every detection should be:

### Accurate

Correctly identifies attacker behavior.

---

### Repeatable

Produces consistent results across multiple validation exercises.

---

### Explainable

Detection logic can be understood by analysts.

---

### Actionable

Alerts provide sufficient context for investigation.

---

### Maintainable

Rules are version controlled and regularly reviewed.

---

### Measurable

Performance can be monitored using defined metrics.

---

# 5. Detection Quality Lifecycle

```
Threat Research
       │
       ▼
Detection Design
       │
       ▼
Rule Development
       │
       ▼
Telemetry Validation
       │
       ▼
Purple Team Testing
       │
       ▼
Quality Review
       │
       ▼
Deployment
       │
       ▼
Continuous Improvement
```

---

# 6. Quality Requirements

Every detection must include:

- Detection Objective
- Threat Description
- ATT&CK Mapping
- Required Telemetry
- Detection Logic
- Validation Evidence
- Analyst Guidance
- False Positive Analysis
- False Negative Analysis
- Version History

---

# 7. Detection Completeness

A detection is considered complete when it includes:

| Requirement | Status |
|-------------|--------|
| Threat documented | Required |
| ATT&CK mapped | Required |
| Telemetry validated | Required |
| Detection tested | Required |
| Evidence collected | Required |
| Analyst documentation | Required |
| Rule owner assigned | Required |
| Review schedule defined | Required |

---

# 8. Telemetry Quality

Detection engineering shall verify:

- Log availability
- Timestamp accuracy
- Field normalization
- Event integrity
- Parsing accuracy
- Data completeness
- Time synchronization

Required telemetry may include:

- Windows Security Logs
- Sysmon
- PowerShell Logs
- DNS
- Firewall
- Suricata IDS
- Active Directory
- Azure Logs
- Linux Syslog

---

# 9. Validation Standards

Each detection must undergo:

- Controlled attack simulation
- Expected alert generation
- Manual verification
- Purple Team validation
- Evidence collection
- Peer review

Validation is incomplete without documented evidence.

---

# 10. False Positive Standards

Each rule shall document:

Expected administrative activity

Known maintenance events

Approved software behavior

Automation platforms

Environmental exceptions

Whitelisting decisions

Target false positive rate:

**< 5%** where operationally achievable.

---

# 11. False Negative Standards

Detection engineers should evaluate:

Missing telemetry

Unlogged attack variants

Parser failures

Unsupported attack paths

Configuration weaknesses

Coverage limitations

All identified gaps shall generate remediation recommendations.

---

# 12. Detection Performance Metrics

Measure:

- Detection Accuracy
- Precision
- Recall
- False Positive Rate
- False Negative Rate
- Alert Volume
- Mean Time to Detect (MTTD)
- Mean Time to Respond (MTTR)
- Detection Latency
- Analyst Investigation Time

---

# 13. ATT&CK Coverage

Each detection shall include:

- ATT&CK Tactic
- ATT&CK Technique
- ATT&CK Sub-Technique (where applicable)

Coverage shall be tracked within the enterprise ATT&CK Coverage Matrix.

---

# 14. Documentation Standard

Each detection record shall include:

Detection ID

Detection Name

Description

Owner

Version

Creation Date

Review Date

Status

Severity

Priority

Telemetry Sources

Validation Status

Evidence References

Related Sigma Rule

Related Splunk Search

MITRE ATT&CK Mapping

Analyst Notes

---

# 15. Review and Approval

Every detection shall undergo:

Technical review

Peer validation

Quality assurance review

Detection engineering approval

SOC operational acceptance

Approved detections become eligible for production deployment.

---

# 16. Continuous Improvement

Detection quality shall improve through:

Purple Team exercises

Threat hunting findings

Incident response lessons learned

Threat intelligence updates

MITRE ATT&CK revisions

Analyst feedback

Detection tuning activities

Regular quality assessments

---

# 17. Governance

Detection engineering teams shall maintain:

Detection Register

Version history

Validation records

Evidence register

Coverage matrix

Tuning history

Review schedule

Ownership records

---

# 18. Success Criteria

A high-quality detection should:

- Reliably identify intended adversary behavior
- Produce actionable alerts
- Maintain acceptable false positive rates
- Demonstrate validated ATT&CK coverage
- Be fully documented and evidence-backed
- Support efficient analyst investigations
- Integrate into enterprise detection governance

---

# 19. Deliverables

Implementation of this standard produces:

- Detection Quality Assessments
- Detection Register
- Validation Reports
- Detection Coverage Matrix
- ATT&CK Mapping Register
- Sigma Rule Repository
- Splunk Detection Library
- Rule Tuning Register
- Detection Performance Dashboard
- Executive Detection Metrics

---

# 20. Relationship to Other Phase G Documents

This standard complements:

- Detection-Engineering-Methodology.md
- Detection-UseCase-Development-Standard.md
- Detection-Tuning-Methodology.md
- Detection-Coverage-Methodology.md
- Detection-Lifecycle.md
- Alert-Triage-Workflow.md
- Sigma-Rule-Development-Standard.md
- Splunk-Detection-Engineering-Guide.md
- ATTACK-Coverage-Mapping.md

Together, these documents establish a comprehensive governance framework for enterprise detection engineering, ensuring that detection content is consistent, validated, 
measurable, and continuously improved across the Lighthouse Technology Enterprise Security Evolution program.
