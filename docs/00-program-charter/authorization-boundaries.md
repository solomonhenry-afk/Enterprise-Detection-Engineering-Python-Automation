# Authorization Boundaries

## Authorized Environment

All testing is restricted to the Lighthouse Technology authorized lab environment and its explicitly approved Active Directory systems, test accounts, hosts, and telemetry platforms.

## In Scope

* Active Directory forest and domain services
* Domain controllers and approved member systems
* Authorized test users, service accounts, and privileged lab accounts
* DNS, LDAP, SMB, Kerberos, WinRM, Group Policy, trusts, and delegation settings
* Windows Event Logs, Sysmon, Splunk, and approved assessment tooling

## Out of Scope

* Production systems
* Third-party systems or identities
* Internet targets not owned by Lighthouse Technology
* Unapproved credential attacks
* Persistent access mechanisms
* Destructive directory changes
* Broad password spraying
* Unapproved replication, ticket-forging, or directory-object modification activity

## High-Impact Validation Controls

The following techniques require a disposable lab account or host, a defined test window, evidence collection, an approved rollback plan, and post-test verification:

* Pass-the-Hash
* Pass-the-Ticket
* Golden Ticket
* Silver Ticket
* DCSync
* DCShadow
* LDAP abuse
* WinRM abuse
* SMB abuse
* Password spraying validation

## Evidence Handling

Evidence must be stored only in the Domain 5 repository evidence structure. Sensitive values, credentials, hashes, secrets, and personally identifying data must not be committed to source control.
