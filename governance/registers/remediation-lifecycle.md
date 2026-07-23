# Remediation Lifecycle

**Document ID:** LHT-Governance-Register-003 
**Owner:** Bassey Solomon Henry 
**Organization:** Lighthouse Technology 
**Phase:** Phase B – Repository Foundation 
**Classification:** Internal Use 
**Status:** Approved

---

# Purpose

This document defines the lifecycle for remediation engineering activities performed during Domain 5. It ensures remediation actions are prioritized, implemented, validated, and measured for effectiveness.

---

# Lifecycle Overview

```text
Finding Confirmed
       │
       ▼
Root Cause Analysis
       │
       ▼
Remediation Planning
       │
       ▼
Implementation
       │
       ▼
Technical Validation
       │
       ▼
Risk Reduction Assessment
       │
       ▼
Retesting
       │
       ▼
Closure
```

---

# Lifecycle Stages

| Stage | Description | Deliverable |
|--------|-------------|-------------|
| Finding Confirmed | Security issue validated. | Validated Finding |
| Root Cause Analysis | Identify underlying cause. | Root Cause Analysis |
| Remediation Planning | Define corrective action. | Remediation Plan |
| Implementation | Apply approved remediation. | Updated Configuration |
| Technical Validation | Verify remediation effectiveness. | Validation Evidence |
| Risk Reduction Assessment | Measure reduction in exposure. | Risk Update |
| Retesting | Confirm issue is resolved. | Retest Results |
| Closure | Formally close remediation. | Closed Record |

---

# Remediation Status

- Planned
- Approved
- In Progress
- Implemented
- Validation Pending
- Verified
- Closed
- Exception Approved

---

# Required Relationships

Every remediation shall reference:

- Remediation_ID
- Finding_ID
- Evidence_ID
- Validation_ID
- Owner
- Risk Rating

---

# Governance Requirements

- Every remediation must be linked to an existing finding.
- Verification evidence is mandatory before closure.
- Exposure reduction must be documented.
- Retesting is required before marking a remediation as complete.
- Exceptions require documented business justification and approval.

---

**Document Owner**

Bassey Solomon Henry

Lighthouse Technology
