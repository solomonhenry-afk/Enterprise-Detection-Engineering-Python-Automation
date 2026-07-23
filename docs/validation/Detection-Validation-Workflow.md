# Detection Validation Workflow

**Document ID:** LHT-D5-DVW-001 
**Project:** Lighthouse Technology – Enterprise Security Evolution 
**Domain:** Domain 5 – Enterprise Active Directory Penetration Testing & Security Auditing 
**Phase:** Phase F – Safe Purple Team Validation 
**Version:** 1.0 
**Status:** Approved 
**Classification:** Internal Use 
**Security Assessor:** Bassey Solomon Henry 
**Reviewer:** Lighthouse Technology Security Team

---

# 1. Purpose

This workflow defines the standardized process for validating enterprise security detections during Purple Team exercises.

The objective is to verify that simulated attacker activity generates the expected telemetry, is successfully collected by monitoring infrastructure, produces accurate detection logic, and results in actionable security findings supported by evidence.

Rather than focusing solely on attack execution, this workflow emphasizes defensive visibility, telemetry quality, detection accuracy, evidence integrity, and continuous improvement of enterprise monitoring capabilities.

---

# 2. Objectives

This workflow enables the assessment team to:

- Validate security monitoring effectiveness.
- Measure detection coverage.
- Confirm telemetry collection.
- Verify SIEM alert generation.
- Assess detection accuracy.
- Measure false positives and false negatives.
- Evaluate analyst visibility.
- Produce repeatable engineering evidence.
- Improve detection engineering maturity.

---

# 3. Scope

The workflow applies to validation activities involving:

- Active Directory
- Windows Servers
- Windows Workstations
- Domain Controllers
- Privileged Accounts
- Service Accounts
- Kerberos
- NTLM
- LDAP
- SMB
- DNS
- Group Policy
- Sysmon
- Windows Event Logs
- Splunk Enterprise
- pfSense
- Suricata IDS

---

# 4. Detection Validation Lifecycle

Every validation exercise follows the same engineering workflow.

```
Validation Planning
        │
        ▼
Attack Simulation
        │
        ▼
Telemetry Generation
        │
        ▼
Log Collection
        │
        ▼
Normalization
        │
        ▼
Detection Execution
        │
        ▼
Alert Generation
        │
        ▼
Evidence Collection
        │
        ▼
Correlation
        │
        ▼
Coverage Analysis
        │
        ▼
Validation Report
```

This workflow ensures every simulated activity can be traced from execution through detection and reporting.

---

# 5. Phase 1 — Validation Planning

Activities:

- Define assessment objective.
- Select ATT&CK technique.
- Identify target systems.
- Verify authorization.
- Prepare rollback procedures.
- Confirm telemetry readiness.

Outputs:

- Validation Plan
- Approved Scope
- Testing Schedule

---

# 6. Phase 2 — Attack Simulation

Controlled simulations may include:

- Authentication attempts
- Privilege changes
- Kerberos activity
- NTLM authentication
- Administrative logons
- Service account usage
- LDAP enumeration
- SMB access
- Group membership changes

All simulations must remain within the approved laboratory environment.

Outputs:

- Simulation Log
- Execution Timeline
- Command History

---

# 7. Phase 3 — Telemetry Generation

Expected telemetry sources include:

- Windows Security Events
- Sysmon Events
- PowerShell Logs
- Active Directory Logs
- Kerberos Logs
- NTLM Events
- DNS Events
- SMB Events
- Firewall Logs
- IDS Alerts

Telemetry should accurately represent the simulated activity.

---

# 8. Phase 4 — Log Collection

Security telemetry shall be collected through approved monitoring systems.

Primary collectors include:

- Splunk Universal Forwarder
- Windows Event Forwarding
- Sysmon
- pfSense
- Suricata IDS

Validation confirms:

- Event delivery
- Timestamp accuracy
- Source attribution
- Event completeness

---

# 9. Phase 5 — Evidence Normalization

Collected telemetry shall be normalized into standardized datasets.

Normalization activities include:

- Field mapping
- Timestamp validation
- Identity normalization
- Asset normalization
- Event categorization
- ATT&CK mapping
- Severity assignment
- Validation metadata

Normalized datasets support consistent reporting and correlation.

---

# 10. Phase 6 — Detection Execution

Detection logic shall evaluate normalized telemetry using approved rules.

Detection methods may include:

