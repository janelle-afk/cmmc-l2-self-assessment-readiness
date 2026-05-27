# CMMC Level 2 Self-Assessment Scoping Worksheet

**Organization Name:** CloudSync Inc.
**Assessment Date:** 2026-04-15
**Completed By:** Sarah Chen, CISO
**Review Date:** 2026-04-16

## Section 1: Customer Request Details

**Customer Name:** Lockheed Martin Aeronautics
**Prime Contract Number (if applicable):** FA8625-25-C-0042 (subcontract)
**Date Requested:** 2026-03-15

**What did the customer request? (Check all that apply)**
- [x] SPRS score only
- [ ] Self-assessment questionnaire
- [x] Attestation letter
- [ ] Full assessment report package
- [ ] Plan of Action and Milestones (POA&M)
- [ ] Evidence index or artifact list
- [ ] Other: ____________________

**Due Date:** 2026-04-15
**Point of Contact at Customer:** James Rodriguez, Supply Chain Security Manager (james.rodriguez@lm.com)

## Section 2: CUI Determination

**Does your organization handle Covered Defense Information (CDI) or other Controlled Unclassified Information (CUI)?**
- [x] Yes
- [ ] No

**If Yes, what types of CUI does your organization handle?**
- [x] Technical data marked as distribution statement C or higher
- [ ] Export-controlled technical data (ITAR/EAR)
- [x] Operationally critical technical data
- [x] DoD-marked CUI
- [ ] Other: ____________________

**How is CUI received?**
- [x] Email (via encrypted channels)
- [x] Secure file transfer portal
- [ ] Physical media
- [x] Customer portal or collaboration platform (our SaaS product)
- [ ] Other: ____________________

**Where is CUI stored?**
- [x] Cloud services (specify: AWS us-gov-west-1 FedRAMP Moderate)
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
| CloudSync Production | Main SaaS application | AWS us-gov-west-1 | Document collaboration platform for DoD customers |
| RDS Database | PostgreSQL database | AWS us-gov-west-1 RDS | Stores customer data including CUI documents |
| S3 Storage (CUI Bucket) | Object storage for uploaded files | AWS S3 us-gov-west-1 | CUI document storage with encryption at rest |
| Okta SSO | Identity provider | Okta FedRAMP Moderate | Authentication and MFA for all users |
| AWS CloudTrail | Audit logging service | AWS us-gov-west-1 | Records all API calls and access events |
| AWS GuardDuty | Threat detection | AWS us-gov-west-1 | Monitors for malicious activity |

### Network Segments in Scope

List network segments that carry or protect CUI:

| Network Segment | CIDR / VLAN | Description | Connectivity |
|-----------------|-------------|-------------|--------------|
| Production VPC | 10.100.0.0/16 | AWS VPC for production workloads | Isolated from corporate; private subnets only |
| Application Subnet | 10.100.10.0/24 | EC2 instances running app servers | Private subnet, no direct internet access |
| Database Subnet | 10.100.20.0/24 | RDS instances | Private subnet, application tier only |
| Management Subnet | 10.100.1.0/24 | Bastion hosts for admin access | Restricted access via VPN + MFA |

### Personnel in Scope

**Number of personnel with CUI access:** 8

**Roles with CUI access:**
- [x] Executives (CEO for customer escalations)
- [x] Engineers/Developers (5 backend engineers with production access)
- [x] System Administrators (2 DevOps engineers)
- [ ] Support Staff
- [ ] Subcontractors
- [ ] Other: ____________________

### Facilities in Scope

List physical locations where CUI is handled:

| Facility Address | Type | CUI Handled Here? | Physical Controls |
|------------------|------|-------------------|-------------------|
| N/A (Cloud-only) | Cloud Infrastructure | [x] Yes [ ] No | AWS data center (FedRAMP controls apply) |
| Employee Home Offices | Home Office | [x] Yes [ ] No | Endpoint encryption, VPN required |

## Section 4: Asset Categorization

Per the CMMC Scoping Guide, categorize assets related to the assessment boundary:

