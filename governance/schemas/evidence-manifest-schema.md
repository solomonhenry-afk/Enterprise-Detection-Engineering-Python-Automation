# Evidence Manifest Schema

**Document ID:** LHT-Governance-Schema-001 
**Owner:** Bassey Solomon Henry 
**Organization:** Lighthouse Technology 
**Phase:** Phase B – Repository Foundation 
**Classification:** Internal Use 
**Status:** Approved

---

# Purpose

This schema defines the standard structure for recording all evidence collected throughout the Enterprise Active Directory Security Assessment. Every evidence artifact shall be uniquely identifiable, traceable, and linked to findings, detections, and remediation activities.

---

# Data Fields

| Field | Required | Description |
|--------|----------|-------------|
| Evidence_ID | Yes | Unique evidence identifier (LHT-Evidence-###). |
| Evidence_Name | Yes | Descriptive name of the evidence artifact. |
| Evidence_Type | Yes | Raw, Normalized, Simulated, Screenshot, Report, Log, Configuration Export, etc. |
| Collection_Status | Yes | Proposed, Collected, Validated, Remediated. |
| Evidence_Source | Yes | Tool, system, or log source. |
| Collection_Tool | Yes | Tool used to collect the evidence. |
| Collection_Date | Yes | Date and time of collection. |
| Collector | Yes | Individual responsible for collection. |
| Phase | Yes | Domain 5 assessment phase. |
| Related_Asset | Optional | Related asset identifier. |
| Related_Finding | Optional | Related finding identifier. |
| Integrity_Status | Yes | Verified, Pending Verification, Integrity Issue. |
| Storage_Location | Yes | Repository path. |
| Classification | Yes | Public, Internal, Confidential, Restricted. |
| Validation_Status | Yes | Pending, Validated, Rejected. |
| Notes | Optional | Additional observations. |

---

# Validation Rules

- Every record must contain a unique Evidence_ID.
- Evidence IDs shall never be reused.
- Every collected artifact shall reference its collection source.
- Evidence supporting findings must reference the associated Finding_ID.
- Storage locations must use repository-relative paths.

---

# Naming Convention

Evidence_ID shall follow:

LHT-Evidence-001

LHT-Evidence-002

LHT-Evidence-003

...

---

# Cross-References

- Findings Register
- Detection Register
- Remediation Register
- Validation Matrix Workbook
- Executive Reports

---

# Owner

Bassey Solomon Henry

Lighthouse Technology
