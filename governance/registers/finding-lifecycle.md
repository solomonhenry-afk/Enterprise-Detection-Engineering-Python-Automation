# Finding Lifecycle

**Document ID:** LHT-Governance-Register-001 
**Owner:** Bassey Solomon Henry 
**Organization:** Lighthouse Technology 
**Phase:** Phase B – Repository Foundation 
**Classification:** Internal Use 
**Status:** Approved

---

# Purpose

This document defines the standardized lifecycle for Active Directory security findings generated throughout Domain 5. The lifecycle ensures every finding is evidence-backed, validated, remediated, and formally closed following enterprise governance practices.

---

# Lifecycle Overview

```text
Discovery
    │
    ▼
Evidence Collection
    │
    ▼
Technical Validation
    │
    ▼
Risk Assessment
    │
    ▼
Detection Validation
    │
    ▼
Remediation Planning
    │
    ▼
Remediation Implementation
    │
    ▼
Retesting
    │
    ▼
Finding Closure
```

---

# Lifecycle Stages

| Stage | Description | Required Output |
|--------|-------------|-----------------|
| Discovery | Security issue identified through auditing, enumeration, or validation. | Finding Record |
| Evidence Collection | Supporting evidence collected and normalized. | Evidence Manifest Entry |
| Technical Validation | Finding verified within the authorized lab environment. | Validation Record |
| Risk Assessment | Business and technical risk evaluated. | Risk Rating |
| Detection Validation | Existing detections reviewed and validated. | Detection Coverage |
| Remediation Planning | Corrective action defined and prioritized. | Remediation Plan |
| Remediation Implementation | Security improvement applied. | Updated Configuration |
| Retesting | Validation performed after remediation. | Retest Results |
| Closure | Finding confirmed as resolved or accepted. | Closed Finding |

---

# Finding Status Values

- Proposed
- Identified
- Under Review
- Validated
- Remediation Planned
- Remediation In Progress
- Retest Pending
- Closed
- Risk Accepted

---

# Required Relationships

Every finding shall reference:

- One Finding_ID
- One or more Evidence_ID values
- One Risk Rating
- One Remediation_ID (where applicable)
- One Validation_ID
- Zero or more Detection_ID values

---

# Governance Requirements

- No finding shall appear in reports without supporting evidence.
- Every Critical and High finding requires remediation planning.
- Closure requires successful validation or documented risk acceptance.
- Findings must remain traceable throughout the assessment lifecycle.

---

**Document Owner**

Bassey Solomon Henry

Lighthouse Technology
