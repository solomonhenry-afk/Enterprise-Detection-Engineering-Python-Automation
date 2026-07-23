# Asset and Tier Zero Model

## Purpose

This model defines how Lighthouse Technology will identify, classify, and prioritize Active Directory assets and identities during Domain 5.

## Asset Classes

| Asset class                 | Identifier pattern | Examples                                                                 | Assessment priority |
| --------------------------- | ------------------ | ------------------------------------------------------------------------ | ------------------- |
| Domain controller           | `LHT-AD-Asset-###` | Writable DC, read-only DC                                                | Critical            |
| Identity infrastructure     | `LHT-AD-Asset-###` | AD CS, identity-management server, privileged administration workstation | Critical            |
| Member server               | `LHT-AD-Asset-###` | File server, application server, management server                       | High                |
| Endpoint                    | `LHT-AD-Asset-###` | Administrator workstation, user workstation                              | Medium              |
| Network identity dependency | `LHT-AD-Asset-###` | DNS, DHCP, authentication relay dependency                               | High                |
| Privileged identity         | `LHT-Identity-###` | Domain Admin, Enterprise Admin, delegated administrator                  | Critical            |
| Service identity            | `LHT-Identity-###` | Service account, gMSA, scheduled-task identity                           | High                |

## Tier Zero Working Definition

Tier Zero is the set of systems, identities, permissions, and control paths that can directly or indirectly control Active Directory security.

Tier Zero candidates include:

* Domain Controllers
* Domain Admins, Enterprise Admins, Schema Admins, and Builtin Administrators
* Accounts with directory replication rights
* Accounts with rights to modify privileged groups, GPOs, trusts, ACLs, or delegation
* Privileged Access Workstations and administrative jump hosts
* Active Directory Certificate Services and equivalent identity infrastructure
* Identity synchronization, federation, backup, monitoring, and management systems with privileged directory access
* Service accounts with elevated privileges or administrative logon rights
* Systems hosting unconstrained delegation or privileged administrative sessions

## Classification Method

Each asset or identity must be classified using collected evidence where available:

1. **Control impact:** Can it alter authentication, authorization, directory data, or privileged access?
2. **Privilege level:** Does it hold direct, delegated, inherited, or indirect administrative capability?
3. **Reachability:** Is it reachable through approved network paths or existing administrative relationships?
4. **Credential exposure:** Does it store, process, or expose privileged credentials, tickets, hashes, or secrets?
5. **Detection coverage:** Are relevant Windows, Sysmon, and Splunk controls available?
6. **Business dependency:** Does disruption or compromise materially affect identity operations?

## Required Inventory Fields

| Field                | Description                                                                       |
| -------------------- | --------------------------------------------------------------------------------- |
| Asset or identity ID | Lighthouse Technology identifier                                                  |
| Name                 | Hostname, account name, group, service, or object name                            |
| Object type          | User, group, computer, GPO, OU, service account, trust, ACL, or delegation object |
| Tier classification  | Tier Zero, Tier One, Tier Two, or unclassified                                    |
| Owner                | Technical or business owner where known                                           |
| Evidence source      | Tool export, event log, configuration report, or manual review                    |
| Evidence state       | Proposed, simulated, collected, validated, remediated, or retested                |
| Related findings     | Linked `LHT-Finding-###` identifiers                                              |
| Review status        | Pending, reviewed, validated, or closed                                           |

## Validation Standard

Tier Zero classification must be supported by collected configuration, directory, graph, telemetry, or administrative exposure evidence. Proposed classifications must remain labeled as proposed until confirmed.
