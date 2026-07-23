# Risk Scoring Methodology

## Purpose

This methodology prioritizes Active Directory findings using technical impact, identity reachability, detection coverage, governance context, and remediation feasibility.

## Scoring Dimensions

Each finding is scored from 1 to 5 in the following categories:

| Dimension                          | Description                                                                                      |
| ---------------------------------- | ------------------------------------------------------------------------------------------------ |
| Identity impact                    | Potential effect on authentication, authorization, privileged access, or directory control       |
| Privilege impact                   | Level of privilege obtainable or exposed                                                         |
| Attack-path reachability           | Practical accessibility through observed relationships, network context, or administrative paths |
| Credential exposure                | Likelihood that credentials, hashes, tickets, or secrets can be exposed or misused               |
| Detection gap                      | Degree to which the activity lacks effective telemetry or detection                              |
| Business or operational dependency | Effect on critical services, administration, or identity operations                              |
| Remediation complexity             | Effort, dependency, and change risk required to reduce exposure                                  |

## Risk Calculation

```text
Base Risk Score =
Identity Impact + Privilege Impact + Attack-Path Reachability +
Credential Exposure + Detection Gap + Business Dependency

Remediation Complexity is recorded separately to support prioritization,
not to reduce the underlying technical risk.
```

## Severity Bands

| Score | Severity      | Required response                                                                      |
| ----- | ------------- | -------------------------------------------------------------------------------------- |
| 25–30 | Critical      | Immediate ownership, containment or compensating control, remediation plan, and retest |
| 19–24 | High          | Prioritized remediation with defined owner and detection validation                    |
| 13–18 | Medium        | Planned remediation and monitoring improvement                                         |
| 7–12  | Low           | Track, validate assumptions, and address through routine hardening                     |
| 0–6   | Informational | Document for visibility or baseline improvement                                        |

## Required Finding Fields

Every `LHT-Finding-###` record must include:

* Title and description
* Evidence references
* Affected assets and identities
* Tier classification
* Attack-path or configuration context
* MITRE ATT&CK mapping where applicable
* Risk score and severity
* Detection status
* Owner
* Recommended remediation
* Expected exposure reduction
* Validation method
* Residual risk
* Evidence state

## Prioritization Rule

Critical and High findings affecting Tier Zero, directory replication, privileged groups, privileged service accounts, delegation, or credential material receive executive visibility even when remediation is complex.
