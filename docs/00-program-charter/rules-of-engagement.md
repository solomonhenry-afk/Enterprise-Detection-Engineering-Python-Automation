# Rules of Engagement

## Purpose

These rules govern all Active Directory assessment and Purple Team validation activities performed within the Lighthouse Technology authorized lab.

## Operating Principles

* Test only authorized systems and accounts.
* Prefer read-only collection and configuration review before validation activity.
* Use the minimum privilege, minimum volume, and minimum duration necessary.
* Capture evidence before, during, and after each approved validation.
* Stop testing if unexpected instability, service disruption, account lockout, or data-integrity risk appears.
* Record all changes and restore the lab to its approved baseline where applicable.

## Prohibited Activities

* Testing outside the approved lab boundary
* Use of real user credentials without documented authorization
* Uncontrolled password spraying or credential guessing
* Destructive modification of directory objects, Group Policy, DNS, or replication configuration
* Persistence, exfiltration, or unauthorized lateral movement
* Committing secrets, hashes, tickets, or sensitive raw evidence to Git

## Validation Requirements

Each high-impact scenario must document:

1. Objective
2. Authorized scope
3. Test account or host
4. Preconditions
5. Expected telemetry
6. Evidence artifact location
7. Detection outcome
8. Rollback action
9. Remediation or tuning action
10. Retest result

## Stop Conditions

Immediately stop the activity and document the condition if a domain controller, identity service, authentication workflow, endpoint, or logging pipeline becomes unstable or behaves outside the expected lab scenario.
