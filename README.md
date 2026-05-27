# CMMC Level 2 Self-Assessment Readiness Skill

A comprehensive AI agent skill for guiding Defense Industrial Base (DIB) vendors through CMMC Level 2 and NIST SP 800-171 Rev 2 self-assessments.

## Overview

This skill enables security teams to efficiently complete vendor self-assessments for Department of Defense contracts. It covers all 110 NIST SP 800-171 security requirements across 14 control families, implements the DoD Assessment Methodology for SPRS scoring, and generates professional customer-facing deliverables.

### What This Skill Does

- **Guides Assessment Process**: 5-phase workflow from scoping through final deliverables
- **Evaluates All 110 Controls**: Complete control-by-control assessment with 320+ objectives
- **Calculates SPRS Scores**: Automated scoring per DoD Assessment Methodology
- **Generates Deliverables**: Customer reports, POA&Ms, attestation letters
- **Ensures Quality**: Built-in guardrails for evidence requirements and defensibility

## Use Cases

Use this skill when:
- A prime contractor requests CMMC self-assessment or SPRS score
- DoD customer asks for NIST 800-171 compliance attestation
- Responding to vendor security questionnaires (CMMC context)
- Preparing for SPRS submission or annual self-assessment
- Planning remediation for identified security gaps

## Skill Structure

```
cmmc-l2-self-assessment-readiness/
├── SKILL.md                          # Main workflow guide
├── README.md                         # This file
├── scripts/
│   └── calculate_sprs_score.py      # SPRS score calculator
├── references/
│   ├── nist-800-171-controls.md     # All 110 requirements with objectives
│   └── dfars-context.md             # Regulatory background
└── assets/
    ├── scoping-worksheet.md         # Assessment boundary template
    ├── control-assessment-workbook.csv  # Complete control checklist
    ├── evidence-index.md            # Evidence tracking template
    ├── poam-template.md             # Remediation planning template
    ├── customer-report-template.md  # Customer-facing report
    ├── attestation-letter-template.md   # Formal attestation
    └── example-saas-vendor/         # Worked example
        ├── README.md
        ├── scoping-worksheet-completed.md
        └── assessment-summary.md
```

## Key Features

### Comprehensive Control Coverage

- **14 Control Families**: Access Control, Awareness & Training, Audit & Accountability, Configuration Management, Identification & Authentication, Incident Response, Maintenance, Media Protection, Personnel Security, Physical Protection, Risk Assessment, Security Assessment, System & Communications Protection, System & Information Integrity
- **110 Requirements**: All NIST SP 800-171 Rev 2 security requirements
- **320+ Assessment Objectives**: Detailed objectives from NIST SP 800-171A
- **Assessment Methods**: Examine, Interview, and Test approaches for each control

### SPRS Score Calculation

Automated calculation using DoD Assessment Methodology:
- **5 points**: Control not implemented or does not meet intent
- **3 points**: Control partially implemented with significant gaps
- **1 point**: Control implemented with minor deficiencies
- **0 points**: Control fully met

Score = 110 minus total point deductions

### Professional Deliverables

Generate customer-ready documents:
- Executive summary and assessment report
- Family-by-family results tables
- SPRS score with methodology statement
- Plan of Action and Milestones (POA&M)
- Signed attestation letter with regulatory references
- Optional redacted evidence index

### Quality Guardrails

Built-in safeguards ensure defensible assessments:
- **Evidence Required**: Cannot mark control "Met" without documented evidence
- **NA Justification**: Every "Not Applicable" requires written justification
- **Attestation Controls**: Must include named officer, title, signature line, and date
- **Honest Assessment**: Emphasizes specific implementation details over marketing language
- **No Em Dashes**: Style compliance for professional documents

## Assessment Workflow

### Phase 1: Intake and Scoping
- Clarify customer requirements (score only vs. full package)
- Complete scoping worksheet
- Define assessment boundary per CMMC Scoping Guide
- Categorize assets (CUI, Security Protection, Risk Managed, Specialized, Out-of-Scope)

### Phase 2: Control-by-Control Assessment
- Walk through all 110 requirements
- Apply Examine/Interview/Test methods
- Document implementation details
- Collect and index evidence artifacts
- Assign Met/Not Met/Not Applicable status
- Determine point deductions for gaps

### Phase 3: SPRS Scoring
- Run automated score calculation script
- Validate point deductions align with gap severity
- Generate family-level breakdown
- Interpret overall security posture

