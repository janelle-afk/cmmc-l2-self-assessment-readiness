---
name: cmmc-l2-self-assessment-readiness
description: Guide vendors through completing CMMC Level 2 / NIST SP 800-171 self-assessments for Defense Industrial Base customers. Use when a customer asks for CMMC self-assessment, NIST 800-171 assessment, SPRS score generation, vendor security questionnaire (CMMC context), prime contractor flowdown compliance, or DoD cybersecurity attestation. Covers all 110 requirements across 14 families, SPRS scoring per DoD Assessment Methodology, POA&M generation, and customer-facing deliverables including attestation letters.
---

# CMMC Level 2 Self-Assessment Readiness

## Overview

This skill guides vendors through completing a CMMC Level 2 self-assessment in response to customer requests from the Defense Industrial Base (DIB). The assessment evaluates implementation of NIST SP 800-171 Rev 2 (110 security requirements across 14 families) using the DoD Assessment Methodology, generates an SPRS score, and produces customer-facing deliverables.

This is for vendor self-attestation, not C3PAO certification. The output must be defensible if escalated or if the vendor later pursues formal certification.

## When to Use This Skill

- Customer (prime contractor or DoD end customer) requests a CMMC self-assessment
- Vendor needs to complete NIST 800-171 self-assessment for contract compliance
- Customer asks for SPRS score before contract award
- Prime contractor flowdown requires cybersecurity attestation
- Vendor needs to prepare for SPRS submission
- Annual self-assessment required under DFARS clauses

## Assessment Workflow

### Phase 1: Intake and Scoping

**Goal:** Understand customer requirements and define the assessment boundary.

1. **Clarify Customer Request**
   - What exactly did the customer ask for?
     - SPRS score only
     - Questionnaire completion
     - Attestation letter
     - Full assessment package (report + POA&M + attestation)
   - Due date and point of contact
   - Contract context (new award, annual refresh, flowdown requirement)

2. **Complete Scoping Worksheet**
   - Use `assets/scoping-worksheet.md` as the template
   - Determine if the vendor handles CUI (Covered Defense Information or other controlled information)
   - Identify all systems, networks, personnel, and facilities that process/store/transmit CUI
   - Categorize assets per CMMC Scoping Guide:
     - **CUI Assets:** Systems that directly handle CUI
     - **Security Protection Assets:** Firewalls, SIEM, MFA servers, monitoring tools
     - **Contractor Risk Managed Assets:** Corporate network, email, HR systems
     - **Specialized Assets:** IoT, OT, test equipment
     - **Out-of-Scope:** Explicitly excluded systems
   - Document external connections, cloud services, third-party access

3. **Define Assessment Boundary**
   - The boundary determines which controls apply
   - Be precise about what is in scope and what is not
   - Document any exclusions with justification

**Deliverable:** Completed scoping worksheet defining the assessment boundary.

### Phase 2: Control-by-Control Assessment

**Goal:** Evaluate all 110 NIST SP 800-171 requirements and determine Met, Not Met, or Not Applicable status.

1. **Reference the Control Catalog**
   - All 110 requirements with assessment objectives are in `references/nist-800-171-controls.md`
   - Each requirement has multiple assessment objectives from NIST SP 800-171A
   - Assessment methods: Examine (documentation/configurations), Interview (personnel), Test (technical validation)

2. **Use the Control Assessment Workbook**
   - `assets/control-assessment-workbook.csv` contains all 110 controls and 320+ assessment objectives
   - For each control, determine:
     - **Status:** Met, Not Met, or Not Applicable
     - **Implementation Details:** Specific description of how the control is implemented
     - **Evidence Reference:** Link to evidence artifact(s) in the evidence index
     - **Gap Description:** If Not Met, describe the gap
     - **Point Deduction:** If Not Met, assign 1, 3, or 5 points per DoD Assessment Methodology

3. **Apply Assessment Methods**
   - **Examine:** Review policies, procedures, configurations, system settings, documentation
   - **Interview:** Discuss with personnel (admins, users, management) to verify practices
   - **Test:** Perform technical validation (attempt unauthorized access, verify encryption, test MFA)

4. **Collect and Index Evidence**
   - Use `assets/evidence-index.md` to track all evidence artifacts
   - Every control marked "Met" MUST reference documented evidence
   - Evidence types: policies, configuration exports, logs, screenshots, interview notes, test results, training records
   - Organize evidence by control for traceability

5. **Assign Point Deductions (DoD Assessment Methodology)**
   - **5 points:** Control not implemented or does not meet intent
   - **3 points:** Control partially implemented with significant gaps
   - **1 point:** Control implemented with minor deficiencies
   - **0 points:** Control fully met or not applicable

**Guardrails:**
- NEVER mark a control "Met" without recorded evidence in the evidence index
- NEVER mark a control "Not Applicable" without written justification
- Use specific implementation language, not marketing voice
- Be honest about gaps; defensibility depends on accuracy

**Deliverable:** Completed control assessment workbook with status, evidence, and point deductions for all 110 requirements.

### Phase 3: SPRS Scoring

**Goal:** Calculate the SPRS score using the DoD Assessment Methodology.

1. **Run the Score Calculation Script**
   - Use `scripts/calculate_sprs_score.py` with the completed workbook:
     ```bash
     python3 scripts/calculate_sprs_score.py control-assessment-workbook.csv
     ```
   - The script calculates:
     - Final SPRS score (110 minus total deductions)
     - Breakdown by control family
     - List of gaps with point deductions

2. **Validate the Score**
   - Review the output for correctness
   - Ensure point deductions align with gap severity
   - Verify that each "Not Met" control has an assigned deduction

