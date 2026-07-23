# Evidence Correlation Methodology

**Document ID:** LHT-D5-ECM-001 
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

This methodology establishes the standardized process for correlating security evidence generated throughout Purple Team validation activities.

The objective is to transform isolated security artifacts into a complete evidence chain that demonstrates how a simulated attack generated telemetry, triggered security detections, produced investigation findings, and ultimately informed remediation decisions.

Evidence correlation ensures every assessment finding is technically verifiable, reproducible, and fully traceable from execution through executive reporting.

---

# 2. Objectives

This methodology enables the assessment team to:

- Establish complete evidence lineage.
- Correlate attack simulations with defensive telemetry.
- Validate SIEM detections.
- Associate findings with supporting evidence.
- Improve investigation efficiency.
- Support governance reporting.
- Maintain evidence integrity.
- Enable repeatable security assessments.
- Produce executive-ready reporting supported by technical evidence.

---

# 3. Scope

This methodology applies to all evidence generated during Phase F, including:

- Purple Team simulations
- Authentication events
- Active Directory logs
- Kerberos activity
- NTLM authentication
- Service account activity
- Privilege changes
- Windows Security Events
- Sysmon telemetry
- Splunk alerts
- IDS alerts
- Firewall logs
- Investigation artifacts
- Assessment findings
- Remediation recommendations

---

# 4. Evidence Correlation Philosophy

Security evidence has little value when viewed in isolation.

The objective of correlation is to establish logical relationships between:

- Simulated attack activity.
- Security telemetry.
- Detection logic.
- Generated alerts.
- Analyst investigation.
- Assessment findings.
- Recommended remediation.
- Executive reporting.

Every conclusion must be supported by observable technical evidence.

---

# 5. Evidence Lifecycle

Evidence progresses through the following lifecycle.

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
Evidence Collection
        │
        ▼
Normalization
        │
        ▼
Correlation
        │
        ▼
Finding Validation
        │
        ▼
Risk Assessment
        │
        ▼
Remediation
        │
        ▼
Executive Reporting
```

This lifecycle establishes end-to-end traceability for every assessment activity.

---

# 6. Evidence Sources

Evidence may originate from multiple enterprise systems.

Typical sources include:

- Active Directory
- Windows Event Logs
- Sysmon
- Splunk Enterprise
- pfSense Firewall
- Suricata IDS
- PowerShell Logs
- Kerberos Authentication Logs
- NTLM Authentication Logs
- LDAP Queries
- SMB Activity
- Group Policy Events
- Security Assessment Scripts
- Validation Checklists
- Analyst Notes

Each evidence source shall be uniquely identifiable.

---

# 7. Correlation Model

Evidence correlation follows a structured engineering model.

```
Attack Activity
        │
        ▼
Target Asset
        │
        ▼
Telemetry Source
        │
        ▼
Normalized Dataset
        │
        ▼
Detection Rule
        │
        ▼
SIEM Alert
        │
        ▼
Investigation
        │
        ▼
Assessment Finding
        │
        ▼
Risk Rating
        │
        ▼
Remediation Recommendation
        │
        ▼
Validation Status
```

This model provides a complete evidence lineage for every finding.

---

# 8. Correlation Attributes

Every correlated finding should include:

- Evidence Identifier
- Validation Identifier
- Assessment Area
- Target Asset
- Identity
- Event Source
- Event Identifier
- Timestamp
- Detection Rule
- Alert Identifier
- ATT&CK Technique
- Analyst
- Risk Rating
- Validation Status
- Related Finding
- Related Recommendation

---

# 9. Normalized Evidence

Evidence shall be normalized before correlation.

Normalization activities include:

- Timestamp standardization.
- Identity normalization.
- Asset normalization.
- Event categorization.
- Severity assignment.
- ATT&CK mapping.
- Source validation.
- Evidence metadata generation.

Normalized evidence enables consistent analytics and reporting.

---

# 10. Correlation Rules

Evidence should be correlated using:

- Shared timestamps.
- Common identities.
- Asset relationships.
- Authentication sessions.
- Event identifiers.
- Process relationships.
- Network connections.
- ATT&CK mappings.
- Validation identifiers.

Correlation logic must be reproducible.

---

# 11. Evidence Validation

Before correlation is considered complete, evidence shall be verified for:

- Authenticity.
- Completeness.
- Integrity.
- Accuracy.
- Timestamp consistency.
- Source reliability.
- Supporting documentation.

Only validated evidence shall support assessment findings.

---

# 12. ATT&CK Correlation

Each correlated finding shall reference:

- ATT&CK Tactic
- ATT&CK Technique
- ATT&CK Sub-technique
- Detection Rule
- Telemetry Source
- Defensive Control
- Validation Status

This standardizes reporting across enterprise security assessments.

---

# 13. Investigation Workflow

Evidence correlation supports the following investigation sequence:

```
Alert