### Phase 4: Gap Analysis and POA&M
- Document all "Not Met" controls
- Define remediation plans with milestones
- Assign owners and target dates
- Estimate resources required
- Prioritize by point deduction value

### Phase 5: Customer Deliverables
- Generate assessment report
- Create attestation letter with named official
- Optionally provide redacted evidence index
- Ensure document consistency (score, date, scope)

## Usage Example

```
User: "Our prime contractor Lockheed Martin asked us to complete a CMMC
self-assessment for our subcontract. They need our SPRS score and an
attestation letter by end of month."

Agent: I'll guide you through the CMMC Level 2 self-assessment process.
Let's start by completing the scoping worksheet to define your assessment
boundary...

[Workflow continues through all 5 phases]

Agent: Here's your complete deliverable package:
- SPRS Score: 97 out of 110
- Customer Report: [report.md]
- Attestation Letter: [attestation.md] (ready for CISO signature)
- POA&M: [poam.md] (4 gaps, 90-day remediation plan)
```

## Technical Requirements

### Script Dependencies

The SPRS calculator script requires:
- Python 3.6 or higher
- Standard library only (csv, sys, collections, typing)

No external dependencies needed.

### Input Format

Control assessment workbook must be CSV with columns:
- Control ID
- Control Title
- Assessment Objective ID
- Assessment Objective
- Assessment Methods
- Status (Met/Not Met/Not Applicable)
- Implementation Details
- Evidence Reference
- Gap Description
- Point Deduction (0, 1, 3, or 5)

## Worked Example

The `assets/example-saas-vendor/` directory contains a complete example for **CloudSync Inc.**, a fictional 30-employee SaaS company:

- **Environment**: 100% AWS cloud (us-gov-west-1), remote workforce
- **CUI Handling**: DoD customer contracts with technical documents
- **Score**: 97 out of 110
- **Key Gaps**: Security training, vulnerability scanning, configuration baselines, file integrity monitoring

This example demonstrates the workflow for small cloud-based vendors.

## Regulatory Compliance

This skill aligns with:
- **NIST SP 800-171 Rev 2**: 110 security requirements for protecting CUI
- **NIST SP 800-171A**: Assessment procedures with Examine/Interview/Test methods
- **DoD Assessment Methodology**: SPRS scoring (1, 3, or 5 point deductions)
- **DFARS 252.204-7012**: Safeguarding CUI and cyber incident reporting
- **DFARS 252.204-7019**: Notice of assessment requirements
- **DFARS 252.204-7020**: Assessment requirements and SPRS posting
- **32 CFR Part 170**: CMMC program regulations

## Tips for Common Scenarios

### Small SaaS Vendor (Cloud)
- Leverage CSP FedRAMP authorization for infrastructure controls
- Physical controls (3.10 family) often covered by cloud provider
- Focus on application-layer controls and access management
- Remote workforce requires attention to alternate work site safeguards (3.10.6)

### Manufacturing (On-Premises)
- Strong physical security provides good 3.10 coverage
- OT/ICS systems may need specialized assessment approach
- Air-gapped networks simplify some boundary protection controls
- Media handling and sanitization typically more complex

### Hybrid Environment
- Clearly define boundary between corporate and CUI environments
- Network segmentation is critical (3.13 family)
- Identity management across environments requires careful assessment
- Document how controls apply differently to each environment

## Self-Assessment vs. C3PAO Certification

**This skill is for self-assessments**, which are:
- Conducted by contractor personnel
- Use DoD Assessment Methodology
- Require attestation by responsible official
- Posted to SPRS annually
- Sufficient for many contracts

**C3PAO Certification** is:
- Conducted by certified third-party assessors
- Required when contract explicitly demands CMMC Level 2 certification
- More rigorous evidence requirements
- Valid for 3 years
- Emerging requirement as CMMC program matures

## License

[Specify your license here]

## Contributing

[Specify contribution guidelines if accepting contributions]

## Support

For questions or issues:
- Review the worked example in `assets/example-saas-vendor/`
- Consult `references/nist-800-171-controls.md` for control details
- Refer to `references/dfars-context.md` for regulatory background

## Version History

- **v1.0.0** (2026-05-08): Initial release
  - Complete workflow for all 110 NIST 800-171 requirements
  - SPRS score calculator
  - Full template library
  - CloudSync worked example

## Authors

Developed for use with AI agent platforms supporting skills.

## Acknowledgments

Based on:
- NIST Special Publication 800-171 Revision 2
- NIST Special Publication 800-171A
- DoD Assessment Methodology
- CMMC Model Version 2.0
