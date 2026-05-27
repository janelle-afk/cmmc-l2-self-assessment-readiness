# Worked Example: CloudSync SaaS Vendor

This directory contains a complete worked example of a CMMC Level 2 self-assessment for a fictional small SaaS company to demonstrate the skill workflow.

## Company Profile: CloudSync Inc.

**Industry:** Cloud-based collaboration software
**Size:** 30 employees
**CUI Handling:** Customer contracts include DoD agencies; platform hosts technical documents marked as CUI
**Infrastructure:** 100% AWS cloud, remote workforce across 3 states

## Assessment Context

**Customer Request:** Prime contractor (Lockheed Martin) requested SPRS score and attestation letter for subcontractor qualification

**Due Date:** 30 days from request

**Deliverables Requested:**
- SPRS score
- Attestation letter signed by CISO
- High-level summary of security posture

## Example Files Included

- `scoping-worksheet-completed.md` - Completed scoping for CloudSync
- `control-assessment-sample.csv` - Sample of first 20 controls assessed (demonstration only; real assessment would include all 110)
- `evidence-index-sample.md` - Sample evidence tracking
- `assessment-summary.md` - Brief narrative of findings and score

This is a teaching example demonstrating the workflow. A real assessment would include all 110 controls, comprehensive evidence, and full POA&M.

## Key Characteristics of This Example

**Strengths:**
- Strong access control (Okta SSO with MFA for all users)
- AWS FedRAMP Moderate environment provides baseline physical and infrastructure controls
- Good logging and monitoring (CloudWatch, CloudTrail, AWS GuardDuty)
- Documented incident response plan

**Gaps:**
- No formal vulnerability management program (3.11.2)
- Security awareness training not formalized (3.2.1)
- Configuration management documentation incomplete (3.4.1)
- No file integrity monitoring (3.14.10)

**Expected Score:** 95-100 out of 110 (moderate gaps requiring remediation)

## How to Use This Example

1. Review the scoping worksheet to see how CloudSync defined their assessment boundary
2. Examine the control assessment sample to understand how to evaluate controls with cloud infrastructure
3. Look at the evidence index to see what artifacts support "Met" determinations
4. Use this as a template for similar small SaaS companies operating in cloud environments
