# Technique Validation Framework

## Purpose

This framework governs safe, controlled validation of identity-based attack techniques in the Lighthouse Technology lab.

## Required Validation Record

Every technique validation must include:

| Field                  | Requirement                                              |
| ---------------------- | -------------------------------------------------------- |
| Validation ID          | Unique identifier                                        |
| Technique              | Technique name and MITRE ATT&CK mapping                  |
| Objective              | Defensive learning or exposure-confirmation objective    |
| Authorization boundary | Approved lab systems, accounts, and time window          |
| Preconditions          | Required configuration or test-state conditions          |
| Test account or host   | Disposable or approved lab identity and endpoint         |
| Evidence plan          | Expected raw, normalized, and screenshot artifacts       |
| Expected telemetry     | Windows Event IDs, Sysmon, network, and Splunk sources   |
| Detection logic        | Existing rule, query direction, or planned detection     |
| Rollback plan          | Steps required to restore the approved lab state         |
| Outcome                | Validated, not validated, detection gap, or inconclusive |
| Remediation            | Corrective action or tuning recommendation               |
| Retest result          | Post-remediation validation status                       |

## Safe Validation Principles

* Use a minimum-privilege test account where possible.
* Prefer configuration validation and telemetry generation over credential-impacting activity.
* Use low-volume, time-bounded tests.
* Do not create persistence or uncontrolled lateral movement.
* Do not use real credentials, secrets, hashes, or tickets in documentation.
* Stop immediately if the test causes unexpected authentication failures, account lockouts, service instability, or logging disruption.

## Technique Categories

| Category                          | Examples                                                              | Validation focus                                              |
| --------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------- |
| Privilege path                    | ACL abuse exposure, delegated rights, privileged group relationships  | Reachability, permissions, detection, remediation             |
| Credential exposure               | Kerberoasting exposure, AS-REP exposure, NTLM exposure                | Configuration, account hygiene, telemetry, hardening          |
| Delegation                        | Constrained, unconstrained, and resource-based constrained delegation | Configuration exposure, privileged reachability, monitoring   |
| Replication and directory control | DCSync and DCShadow lab-only scenarios                                | Rights review, high-fidelity detection, rollback discipline   |
| Ticket and hash abuse             | Pass-the-Hash, Pass-the-Ticket, Golden Ticket, Silver Ticket          | Telemetry, detection coverage, account and Kerberos hardening |
| Remote services                   | LDAP, SMB, and WinRM abuse scenarios                                  | Access controls, logging, segmentation, and alerting          |

## Outcome Labels

* **Validated:** The approved lab condition and expected evidence were confirmed.
* **Not validated:** The condition was absent or the scenario did not meet preconditions.
* **Detection gap:** The activity occurred but required telemetry or detection was absent.
* **Tuning required:** Detection occurred but required refinement.
* **Inconclusive:** Evidence was insufficient to make a reliable determination.