- SIEM correlation searches
- Event correlation
- Behavioral analytics
- Authentication monitoring
- Privilege monitoring
- Identity analytics
- Threshold detection
- Rule-based detection

Detection logic shall be documented and reproducible.

---

# 11. Phase 7 — Alert Validation

Each generated alert shall be reviewed to confirm:

- Correct triggering event.
- Accurate severity.
- Correct asset identification.
- Identity attribution.
- ATT&CK mapping.
- Supporting evidence.
- Investigation value.

Alerts lacking sufficient evidence shall be reviewed for tuning.

---

# 12. Phase 8 — Evidence Collection

Evidence collected during validation shall include:

- Alert screenshots
- Event logs
- SIEM searches
- Detection rules
- Analyst notes
- Timeline
- Validation status
- Supporting datasets

Every finding shall be supported by reproducible evidence.

---

# 13. Phase 9 — Evidence Correlation

Correlation activities connect:

Attack Activity

↓

Telemetry

↓

Normalized Dataset

↓

Detection Rule

↓

Alert

↓

Finding

↓

Recommendation

↓

Remediation

↓

Validation Result

This establishes complete evidence lineage.

---

# 14. Phase 10 — Detection Coverage Assessment

Coverage shall be measured by evaluating:

- Events observed.
- Events detected.
- Events missed.
- Alert quality.
- False positives.
- False negatives.
- ATT&CK coverage.
- Data completeness.
- Investigation readiness.

Coverage metrics support future detection improvements.

---

# 15. Detection Quality Metrics

Detection effectiveness should be evaluated using:

| Metric | Description |
|----------|-------------|
| Detection Rate | Percentage of simulated attacks successfully detected |
| False Positive Rate | Benign activity incorrectly detected |
| False Negative Rate | Malicious activity not detected |
| Time to Detect | Time from activity to alert generation |
| Alert Accuracy | Correct classification of activity |
| Correlation Quality | Ability to link related events |
| Evidence Completeness | Availability of supporting artifacts |

---

# 16. ATT&CK Alignment

Every validation exercise shall document:

- ATT&CK Tactic
- ATT&CK Technique
- ATT&CK Sub-technique
- Detection Rule
- Telemetry Source
- Defensive Control
- Detection Status

This enables standardized reporting across enterprise assessments.

---

# 17. Success Criteria

A detection validation exercise is successful when:

- The simulation executes as planned.
- Expected telemetry is generated.
- Logs are successfully collected.
- Detection rules execute correctly.
- Alerts are produced.
- Evidence is complete.
- ATT&CK mapping is documented.
- Findings support remediation decisions.

---

# 18. Deliverables

This workflow produces:

- Detection Validation Report
- Telemetry Assessment
- Detection Coverage Matrix
- ATT&CK Mapping
- Validation Evidence Register
- Detection Findings
- Remediation Recommendations
- Executive Summary

---

# 19. Continuous Improvement

Results from each validation exercise should be used to improve:

- Detection logic
- SIEM correlation rules
- Telemetry collection
- Event normalization
- Alert quality
- Coverage metrics
- Investigation workflows
- Purple Team methodology

Detection engineering should evolve as new attack techniques and defensive capabilities emerge.

---

# 20. Related Documents

Methodology:

- Purple-Team-Validation-Methodology.md
- Validation-Safety-Standard.md
- Evidence-Correlation-Methodology.md
- Telemetry-Collection-Runbook.md

Normalized Datasets:

- LHT-PurpleTeam-Normalized.csv
- LHT-DetectionValidation-Normalized.csv
- LHT-Telemetry-Normalized.csv
- LHT-DetectionCoverage-Normalized.csv
- LHT-AttackSimulation-Normalized.csv
- LHT-Validation-Metadata.csv

Templates:

- LHT-Detection-Validation-Template.md
- LHT-PurpleTeam-Assessment-Template.md
- LHT-Telemetry-Assessment-Template.md
- LHT-Coverage-Assessment-Template.md
- LHT-Attack-Simulation-Template.md

Evidence Registers:

- LHT-Validation-Evidence-Register.csv
- LHT-Detection-Checklist.csv
- LHT-PurpleTeam-Checklist.csv
- LHT-Telemetry-Checklist.csv
- LHT-Coverage-Checklist.csv

---

# 21. Document Approval

| Role | Name |
|------|------|
| Security Assessor | Bassey Solomon Henry |
| Reviewer | Lighthouse Technology Security Team |
| Status | Approved |
| Version | 1.0 |

---
