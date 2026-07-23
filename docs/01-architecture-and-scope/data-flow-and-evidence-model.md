# Data Flow and Evidence Model

## Purpose

This document defines how evidence moves from collection to reporting while preserving traceability, integrity, and claim accuracy.

## Evidence Flow

```text
Authorized source system or approved tool
                |
                v
Raw evidence preservation
evidence/raw/
                |
                v
Normalization and metadata capture
evidence/normalized/ and data/
                |
                v
Evidence manifest and quality review
evidence/manifests/ and governance/
                |
                v
Finding, detection, and remediation linkage
data/findings/ detections/ data/remediation/
                |
                v
Technical and executive reporting
reports/ and docs/
```

## Repository Data Locations

| Location                | Purpose                                                                                             |
| ----------------------- | --------------------------------------------------------------------------------------------------- |
| `evidence/raw/`         | Original exports, reports, event extracts, and tool output retained without analytical modification |
| `evidence/normalized/`  | Cleaned, structured, and analysis-ready evidence                                                    |
| `evidence/manifests/`   | Evidence inventory, hashes, source metadata, and lineage records                                    |
| `evidence/screenshots/` | Supporting visual proof; not the sole source of a finding                                           |
| `evidence/simulated/`   | Controlled test artifacts and synthetic validation data                                             |
| `data/inventories/`     | Structured asset, identity, privilege, and configuration inventories                                |
| `data/findings/`        | Finding register and supporting relationships                                                       |
| `data/detections/`      | Detection coverage and validation records                                                           |
| `data/remediation/`     | Remediation roadmap, ownership, and retest status                                                   |

## Minimum Evidence Metadata

Every evidence item must include:

* Evidence ID: `LHT-Evidence-###`
* Title and description
* Source system or tool
* Collection date and time
* Collector or process
* Scope or target
* Evidence state
* File path
* Integrity hash where practical
* Sensitivity classification
* Related asset, identity, finding, detection, or remediation identifiers
* Notes on limitations, transformations, or data quality

## Normalization Rules

* Preserve raw evidence before creating normalized copies.
* Record the transformation process for normalized evidence.
* Do not alter timestamps, object names, or source values without documenting the change.
* Redact credentials, secrets, hashes, tickets, and sensitive personal data before publication.
* Retain only the minimum data necessary for portfolio reporting.
* Clearly distinguish collected lab evidence from simulated examples.

## Evidence-to-Claim Rule

A report claim must link to at least one evidence record, or be labeled as proposed or simulated. Screenshots may support a claim but cannot replace the underlying source evidence when structured output is available.
