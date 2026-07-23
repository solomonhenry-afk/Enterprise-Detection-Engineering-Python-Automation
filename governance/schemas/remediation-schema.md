# Remediation Schema

**Document ID:** LHT-Governance-Schema-004

**Owner:** Bassey Solomon Henry

---

# Purpose

Defines the standard structure for documenting remediation engineering activities, implementation status, verification, and exposure reduction.

---

# Data Fields

| Field | Required | Description |
|--------|----------|-------------|
| Remediation_ID | Yes | Unique remediation identifier. |
| Related_Finding | Yes | Linked finding. |
| Remediation_Action | Yes | Recommended corrective action. |
| Risk_Reduction | Yes | Expected reduction in exposure or risk. |
| Owner | Yes | Responsible owner. |
| Priority | Yes | Critical, High, Medium, Low. |
| Implementation_Status | Yes | Planned, In Progress, Implemented, Verified. |
| Validation_Method | Yes | Retest, Configuration Review, Log Validation, etc. |
| Retest_Date | Optional | Scheduled retest date. |
| Completion_Date | Optional | Completion date. |
| Evidence_ID | Yes | Supporting implementation evidence. |
| Notes | Optional | Additional implementation notes. |

---

# Validation Rules

- Every remediation shall reference an existing Finding_ID.
- Verification evidence is mandatory before closure.
- Every implemented remediation requires a validation activity.
- Exposure reduction shall be documented before final closure.

---

# Naming Convention

Remediation_ID

LHT-Remediation-001

LHT-Remediation-002

...

---

# Cross-References

- Findings Register
- Validation Matrix
- Executive Remediation Roadmap
- Evidence Manifest

---

Owner

Bassey Solomon Henry

Lighthouse Technology