↓

Event Review

↓

Identity Analysis

↓

Asset Analysis

↓

Authentication Review

↓

Privilege Analysis

↓

Attack Path Review

↓

Risk Assessment

↓

Recommendation

↓

Closure
```

Each stage shall reference supporting evidence.

---

# 14. Risk Correlation

Correlated evidence contributes to enterprise risk assessment by evaluating:

- Identity Exposure
- Privilege Exposure
- Authentication Weaknesses
- Detection Coverage
- Control Effectiveness
- Business Impact
- Likelihood
- Residual Risk

Risk ratings shall be supported by correlated technical evidence.

---

# 15. Evidence Integrity

Evidence integrity shall be maintained through:

- Immutable timestamps.
- Standardized filenames.
- Controlled storage.
- Validation metadata.
- Chain of custody.
- Version control.
- Secure repositories.

Evidence modifications shall be documented.

---

# 16. Success Criteria

Evidence correlation is considered successful when:

- All evidence sources are identified.
- Related events are successfully linked.
- Detection logic is verified.
- ATT&CK mappings are complete.
- Findings are evidence-based.
- Risk ratings are justified.
- Recommendations are supported by technical evidence.
- Executive reports maintain traceability to source artifacts.

---

# 17. Deliverables

This methodology supports creation of:

- Evidence Correlation Report
- Detection Validation Report
- Investigation Timeline
- ATT&CK Mapping Matrix
- Validation Evidence Register
- Risk Assessment Summary
- Executive Findings Report
- Remediation Tracking Report

---

# 18. Continuous Improvement

Following each assessment, correlation processes should be reviewed to improve:

- Evidence quality.
- Detection accuracy.
- Telemetry completeness.
- Investigation workflows.
- Reporting consistency.
- Data normalization.
- Automation opportunities.

Lessons learned shall be incorporated into future assessment cycles.

---

# 19. Related Documents

Methodology:

- Purple-Team-Validation-Methodology.md
- Validation-Safety-Standard.md
- Detection-Validation-Workflow.md
- Telemetry-Collection-Runbook.md

Normalized Datasets:

- LHT-PurpleTeam-Normalized.csv
- LHT-DetectionValidation-Normalized.csv
- LHT-Telemetry-Normalized.csv
- LHT-DetectionCoverage-Normalized.csv
- LHT-AttackSimulation-Normalized.csv
- LHT-Validation-Metadata.csv

Templates:

- LHT-PurpleTeam-Assessment-Template.md
- LHT-Detection-Validation-Template.md
- LHT-Telemetry-Assessment-Template.md
- LHT-Coverage-Assessment-Template.md
- LHT-Attack-Simulation-Template.md

Evidence Registers:

- LHT-Validation-Evidence-Register.csv
- LHT-PurpleTeam-Checklist.csv
- LHT-Telemetry-Checklist.csv
- LHT-Detection-Checklist.csv
- LHT-Attack-Simulation-Checklist.csv
- LHT-Coverage-Checklist.csv

---

# 20. Document Approval

| Role | Name |
|------|------|
| Security Assessor | Bassey Solomon Henry |
| Reviewer | Lighthouse Technology Security Team |
| Status | Approved |
| Version | 1.0 |

---
