# Assessment Workflow

## Workflow

1. Confirm authorization, scope, and rules of engagement.
2. Collect baseline Active Directory and infrastructure evidence.
3. Normalize inventory data and establish evidence lineage.
4. Identify Tier Zero assets, privileged identities, and administrative exposure.
5. Analyze graph-based attack paths, ACLs, trusts, delegation, and credential exposure.
6. Prioritize findings using technical impact, reachability, privilege impact, detection coverage, and remediation feasibility.
7. Conduct approved, low-impact Purple Team validations.
8. Validate Windows, Sysmon, and Splunk telemetry.
9. Engineer or tune detections and map coverage to MITRE ATT&CK.
10. Design remediation actions with owners, priorities, expected exposure reduction, and retest methods.
11. Retest remediated controls where evidence is available.
12. Produce technical, governance, and executive deliverables.

## Evidence Lifecycle

```text
Proposed → Simulated or Collected → Validated → Remediated → Retested
```

## Finding Lifecycle

```text
LHT-Finding-### → Evidence review → Risk score → Owner assignment →
LHT-Remediation-### → Implementation evidence → Retest outcome → Residual risk
```

## Cross-Domain Inputs

* Domain 1: Windows logs, Sysmon, Splunk, detection logic, evidence generation.
* Domain 2: Purple Team validation workflow and ATT&CK mapping.
* Domain 3: Network segmentation, firewall context, SMB, LDAP, DNS, and reachable-path context.
* Domain 4: Evidence lineage, risk register, remediation scoring, governance automation, and executive reporting.
