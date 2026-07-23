# Data Quality Standard

**Document ID:** LHT-Governance-Quality-001 
**Owner:** Bassey Solomon Henry 
**Organization:** Lighthouse Technology 
**Phase:** Phase B – Repository Foundation 
**Classification:** Internal Use 
**Status:** Approved

---

# Purpose

This document establishes the data quality standards for all information collected, processed, normalized, analyzed, and reported during the Enterprise Active Directory Security Assessment.

The objective is to ensure that every assessment output is accurate, complete, traceable, reproducible, and suitable for technical and executive decision-making.

---

# Data Quality Principles

The assessment follows six core data quality principles:

- Accuracy
- Completeness
- Consistency
- Timeliness
- Integrity
- Traceability

---

# Quality Dimensions

| Dimension | Requirement | Validation Method |
|------------|-------------|-------------------|
| Accuracy | Information correctly represents collected evidence. | Manual review and evidence verification |
| Completeness | Required fields are populated. | Schema validation |
| Consistency | Naming standards are followed. | Governance review |
| Timeliness | Evidence reflects the assessment period. | Collection timestamp verification |
| Integrity | Evidence has not been altered after collection. | Hash verification where applicable |
| Traceability | Every claim maps to supporting evidence. | Evidence manifest review |

---

# Mandatory Requirements

Every dataset shall:

- Follow Lighthouse Technology naming conventions.
- Include unique identifiers.
- Reference the originating evidence.
- Record the collection date.
- Identify the collection tool.
- Record the collector.
- Maintain repository-relative storage paths.

---

# Data Validation Process

1. Collect evidence.
2. Verify completeness.
3. Normalize data.
4. Validate schema compliance.
5. Assign identifiers.
6. Update the Evidence Manifest.
7. Perform quality review.
8. Approve for reporting.

---

# Quality Metrics

The following metrics should be monitored throughout the assessment:

| Metric | Target |
|---------|--------|
| Missing Required Fields | 0% |
| Duplicate Records | 0% |
| Invalid Identifiers | 0% |
| Broken Evidence References | 0% |
| Unsupported Findings | 0% |
| Unvalidated Detections | 0% |

---

# Roles and Responsibilities

| Role | Responsibility |
|------|----------------|
| Collector | Gather evidence in accordance with approved methodology. |
| Validator | Confirm technical accuracy. |
| Reviewer | Verify governance compliance. |
| Report Author | Ensure evidence supports every reported claim. |

---

# Document Owner

Bassey Solomon Henry

Lighthouse Technology
