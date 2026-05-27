# CMMC Level 2 Self-Assessment Scoping Worksheet

**Organization Name:** ____________________
**Assessment Date:** ____________________
**Completed By:** ____________________
**Review Date:** ____________________

## Section 1: Customer Request Details

**Customer Name:** ____________________
**Prime Contract Number (if applicable):** ____________________
**Date Requested:** ____________________

**What did the customer request? (Check all that apply)**
- [ ] SPRS score only
- [ ] Self-assessment questionnaire
- [ ] Attestation letter
- [ ] Full assessment report package
- [ ] Plan of Action and Milestones (POA&M)
- [ ] Evidence index or artifact list
- [ ] Other: ____________________

**Due Date:** ____________________
**Point of Contact at Customer:** ____________________

## Section 2: CUI Determination

**Does your organization handle Covered Defense Information (CDI) or other Controlled Unclassified Information (CUI)?**
- [ ] Yes
- [ ] No

**If Yes, what types of CUI does your organization handle?**
- [ ] Technical data marked as distribution statement C or higher
- [ ] Export-controlled technical data (ITAR/EAR)
- [ ] Operationally critical technical data
- [ ] DoD-marked CUI
- [ ] Other: ____________________

**How is CUI received?**
- [ ] Email
- [ ] Secure file transfer portal
- [ ] Physical media
- [ ] Customer portal or collaboration platform
- [ ] Other: ____________________

**Where is CUI stored?**
- [ ] Cloud services (specify: ____________________)
- [ ] On-premises servers
- [ ] Workstations or laptops
- [ ] Mobile devices
- [ ] Not stored (processed only)
- [ ] Other: ____________________

## Section 3: Assessment Boundary Definition

The assessment boundary defines which systems, networks, people, and facilities are in scope for this assessment.

### Systems in Scope

List all systems that process, store, or transmit CUI:

| System Name | Description | Hosted Where | Primary Function |
|-------------|-------------|--------------|------------------|
| Example: CRM | Salesforce instance | Cloud (Salesforce) | Customer data management |
| | | | |
| | | | |
| | | | |

### Network Segments in Scope

List network segments that carry or protect CUI:

| Network Segment | CIDR / VLAN | Description | Connectivity |
|-----------------|-------------|-------------|--------------|
| Example: Production VPC | 10.0.0.0/16 | AWS production environment | Isolated from corporate |
| | | | |
| | | | |

### Personnel in Scope

**Number of personnel with CUI access:** ____________________

**Roles with CUI access:**
- [ ] Executives
- [ ] Engineers/Developers
- [ ] System Administrators
- [ ] Support Staff
- [ ] Subcontractors
- [ ] Other: ____________________

### Facilities in Scope

List physical locations where CUI is handled:

| Facility Address | Type | CUI Handled Here? | Physical Controls |
|------------------|------|-------------------|-------------------|
| | Office | [ ] Yes [ ] No | |
| | Data Center | [ ] Yes [ ] No | |
| | Home Office | [ ] Yes [ ] No | |

## Section 4: Asset Categorization

Per the CMMC Scoping Guide, categorize assets related to the assessment boundary:

### CUI Assets
Assets that process, store, or transmit CUI.

| Asset Name | Type | Description |
|------------|------|-------------|
| | | |
| | | |

### Security Protection Assets
Assets that provide security functions for CUI Assets (firewalls, SIEM, MFA servers, etc.).

| Asset Name | Type | Security Function |
|------------|------|-------------------|
| | | |
| | | |

### Contractor Risk Managed Assets
Assets outside the boundary but posing risk if compromised (corporate network, email, etc.).

| Asset Name | Type | Risk Mitigation Measures |
|------------|------|--------------------------|
| | | |
| | | |

### Specialized Assets
Non-IT assets with unique security characteristics (IoT, OT, test equipment).

| Asset Name | Type | Special Considerations |
|------------|------|------------------------|
| | | |
| | | |

### Out-of-Scope Assets
Assets explicitly excluded from the assessment boundary.

| Asset Name | Type | Reason for Exclusion |
|------------|------|----------------------|
| | | |
| | | |

## Section 5: External Services and Connections

### Cloud Service Providers

| Provider | Service Used | FedRAMP Authorized? | CUI Stored? |
|----------|--------------|---------------------|-------------|
| Example: AWS | EC2, S3, RDS | Moderate | Yes |
| | | | |
| | | | |

### External Connections

| Connection To | Purpose | Type | Security Controls |
|---------------|---------|------|-------------------|
| Example: Customer VPN | Access to customer portal | VPN | MFA, AES-256 |
| | | | |
| | | | |

### Third-Party Services with CUI Access

| Service Provider | Service | Data Shared | BAA/NDA in Place? |
|------------------|---------|-------------|-------------------|
| | | | [ ] Yes [ ] No |
| | | | [ ] Yes [ ] No |

## Section 6: Scoping Exclusions and Limitations

**Are there any systems, networks, or facilities that handle CUI but are excluded from this assessment?**
- [ ] Yes (explain below)
- [ ] No

**Exclusions and Justifications:**

| Excluded Item | Reason for Exclusion | Planned Inclusion Date |
|---------------|----------------------|------------------------|
| | | |
| | | |

**Known Limitations of This Assessment:**
-
-
-

## Section 7: Approval

**Assessment Scope Approved By:**

Name: ____________________
Title: ____________________
Signature: ____________________
Date: ____________________

**Security Point of Contact:**

Name: ____________________
Title: ____________________
Email: ____________________
Phone: ____________________
