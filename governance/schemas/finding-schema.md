# Finding Schema

**Document ID:** LHT-Governance-Schema-002

**Owner:** Bassey Solomon Henry

---

# Purpose

Defines the standard structure for recording all Active Directory security findings generated during Domain 5.

---

# Data Fields

| Field | Required | Description |
|--------|----------|-------------|
| Finding_ID | Yes | Unique finding identifier. |
| Finding_Title | Yes | Short descriptive title. |
| Finding_Category | Yes | Identity, GPO, Kerberos, LDAP, SMB, Tier Zero, etc. |
| Risk_Rating | Yes | Critical, High, Medium, Low. |
| CVSS_Score | Optional | CVSS score where applicable. |
| MITRE_ATT&CK | Optional | ATT&CK Technique ID(s). |
| Related_Asset | Yes | Asset identifier. |
| Evidence_ID | Yes | Supporting evidence. |
| Status | Yes | Open, In Progress, Closed. |
| Owner | Yes | Responsible owner. |
| Priority | Yes | P1–P4. |
| Remediation_ID | Optional | Linked remediation. |
| Validation_Status | Yes | Pending, Validated, Rejected. |
| Discovery_Date | Yes | Date discovered. |
| Closure_Date | Optional | Date closed. |
| Notes | Optional | Additional observations. |

---

# Validation Rules

- Every finding requires supporting evidence.
- Every finding must have a severity.
- Every finding must map to at least one asset.
- Unsupported findings shall not appear in executive reports.

---

# Naming Convention

Finding_ID:

LHT-Finding-001

LHT-Finding-002

...

---

# Related Documents

- Evidence Manifest
- Remediation Register
- Executive Risk Summary
- Technical Findings Report

---

Owner:

Bassey Solomon Henry
