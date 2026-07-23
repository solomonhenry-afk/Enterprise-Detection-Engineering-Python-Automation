# Lighthouse Technology Detection Engineering Tuning Template

# Detection Tuning Assessment Report

---

# Document Information

| Field | Value |
|---|---|
| Tuning Assessment ID | LHT-DET-TUNE-001 |
| Detection ID | DET-001 |
| Detection Name | Suspicious PowerShell Execution Detection |
| Detection Category | Endpoint Detection |
| Assessment Type | Detection Optimization & False Positive Reduction |
| Version | 1.0 |
| Assessment Date | 2026-07-22 |
| Analyst | Lighthouse Technology Detection Engineering Team |
| Reviewer | Enterprise Security Governance Team |
| Status | Approved |
| Classification | Internal Security Engineering Documentation |

---

# 1. Tuning Objective

## 1.1 Purpose

The purpose of this tuning assessment is to improve detection accuracy while maintaining effective coverage against adversary behavior.

The tuning process ensures that:

- Detection logic remains effective.
- False positives are minimized.
- SOC analyst workload is controlled.
- Threat visibility is preserved.
- Detection quality improves over time.

---

# 2. Detection Overview

| Attribute | Value |
|---|---|
| Detection ID | DET-001 |
| Rule ID | RULE-001 |
| Sigma ID | SIG-001 |
| Detection Name | Suspicious PowerShell Execution Detection |
| MITRE Technique | T1059.001 - PowerShell |
| Severity | High |
| SIEM Platform | Splunk |
| Lifecycle Status | Production |

---

# 3. Tuning Trigger

## Reason for Review

| Trigger | Selected |
|---|---|
| High Alert Volume | Yes |
| False Positive Increase | Yes |
| Detection Logic Improvement | Yes |
| Threat Intelligence Update | Yes |
| New Attack Technique | No |

---

# 4. Current Detection Performance

| Metric | Current Value |
|---|---|
| Total Alerts Generated | 48 |
| True Positive Alerts | 46 |
| False Positive Alerts | 2 |
| False Positive Rate | 4.17% |
| Detection Accuracy | 95.83% |
| Average Investigation Time | 18 Minutes |

---

# 5. False Positive Analysis

## 5.1 Identified False Positive Sources

| Source | Description | Risk |
|---|---|---|
| IT Administration | Authorized PowerShell automation | Low |
| Software Deployment | Deployment scripts executing PowerShell | Low |
| Security Tools | Endpoint management actions | Low |

---

## 5.2 False Positive Investigation

| Question | Result |
|---|---|
| Is activity authorized? | Yes |
| Is account trusted? | Yes |
| Is execution pattern expected? | Yes |
| Should alert remain visible? | Yes, with reduced priority |

---

# 6. Tuning Actions

## Implemented Changes

| Change ID | Action | Owner | Status |
|---|---|---|---|
| TUNE-001 | Exclude approved administrative accounts | Detection Engineering Team | Completed |
| TUNE-002 | Baseline enterprise automation scripts | Detection Engineering Team | Completed |
| TUNE-003 | Increase suspicious argument weighting | Detection Engineering Team | Completed |

---

# 7. Detection Logic Improvements

## Before Tuning

```text
Alert when:

PowerShell execution detected
+
Suspicious keyword match
