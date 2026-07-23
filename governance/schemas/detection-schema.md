# Detection Schema

**Document ID:** LHT-Governance-Schema-003

**Owner:** Bassey Solomon Henry

---

# Purpose

Defines the standard structure for documenting detection engineering activities, telemetry validation, and coverage measurements.

---

# Data Fields

| Field | Required | Description |
|--------|----------|-------------|
| Detection_ID | Yes | Unique detection identifier. |
| Detection_Name | Yes | Detection title. |
| Detection_Type | Yes | Splunk, Sigma, Sysmon, Windows Event, Custom Logic. |
| Splunk_Search | Optional | Splunk detection reference. |
| Sigma_Rule | Optional | Sigma rule reference. |
| Event_IDs | Optional | Related Windows Event IDs. |
| Data_Source | Yes | Primary telemetry source. |
| MITRE_ATT&CK | Optional | ATT&CK mapping. |
| Validation_Status | Yes | Pending, Validated, Failed. |
| False_Positives | Optional | Known false positives. |
| False_Negatives | Optional | Known false negatives. |
| Owner | Yes | Detection owner. |
| Status | Yes | Active, Draft, Retired. |
| Last_Validated | Yes | Latest validation date. |
| Notes | Optional | Additional comments. |

---

# Validation Rules

- Every detection shall map to a telemetry source.
- Detection validation is mandatory before reporting coverage.
- False positives and false negatives shall be documented where observed.
- Every detection shall reference a Validation_ID.

---

# Naming Convention

Detection_ID

LHT-Detection-001

LHT-Detection-002

...

---

# Cross-References

- Splunk Detection Package
- Sigma Repository
- Validation Matrix
- MITRE ATT&CK Matrix

---

Owner

Bassey Solomon Henry
