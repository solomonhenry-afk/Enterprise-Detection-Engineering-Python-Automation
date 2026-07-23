| Column                        | Purpose                                                             |
| ----------------------------- | ------------------------------------------------------------------- |
| Authentication_Record_ID      | Unique authentication observation                                   |
| Identity_ID                   | Links to `LHT-Identity-Normalized.csv`                              |
| System_ID                     | Links to `LHT-System-Normalized.csv`                                |
| Relationship_ID               | Links to `LHT-Relationship-Normalized.csv`                          |
| Collection_Metadata_ID        | Links to collection metadata                                        |
| Authentication_Type           | Interactive, Service, Network, Remote, Batch, etc.                  |
| Authentication_Protocol       | Kerberos, NTLM, LDAP, LDAPS, SMB, WinRM, etc.                       |
| Authentication_Method         | Password, Certificate, gMSA, Smart Card, Token (as applicable)      |
| Authentication_Source         | Originating host or service                                         |
| Authentication_Target         | Destination system or service                                       |
| Authentication_Status         | Success, Failure, Unknown                                           |
| Privilege_Level               | Standard, Elevated, Administrative, Tier Zero                       |
| Identity_Category             | User, Service Account, Computer, Administrator, etc.                |
| Tier_Classification           | Tier 0, Tier 1, Tier 2                                              |
| Credential_Type               | User Password, gMSA, Service Credential, Machine Account, etc.      |
| Authentication_Context        | Console, Remote, Scheduled Task, Service Logon, Network Logon, etc. |
| Authentication_Time_Reference | Timestamp or collection reference                                   |
| Evidence_ID                   | `LHT-Evidence-###`                                                  |
| Evidence_Source               | Event Log, Splunk, PowerShell, ADRecon, etc.                        |
| Evidence_Status               | Proposed, Collected, Validated, Simulated, Remediated               |
| Validation_Status             | Pending, Validated, Rejected                                        |
| Detection_Coverage            | Yes, Partial, No                                                    |
| Telemetry_Source              | Windows Security Log, Sysmon, Splunk, etc.                          |
| Related_Event_IDs             | Relevant Windows Event IDs (if applicable)                          |
| MITRE_ATTCK_Technique         | Associated ATT&CK technique(s), where relevant                      |
| Risk_Rating                   | Informational, Low, Medium, High, Critical                          |
| Assessment_Phase              | Domain 5 phase that produced the observation                        |
| Assessment_Date               | Date of assessment                                                  |
| Assessor                      | Security assessor                                                   |
| Comments                      | Additional notes                                                    |