### CUI Assets
Assets that process, store, or transmit CUI.

| Asset Name | Type | Description |
|------------|------|-------------|
| CloudSync Production App | Application | Web application serving DoD customers |
| RDS PostgreSQL Database | Database | Stores CUI documents and metadata |
| S3 CUI Bucket | Object Storage | Encrypted storage for uploaded CUI files |

### Security Protection Assets
Assets that provide security functions for CUI Assets (firewalls, SIEM, MFA servers, etc.).

| Asset Name | Type | Security Function |
|------------|------|-------------------|
| AWS WAF | Web Application Firewall | Protects application from web attacks |
| AWS Security Groups | Network Firewall | Controls traffic between subnets |
| Okta SSO | Authentication | Provides MFA and SSO for all users |
| AWS GuardDuty | Threat Detection | Monitors for malicious activity |
| AWS CloudTrail | Audit Logging | Records all API and access events |
| AWS KMS | Key Management | Manages encryption keys for data at rest |

### Contractor Risk Managed Assets
Assets outside the boundary but posing risk if compromised (corporate network, email, etc.).

| Asset Name | Type | Risk Mitigation Measures |
|------------|------|--------------------------|
| Google Workspace | Corporate Email/Docs | Separate from production; MFA required; no CUI storage |
| GitHub Enterprise | Source Code Repository | 2FA required; production secrets in AWS Secrets Manager, not GitHub |
| Slack | Internal Communications | CUI prohibited in Slack per policy; monitoring for violations |

### Specialized Assets
Non-IT assets with unique security characteristics (IoT, OT, test equipment).

| Asset Name | Type | Special Considerations |
|------------|------|------------------------|
| N/A | N/A | None |

### Out-of-Scope Assets
Assets explicitly excluded from the assessment boundary.

| Asset Name | Type | Reason for Exclusion |
|------------|------|----------------------|
| Marketing Website | Web Application | Public-facing; does not handle CUI |
| Staging Environment | Test Environment | Does not contain production CUI data |
| Corporate Office Network | Network | Remote-only company; no office |

## Section 5: External Services and Connections

### Cloud Service Providers

| Provider | Service Used | FedRAMP Authorized? | CUI Stored? |
|----------|--------------|---------------------|-------------|
| AWS | EC2, RDS, S3, CloudTrail, GuardDuty, KMS | Yes (Moderate, us-gov) | Yes |
| Okta | SSO and MFA | Yes (Moderate) | No (metadata only) |

### External Connections

| Connection To | Purpose | Type | Security Controls |
|---------------|---------|------|-------------------|
| Customer VPN (optional) | Direct integration for some customers | IPsec VPN | Pre-shared keys, AES-256, customer-managed |
| Okta Federation | SSO authentication | SAML 2.0 over TLS 1.3 | Certificate-based trust |

### Third-Party Services with CUI Access

| Service Provider | Service | Data Shared | BAA/NDA in Place? |
|------------------|---------|-------------|-------------------|
| N/A | None | None | N/A |

## Section 6: Scoping Exclusions and Limitations

**Are there any systems, networks, or facilities that handle CUI but are excluded from this assessment?**
- [ ] Yes (explain below)
- [x] No

**Exclusions and Justifications:**

| Excluded Item | Reason for Exclusion | Planned Inclusion Date |
|---------------|----------------------|------------------------|
| N/A | N/A | N/A |

**Known Limitations of This Assessment:**
- Physical security controls (3.10 family) rely on AWS FedRAMP authorization; CloudSync does not directly control data center physical access
- Some controls assessed based on AWS documentation and CloudSync configuration rather than direct testing of AWS infrastructure
- Assessment performed by internal team (self-assessment); not independently validated by C3PAO

## Section 7: Approval

**Assessment Scope Approved By:**

Name: Sarah Chen
Title: Chief Information Security Officer
Signature: [Signed]
Date: 2026-04-16

**Security Point of Contact:**

Name: Sarah Chen
Title: CISO
Email: sarah.chen@cloudsync.example
Phone: (555) 123-4567
