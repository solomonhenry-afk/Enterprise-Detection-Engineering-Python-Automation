# Assessment Plan

## Objective

Perform a comprehensive, evidence-backed security assessment of the Lighthouse Technology Active Directory lab environment.

## Assessment Sequence

| Stage | Activity                                                                               | Primary output                                        |
| ----- | -------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| 1     | Confirm scope, authorization, and safety controls                                      | Approved assessment boundary                          |
| 2     | Collect baseline AD, host, policy, and telemetry evidence                              | Raw and normalized evidence inventory                 |
| 3     | Identify Tier Zero assets and privileged identities                                    | Tier Zero model and administrative exposure inventory |
| 4     | Review forest, domain, GPO, OU, DNS, DC, SMB, LDAP, and Kerberos controls              | Security audit findings                               |
| 5     | Analyze users, groups, computers, service accounts, trusts, ACLs, GPOs, and delegation | Identity and privilege exposure report                |
| 6     | Analyze attack paths and high-risk relationships                                       | Attack-path analysis and prioritized findings         |
| 7     | Assess credential and authentication security                                          | Credential security findings                          |
| 8     | Conduct approved Purple Team validations                                               | Validation matrix and telemetry evidence              |
| 9     | Measure and improve detection coverage                                                 | Splunk, Sigma, ATT&CK, and coverage matrix            |
| 10    | Engineer remediation and perform retests                                               | Remediation roadmap and residual-risk status          |
| 11    | Produce technical and executive reporting                                              | Final Domain 5 deliverables                           |

## Collection Principles

* Start with read-only and low-impact evidence collection.
* Use approved tools only within the authorized lab.
* Preserve raw output before normalization.
* Capture tool version, command context, date, and source host.
* Do not claim findings until evidence has been reviewed and classified.

## Decision Gates

| Gate               | Decision                                                                              |
| ------------------ | ------------------------------------------------------------------------------------- |
| Authorization gate | Scope, systems, accounts, and test windows are confirmed                              |
| Evidence gate      | Baseline data is complete enough for analysis                                         |
| Validation gate    | High-impact simulation has approval, rollback, and telemetry coverage                 |
| Detection gate     | Detection outcome is documented as validated, gap, tuning required, or not observable |
| Remediation gate   | Finding has owner, priority, validation method, and expected exposure reduction       |
| Reporting gate     | Claims are evidence-linked and evidence states are accurately labeled                 |

## Final Reporting Standard

The final report must separate collected findings, simulated validation results, proposed improvements, remediated controls, and retested outcomes.
