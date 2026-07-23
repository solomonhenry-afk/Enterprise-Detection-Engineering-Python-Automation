# Lighthouse Technology

# Enterprise Security Evolution

## Domain 5 — Enterprise Active Directory Penetration Testing & Security Auditing

# Identity Collection Runbook

| Document Information | |
|----------------------|------------------------------------------------|
| Document ID | LHT-RUN-001 |
| Version | 1.0 |
| Status | Approved |
| Classification | Internal |
| Project | Enterprise Security Evolution |
| Domain | Domain 5 |
| Owner | Lighthouse Technology |
| Last Updated | 2026-07-13 |
| Related Documents | LHT-METH-001, LHT-METH-002, LHT-METH-003, LHT-PLAN-001, LHT-PLAN-002, LHT-STD-001 |

---

# 1. Purpose

This runbook defines the operational procedure for collecting identity-related information from the authorized Lighthouse Technology Enterprise Active Directory laboratory.

The objective is to ensure that identity enumeration is:

- Repeatable
- Evidence-driven
- Traceable
- Non-destructive
- Consistent
- Suitable for technical analysis and governance reporting

This runbook governs operational execution only.

It does not contain inventory records, assessment findings, or remediation actions.

---

# 2. Scope

This runbook applies to the collection of:

- User accounts
- Security groups
- Distribution groups
- Computer accounts
- Service accounts
- Group Managed Service Accounts (gMSA)
- Organizational Units
- Group Policy Objects
- Trust relationships
- Delegation configurations
- Tier Zero candidates
- Identity relationships
- Supporting metadata

Collection activities are limited to the authorized Lighthouse Technology Enterprise Lab.

---

# 3. Roles and Responsibilities

| Role | Responsibility |
|------|----------------|
| Security Assessor | Execute identity collection activities |
| Infrastructure Administrator | Provide authorized access where required |
| Detection Engineer | Correlate inventory with telemetry |
| Governance Analyst | Validate evidence quality and traceability |

---

# 4. Prerequisites

Before beginning collection, confirm that:

- Assessment authorization has been approved.
- Rules of Engagement remain valid.
- Repository structure has been created.
- Methodology documents are approved.
- Evidence registration templates are available.
- Normalized dataset templates exist.
- Required collection tools are available within the authorized lab.

No collection activities shall begin until these prerequisites have been satisfied.

---

# 5. Evidence Lifecycle

All collected information shall follow the Lighthouse Technology evidence lifecycle.

| Status | Description |
|----------|-------------|
| Proposed | Planned but not collected |
| Collected | Acquired from an authorized source |
| Validated | Verified for accuracy and completeness |
| Simulated | Artificially generated for demonstration purposes |
| Remediated | Collected following corrective actions |

Evidence status shall be recorded within the Evidence Manifest.

---

# 6. Planned Collection Workflow

The operational workflow shall follow the sequence below.

1. Confirm authorization.
2. Identify collection objective.
3. Select approved evidence source.
4. Perform authorized collection.
5. Register evidence.
6. Preserve original artifacts.
7. Normalize collected data.
8. Validate inventory records.
9. Update evidence lifecycle status.
10. Store evidence in the repository.
11. Perform quality assurance review.
12. Prepare data for analysis.

---

# 7. Planned Collection Sources

The following evidence sources may be used during the assessment.

| Source | Purpose | Expected Output | Initial Status |
|---------|---------|----------------|----------------|
| PowerShell Active Directory Module | Directory inventory | CSV / JSON / XML | Proposed |
| ADRecon | Active Directory configuration review | HTML / CSV | Proposed |
| BloodHound Community Edition | Relationship analysis | JSON / ZIP | Proposed |
| Group Policy Reports | GPO inventory | XML / HTML | Proposed |
| Windows Event Logs | Identity activity context | EVTX | Proposed |
| Sysmon | Endpoint telemetry | EVTX | Proposed |
| Splunk | Detection correlation | Saved Searches / Reports | Proposed |

