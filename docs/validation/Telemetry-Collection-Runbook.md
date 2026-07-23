# Telemetry Collection Runbook

**Document ID:** LHT-D5-TCR-001 
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

This runbook defines the standardized operational procedures for collecting, validating, preserving, and documenting security telemetry during Purple Team validation activities.

The objective is to ensure telemetry generated throughout controlled attack simulations is complete, accurate, reproducible, and suitable for detection engineering, investigation, evidence correlation, and governance reporting.

This runbook establishes repeatable operational procedures supporting enterprise security monitoring and evidence engineering.

---

# 2. Objectives

The telemetry collection process aims to:

- Capture complete security telemetry.
- Verify monitoring readiness before validation.
- Preserve evidence integrity.
- Ensure timestamp consistency.
- Support detection engineering.
- Enable ATT&CK-aligned analysis.
- Produce normalized datasets.
- Support incident investigations.
- Maintain repeatable evidence collection procedures.

---

# 3. Scope

This runbook applies to telemetry collected from:

- Active Directory
- Domain Controllers
- Windows Servers
- Windows Workstations
- Administrative Workstations
- Service Accounts
- Privileged Accounts
- Splunk Enterprise
- Sysmon
- Windows Security Event Logs
- PowerShell Logging
- pfSense Firewall
- Suricata IDS
- DNS
- LDAP
- SMB
- Kerberos
- NTLM
- Group Policy

---

# 4. Telemetry Collection Principles

Telemetry collection shall follow these principles:

- Complete visibility.
- Accurate timestamps.
- Minimal operational impact.
- Standardized collection.
- Repeatability.
- Evidence integrity.
- Secure storage.
- Full traceability.

---

# 5. Telemetry Collection Workflow

Every validation exercise shall follow the workflow below.

```
Prepare Environment
        │
        ▼
Verify Monitoring
        │
        ▼
Execute Validation
        │
        ▼
Generate Telemetry
        │
        ▼
Collect Logs
        │
        ▼
Validate Collection
        │
        ▼
Normalize Data
        │
        ▼
Store Evidence
        │
        ▼
Correlate Findings
        │
        ▼
Generate Report
```

---

# 6. Pre-Collection Activities

Prior to every validation exercise:

- Confirm assessment authorization.
- Verify target systems.
- Synchronize system clocks.
- Confirm Splunk connectivity.
- Verify Sysmon status.
- Verify Windows Event Logging.
- Confirm Universal Forwarder connectivity.
- Verify firewall logging.
- Verify IDS monitoring.
- Confirm evidence repository availability.

No validation activity shall begin until telemetry readiness has been confirmed.

---

# 7. Telemetry Sources

Primary telemetry sources include:

## Identity Telemetry

- User Logons
- Logoff Events
- Account Lockouts
- Authentication Failures
- Password Changes
- Group Membership Changes
- Privileged Logons

---

## Authentication Telemetry

- Kerberos Events
- NTLM Authentication
- Ticket Requests
- Ticket Renewals
- Service Ticket Activity
- Credential Validation

---

## Endpoint Telemetry

Collected using Sysmon:

- Process Creation
- Process Termination
- Network Connections
- Image Loads
- Driver Loads
- Registry Activity
- File Creation
- DNS Queries

---

## Windows Security Events

Examples include:

- Logon Events
- Account Management
- Security Group Changes
- Policy Changes
- Privilege Use
- Object Access
- Audit Policy Changes

---

## Network Telemetry

Collected from:

- pfSense
- Suricata IDS
- DNS
- SMB
- LDAP
- Kerberos
- Firewall Logs

---

# 8. Collection Validation

After telemetry collection verify:

- Event completeness.
- Correct timestamps.
- Source attribution.
- Asset identification.
- Identity information.
- Event categorization.
- ATT&CK relevance.
- Successful forwarding to Splunk.

Incomplete telemetry shall be investigated before continuing.

---

# 9. Telemetry Quality Assessment

Telemetry shall be evaluated for:

