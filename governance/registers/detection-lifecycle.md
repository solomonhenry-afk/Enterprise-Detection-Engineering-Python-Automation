# Detection Lifecycle

**Document ID:** LHT-Governance-Register-002 
**Owner:** Bassey Solomon Henry 
**Organization:** Lighthouse Technology 
**Phase:** Phase B – Repository Foundation 
**Classification:** Internal Use 
**Status:** Approved

---

# Purpose

This document defines the lifecycle for detection engineering activities performed during the Enterprise Active Directory Security Assessment. It ensures detection logic is evidence-driven, validated, and continuously improved.

---

# Lifecycle Overview

```text
Threat Research
      │
      ▼
Detection Design
      │
      ▼
Detection Development
      │
      ▼
Telemetry Validation
      │
      ▼
Purple Team Validation
      │
      ▼
Coverage Assessment
      │
      ▼
Detection Tuning
      │
      ▼
Operational Deployment
      │
      ▼
Continuous Improvement
```

---

# Lifecycle Stages

| Stage | Description | Deliverable |
|--------|-------------|-------------|
| Threat Research | Review attack techniques and telemetry requirements. | Research Notes |
| Detection Design | Define detection logic and expected telemetry. | Detection Design |
| Detection Development | Implement Splunk searches, Sigma rules, or analytics. | Detection Logic |
| Telemetry Validation | Confirm required logs are available. | Validation Evidence |
| Purple Team Validation | Validate detections through authorized lab testing. | Validation Matrix |
| Coverage Assessment | Evaluate detection effectiveness. | Coverage Report |
| Detection Tuning | Reduce false positives and false negatives. | Updated Detection |
| Operational Deployment | Detection accepted for monitoring. | Production Version |
| Continuous Improvement | Periodic review and optimization. | Revision History |

---

# Detection Status

- Draft
- Under Development
- Validation Pending
- Validated
- Tuned
- Operational
- Retired

---

# Required Relationships

Every detection shall reference:

- Detection_ID
- Validation_ID
- ATT&CK Technique
- Evidence_ID
- Data Source
- Detection Owner

---

# Governance Requirements

- Every detection must map to telemetry.
- Validation is mandatory before operational use.
- Detection gaps shall be documented.
- False positives and false negatives must be reviewed.
- Detection revisions shall be tracked.

---

**Document Owner**

Bassey Solomon Henry

Lighthouse Technology
