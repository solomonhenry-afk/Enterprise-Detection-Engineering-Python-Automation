# Scripts Directory

**Document ID:** LHT-Governance-Script-001 
**Owner:** Bassey Solomon Henry 
**Organization:** Lighthouse Technology 
**Project:** Enterprise Security Evolution – Domain 5 
**Phase:** Phase B – Repository Foundation 
**Classification:** Internal Use 
**Status:** Approved

---

# Purpose

The `scripts/` directory contains automation developed to support the Enterprise Active Directory Security Assessment performed within the authorized Lighthouse Technology laboratory environment.

Unlike general-purpose scripting repositories, every script within this project must serve a clearly defined operational purpose and directly support one or more assessment objectives.

Automation is intended to improve consistency, reduce manual effort, normalize collected data, generate reports, and support evidence-driven security assessments.

---

# Directory Structure

```text
scripts/
├── collection/
├── normalization/
├── reporting/
└── README.md
```

---

# Script Categories

## Collection

Scripts used to collect authorized security assessment data from the Active Directory environment.

Examples include:

- Active Directory inventory collection
- LDAP information collection
- SMB configuration collection
- Group Policy exports
- PowerShell data collection
- Windows Event Log collection
- Sysmon log exports

Expected Output

- Raw evidence
- Inventory datasets
- Configuration exports

---

## Normalization

Scripts that transform raw evidence into standardized formats suitable for reporting and analysis.

Examples include:

- CSV normalization
- JSON transformation
- Evidence identifier assignment
- Asset normalization
- Finding correlation
- Evidence manifest updates

Expected Output

- Normalized datasets
- Evidence-ready records
- Reporting inputs

---

## Reporting

Scripts used to generate assessment outputs.

Examples include:

- Finding summaries
- Detection coverage reports
- Executive dashboards
- MITRE ATT&CK mappings
- Remediation summaries
- Evidence manifests

Expected Output

- Technical reports
- Executive summaries
- Portfolio-ready documentation

---

# Script Development Standards

Every script shall:

- Support a defined assessment objective.
- Be documented before execution.
- Produce deterministic and reproducible results.
- Handle errors gracefully.
- Generate structured outputs where possible.
- Follow repository naming conventions.
- Be version controlled through Git.

---

# Naming Convention

Scripts should use descriptive lowercase filenames with underscores.

Examples:

```text
collect_ad_inventory.py

normalize_pingcastle_results.py

generate_detection_matrix.py

export_gpo_report.ps1

update_evidence_manifest.py
```

---

# Supported Languages

The following scripting languages are approved for this project:

- Python
- PowerShell
- Bash

Additional tooling may be used where operationally justified.

---

# Output Requirements

Automation should produce structured outputs whenever possible, including:

- CSV
- JSON
- XML
- Markdown
- Excel

Generated outputs shall be stored in the appropriate project directories and referenced within the Evidence Manifest.

---

# Logging Requirements

Where appropriate, scripts should record:

- Execution date and time
- Script version
- Operator
- Input source
- Output location
- Execution status
- Error messages

---

# Security Requirements

Scripts shall:

- Operate only within the authorized Lighthouse Technology lab environment.
- Avoid destructive actions unless explicitly required for controlled validation.
- Never expose credentials, secrets, or sensitive data.
- Respect authorization boundaries defined in the Rules of Engagement.
- Support evidence collection, detection validation, remediation engineering, and reporting.

---

# Quality Assurance

Before a script is committed to the repository, verify that:

- [ ] The script has a defined operational purpose.
- [ ] Input validation is implemented.
- [ ] Output is reproducible.
- [ ] Documentation is complete.
- [ ] Naming conventions are followed.
- [ ] Generated artifacts are stored in the correct directory.
- [ ] Sensitive information is excluded.
- [ ] The script has been tested in the authorized lab environment.

---

# Relationship to Other Domains

This scripting framework extends automation developed throughout the Enterprise Security Evolution portfolio.

- **Domain 1** – Telemetry collection, detection engineering, and Splunk integration.
- **Domain 2** – Purple Team validation and adversary simulation support.
- **Domain 3** – Infrastructure auditing, network assessment, and security engineering.
- **Domain 4** – Governance automation, evidence lineage, risk analytics, and executive reporting.
- **Domain 5** – Active Directory security auditing, identity assessment, privilege analysis, detection validation, remediation engineering, and executive reporting.

---

# Future Automation

Planned automation may include:

- Active Directory inventory collection
- BloodHound data normalization
- PingCastle result parsing
- Purple Knight result normalization
- ADRecon reporting
- Evidence manifest automation
- Detection coverage reporting
- MITRE ATT&CK matrix generation
- Executive reporting automation
- Remediation tracking

---

# Document Owner

**Bassey Solomon Henry** 
**Lead Infrastructure Security & Platform Operations Engineer** 
**Lighthouse Technology**

Enterprise Security Evolution Portfolio