Evidence shall remain in the **Proposed** state until collected from the authorized laboratory.

---

# 8. Planned Collection Order

Identity collection should follow the order below.

| Sequence | Object Category | Purpose |
|----------|-----------------|---------|
| 1 | Forest and Domains | Establish assessment scope |
| 2 | Organizational Units | Administrative structure |
| 3 | Users | Identity inventory |
| 4 | Groups | Administrative relationships |
| 5 | Computers | Asset inventory |
| 6 | Service Accounts | Credential exposure assessment |
| 7 | gMSA | Managed identity assessment |
| 8 | Group Policy Objects | Identity governance review |
| 9 | Trust Relationships | Cross-domain analysis |
| 10 | Delegation Configurations | Privilege exposure assessment |
| 11 | Tier Zero Candidates | Critical asset identification |

---

# 9. Evidence Registration Requirements

Each collected artifact shall receive a unique Lighthouse Evidence ID.

Example:

- LHT-Evidence-001
- LHT-Evidence-002
- LHT-Evidence-003

Evidence records shall include:

- Evidence ID
- Evidence Name
- Collection Method
- Source Tool
- Collection Date
- Collector
- Validation Status
- Lifecycle Status
- Related Asset(s)
- Related Identity(ies)

---

# 10. Data Quality Checks

Following collection, verify that:

- Files are readable.
- Required metadata is present.
- Duplicate records are identified.
- Object naming is consistent.
- Source attribution is complete.
- Timestamps are recorded.
- Evidence identifiers are assigned.
- No unauthorized modifications have occurred.

Any quality issues shall be documented before analysis.

---

# 11. Evidence Storage

Evidence shall be stored according to the repository structure.

```text
evidence/
├── proposed/
├── collected/
├── normalized/
├── validated/
├── remediated/
└── manifests/
```

Original evidence shall always be retained separately from normalized datasets.

---

# 12. Validation Activities

Before inventory data is used in technical analysis:

- Confirm evidence integrity.
- Review metadata completeness.
- Validate object classifications.
- Verify evidence references.
- Review normalization results.
- Confirm lifecycle status.
- Document validation outcome.

Only validated evidence shall support technical findings.

---

# 13. Expected Outputs

Successful execution of this runbook supports:

- Identity Inventory
- Computer Inventory
- Group Inventory
- Service Account Inventory
- Delegation Inventory
- Tier Zero Inventory
- Normalized Identity Dataset
- Relationship Dataset
- Evidence Manifest
- Data Quality Report

---

# 14. Cross-Domain Integration

## Domain 1 — SOC Operations, Telemetry & Detection Engineering

Collected identity data provides authoritative context for Windows Event Logs, Sysmon telemetry, and Splunk detections.

## Domain 2 — Enterprise Adversary Validation & Purple Team Operations

Validated inventories define the identities and systems used during authorized Purple Team validation activities.

## Domain 3 — Network Security & Infrastructure Engineering

Identity records are correlated with infrastructure components, including Domain Controllers, DNS, LDAP, SMB, and network segmentation.

## Domain 4 — Governance, Risk & Compliance Intelligence

Collected evidence becomes governed data supporting evidence lineage, risk scoring, remediation tracking, and executive reporting.

---

# 15. Success Criteria

This runbook shall be considered successfully executed when:

- All planned identity categories have been collected from authorized sources.
- Evidence has been registered and preserved.
- Data has been normalized and validated.
- Inventory records are traceable to supporting evidence.
- Data quality checks have been completed.
- Outputs are suitable for privilege exposure analysis, attack-path assessment, detection engineering, and governance reporting.

---

# Document Approval

| Role | Name | Status |
|------|------|--------|
| Project Owner | Lighthouse Technology | Approved |
| Security Assessor | __________________ | B. Solomon Henry |
| Reviewer | __________________ | Lighthouse Technology Security Team |

---

