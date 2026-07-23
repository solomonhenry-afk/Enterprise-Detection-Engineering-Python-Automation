# Reporting Claim Standard

## Purpose

This standard prevents unsupported, overstated, or ambiguous claims in Domain 5 documentation and presentations.

## Approved Claim Labels

| Label      | Use                                                              |
| ---------- | ---------------------------------------------------------------- |
| Proposed   | Planned control, test, finding, or remediation not yet evidenced |
| Simulated  | Controlled scenario or synthetic data used for demonstration     |
| Collected  | Directly acquired evidence from the authorized lab               |
| Validated  | Confirmed through approved review or testing                     |
| Remediated | Corrective action implemented and evidenced                      |
| Retested   | Post-remediation validation completed                            |

## Claim Rules

* Every technical claim must reference an evidence identifier, finding identifier, or explicitly labeled simulated scenario.
* Do not state that a tool was run unless its output or collection record exists.
* Do not state that a vulnerability was exploited unless an approved validation record confirms it.
* Do not state that a detection worked unless telemetry and outcome evidence exist.
* Do not state that remediation reduced risk unless implementation and retest evidence exist.
* Distinguish absence of evidence from evidence of absence.
* Identify assumptions, scope limitations, missing telemetry, and data-quality constraints.

## Acceptable Examples

* “Collected evidence indicates that `LHT-Identity-014` has membership in a privileged group.”
* “A simulated validation scenario was designed to test detection coverage for DCSync-related activity.”
* “Detection coverage is proposed pending collection of Windows and Splunk telemetry.”
* “LHT-Remediation-005 is remediated; retest evidence is pending.”

## Unacceptable Examples

* “The domain is fully secure.”
* “DCSync was detected” without linked validation evidence.
* “All service accounts are compliant” without complete inventory and review evidence.
* “The remediation eliminated risk” without a documented retest and residual-risk assessment.

## Executive Reporting Rule

Executive summaries must present validated outcomes separately from planned work, simulated demonstrations, and unresolved risk.
