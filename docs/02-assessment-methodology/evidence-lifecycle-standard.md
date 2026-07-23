# Evidence Lifecycle Standard

## Purpose

This standard ensures that Domain 5 evidence is traceable, accurately labeled, and suitable for technical and executive reporting.

## Evidence States

| State      | Definition                                                                                      |
| ---------- | ----------------------------------------------------------------------------------------------- |
| Proposed   | Planned activity, hypothesis, control, or expected result not yet evidenced                     |
| Simulated  | Controlled test data or lab scenario created to exercise a process or detection                 |
| Collected  | Evidence directly acquired from the authorized Lighthouse Technology lab                        |
| Validated  | A finding, exposure, detection, or control outcome confirmed through approved review or testing |
| Remediated | Corrective action implemented and supported by change or configuration evidence                 |
| Retested   | Post-remediation validation completed and outcome recorded                                      |
| Superseded | Evidence replaced by newer or more reliable evidence while retained for lineage                 |

## Lifecycle Requirements

1. Assign an `LHT-Evidence-###` identifier when an evidence item enters the repository.
2. Preserve the original artifact in `evidence/raw/` when practical.
3. Create normalized copies only after raw preservation.
4. Record source, collector, collection time, scope, integrity information, and sensitivity.
5. Link evidence to affected assets, identities, findings, detections, and remediations.
6. Label limitations, assumptions, missing telemetry, and data-quality concerns.
7. Do not upgrade evidence state without a documented basis.
8. Retain prior evidence when remediation changes the environment.

## Evidence Quality Checks

* Source is identifiable.
* Scope is within authorization.
* Timestamp is available or documented as unavailable.
* Artifact is readable and complete enough for its intended claim.
* Sensitive data is handled according to classification rules.
* The evidence supports the linked finding or is clearly marked as contextual.
* Simulated evidence is never represented as collected lab evidence.

## Reporting Rule

Technical and executive reports must use the evidence state exactly as recorded in the evidence manifest.