3. **Interpret the Score**
   - **110:** Perfect score, all requirements met
   - **100-109:** Strong posture with minor gaps
   - **90-99:** Moderate posture, some remediation needed
   - **Below 90:** Significant gaps requiring immediate attention

**Deliverable:** SPRS score out of 110 with family-level breakdown and gap list.

### Phase 4: Gap Analysis and POA&M

**Goal:** Document remediation plans for all "Not Met" controls.

1. **Create the POA&M**
   - Use `assets/poam-template.md`
   - For each gap (Not Met control), document:
     - Gap description (what is missing or inadequate)
     - Current vs. target implementation state
     - Remediation milestones with owners and target dates
     - Resources required (budget, personnel, tools)
     - Success criteria and validation method

2. **Prioritize Remediation**
   - Focus on 5-point deductions first (most critical)
   - Identify "quick wins" (low effort, high impact)
   - Flag any gaps that would block future C3PAO certification

3. **Develop Remediation Timeline**
   - Quarterly milestones showing score improvement trajectory
   - Target completion date for full remediation
   - Risk acceptance for any gaps that cannot be remediated

**Deliverable:** Comprehensive POA&M with remediation plans, timeline, and resource estimates.

### Phase 5: Customer-Facing Deliverables

**Goal:** Produce professional deliverables the customer can review and accept.

1. **Customer Report**
   - Use `assets/customer-report-template.md`
   - Executive summary (one page)
   - Assessment methodology statement
   - Results by control family (table format)
   - SPRS score and calculation
   - Gap summary with remediation commitment
   - Assessment limitations and scope boundaries

2. **Attestation Letter**
   - Use `assets/attestation-letter-template.md`
   - Formal attestation by responsible official (named individual with title and signature)
   - SPRS score and date
   - Statement of assessment methodology
   - Commitment to remediation per POA&M
   - Regulatory compliance references (DFARS clauses)

   **Critical:** NEVER produce an attestation letter without:
   - Named accountable officer
   - Title and signature line
   - Specific date
   - Accurate SPRS score

3. **Optional: Redacted Evidence Index**
   - If customer requests evidence visibility, provide redacted version
   - Remove: internal IPs, hostnames, employee names, proprietary implementation details
   - Retain: sufficient detail to demonstrate control implementation

**Deliverable:** Complete customer package ready for submission.

## Guardrails and Quality Standards

**Evidence Requirements:**
- Every "Met" determination MUST have documented evidence
- No control can be marked "Met" without evidence references in the evidence index
- Evidence must be current (collected during assessment period)

**Not Applicable Justifications:**
- Every "NA" determination MUST have written justification
- Flag any questionable NA determinations for review
- Most controls apply to any system handling CUI; true NAs are rare

**Attestation Requirements:**
- NEVER produce attestation without named responsible official and date
- Official must have authority to attest (typically CISO, CIO, or executive)
- Attestation must accurately reflect the assessment date and score

**Defensibility:**
- Use specific technical language (not marketing voice)
- Reference actual system names, tools, configurations
- Be honest about gaps; credibility matters more than perfect scores
- Assume customer may escalate or request evidence review

**No Em Dashes:**
- Do not use em dashes (—) in any generated output
- Use colons, commas, or separate sentences instead

## Regulatory Context

Brief context on why customers request these assessments is in `references/dfars-context.md`. Key points:

- **DFARS 252.204-7012:** Requires NIST 800-171 implementation for contractors with CUI
- **DFARS 252.204-7020:** Requires current assessment (no more than 3 years old) posted to SPRS
- **32 CFR Part 170:** Establishes CMMC program and self-assessment requirements
- Prime contractors flow down these requirements to subcontractors for supply chain risk management

## Tips for Common Scenarios

**Small SaaS Vendor in Cloud:**
- Focus on cloud service provider (CSP) FedRAMP authorization as evidence for many controls
- Physical controls (3.10 family) may apply to CSP, not vendor
- Remote workforce requires attention to 3.10.6 (alternate work site safeguards)

**On-Premises Manufacturing:**
- Strong physical controls (facilities, badge access) provide good 3.10 coverage
- OT/ICS systems may be specialized assets with tailored controls
- Air-gapped networks simplify some boundary protection controls

**Hybrid Environment:**
- Clearly define boundary between corporate and CUI environments
- Network segmentation is critical (3.13 family)
- Identity management across environments requires careful assessment (3.5 family)

**Customer Asks for Score Only:**
- Still complete the full assessment internally for defensibility
- Score without supporting evidence is not credible
- Provide at minimum: score, methodology statement, attestation

**Customer Asks for Full Package:**
- Deliver: assessment report, POA&M, attestation letter, (optionally) redacted evidence index
- Ensure all documents are internally consistent (same score, same date, same scope)

## Working with This Skill

1. Start by completing the scoping worksheet with the vendor
2. Walk through the control assessment workbook systematically by family
3. Build the evidence index concurrently with control assessment
4. Run the scoring script to validate point deductions and calculate final score
5. Create the POA&M for all gaps
6. Generate customer deliverables using templates
7. Review all outputs for consistency, accuracy, and defensibility before delivery

## Resources

- `references/nist-800-171-controls.md` - All 110 requirements with assessment objectives (read as needed during control assessment)
- `references/dfars-context.md` - Regulatory background (read if customer asks why this is required)
- `scripts/calculate_sprs_score.py` - SPRS score calculator (execute after completing workbook)
- `assets/scoping-worksheet.md` - Assessment boundary template
- `assets/control-assessment-workbook.csv` - All 110 controls and 320+ objectives
- `assets/evidence-index.md` - Evidence artifact tracking
- `assets/poam-template.md` - Remediation planning template
- `assets/customer-report-template.md` - Customer-facing assessment report
- `assets/attestation-letter-template.md` - Formal attestation letter