| Quality Attribute | Description |
|-------------------|-------------|
| Completeness | Required events successfully collected |
| Accuracy | Events accurately represent observed activity |
| Consistency | Standardized field values |
| Integrity | No evidence modification |
| Timeliness | Events received within expected timeframe |
| Traceability | Events linked to originating systems |
| Reliability | Stable telemetry throughout validation |

---

# 10. Normalization

Collected telemetry shall be normalized before analysis.

Normalization activities include:

- Timestamp standardization.
- Identity normalization.
- Asset normalization.
- Event classification.
- Severity assignment.
- ATT&CK mapping.
- Validation metadata.
- Evidence identifiers.

Normalized datasets support consistent engineering analysis.

---

# 11. Evidence Storage

Collected telemetry shall be stored using standardized repositories.

Example structure:

```
evidence/
└── validation/
    ├── proposed/
    ├── collected/
    ├── validated/
    └── remediated/
```

Evidence shall remain immutable after validation.

---

# 12. Metadata Requirements

Every telemetry record should include:

- Evidence ID
- Validation ID
- Collection Date
- Collection Time
- Source System
- Hostname
- Identity
- Event ID
- Event Category
- Collection Method
- Analyst
- Validation Status
- Related Dataset

---

# 13. Evidence Integrity

Integrity controls include:

- Immutable timestamps.
- Controlled storage.
- Standardized filenames.
- Version control.
- Chain of custody.
- Validation records.
- Audit logging.

Evidence integrity shall be maintained throughout the assessment lifecycle.

---

# 14. Common Collection Issues

Potential issues include:

- Missing Sysmon events.
- Windows logging disabled.
- Forwarder communication failures.
- Time synchronization problems.
- Duplicate events.
- Incomplete event forwarding.
- Missing authentication logs.
- Network connectivity interruptions.

Each issue shall be documented and resolved before assessment completion.

---

# 15. Success Criteria

Telemetry collection is considered successful when:

- Required telemetry is generated.
- Monitoring systems remain operational.
- Events are successfully collected.
- Data normalization is completed.
- Evidence integrity is preserved.
- ATT&CK mapping is supported.
- Detection engineering receives complete telemetry.

---

# 16. Deliverables

This runbook supports production of:

- Telemetry Collection Log
- Evidence Register
- Validation Timeline
- Detection Inputs
- ATT&CK Mapping
- Investigation Artifacts
- Normalized Datasets
- Executive Reporting Evidence

---

# 17. Continuous Improvement

Following each validation exercise, telemetry collection should be reviewed to improve:

- Event coverage.
- Log quality.
- Collection reliability.
- Detection visibility.
- Correlation accuracy.
- Automation opportunities.
- Documentation quality.

Operational improvements shall be incorporated into future assessments.

---

# 18. Related Documents

Methodology

- Purple-Team-Validation-Methodology.md
- Validation-Safety-Standard.md
- Detection-Validation-Workflow.md
- Evidence-Correlation-Methodology.md

Normalized Datasets

- LHT-PurpleTeam-Normalized.csv
- LHT-DetectionValidation-Normalized.csv
- LHT-Telemetry-Normalized.csv
- LHT-DetectionCoverage-Normalized.csv
- LHT-AttackSimulation-Normalized.csv
- LHT-Validation-Metadata.csv

Templates

- LHT-PurpleTeam-Assessment-Template.md
- LHT-Detection-Validation-Template.md
- LHT-Telemetry-Assessment-Template.md
- LHT-Coverage-Assessment-Template.md
- LHT-Attack-Simulation-Template.md

Evidence Registers

- LHT-Validation-Evidence-Register.csv
- LHT-PurpleTeam-Checklist.csv
- LHT-Telemetry-Checklist.csv
- LHT-Detection-Checklist.csv
- LHT-Attack-Simulation-Checklist.csv
- LHT-Coverage-Checklist.csv

---

# 19. Document Approval

| Role | Name |
|------|------|
| Security Assessor | Bassey Solomon Henry |
| Reviewer | Lighthouse Technology Security Team |
| Status | Approved |
| Version | 1.0 |

---
