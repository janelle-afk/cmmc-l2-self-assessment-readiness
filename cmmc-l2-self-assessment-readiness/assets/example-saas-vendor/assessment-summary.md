# CloudSync Inc. Assessment Summary

**Assessment Date:** 2026-04-15
**Assessed By:** Sarah Chen (CISO), David Kim (DevOps Lead)
**Assessment Scope:** Production systems handling CUI in AWS us-gov-west-1

## Executive Summary

CloudSync Inc. completed a NIST SP 800-171 self-assessment using the DoD Assessment Methodology. The assessment evaluated all 110 security requirements across the CloudSync production environment that processes, stores, and transmits Controlled Unclassified Information for Department of Defense customers.

**Final SPRS Score: 97 out of 110**

This score reflects a strong security posture with minor gaps requiring remediation. CloudSync has documented remediation plans for all identified deficiencies.

## Assessment Approach

The assessment was conducted over 3 weeks using the following methods:

- **Examine:** Reviewed AWS configurations, Okta settings, security policies, and FedRAMP documentation
- **Interview:** Interviewed 8 personnel with CUI access (engineers, DevOps, CEO)
- **Test:** Performed technical validation of access controls, encryption, and monitoring capabilities

## Key Findings by Control Family

### Strong Areas

**3.1 Access Control (22 requirements) - 21 Met, 1 Not Met**
- Okta SSO with MFA provides strong authentication across all systems
- AWS IAM policies enforce least privilege
- Session timeouts configured per policy
- Gap: Control 3.1.22 (public posting controls) needs formalized review process

**3.5 Identification and Authentication (11 requirements) - All Met**
- MFA enforced for all users via Okta (hardware tokens and push notifications)
- Password complexity enforced (14 characters minimum, complexity requirements)
- Replay-resistant authentication via SAML and OAuth 2.0
- FIPS 140-2 validated cryptography for password storage

**3.13 System and Communications Protection (16 requirements) - All Met**
- TLS 1.3 for all data in transit
- AES-256 encryption at rest via AWS KMS
- Network segmentation with private subnets
- Default-deny firewall rules via AWS Security Groups
- FIPS-validated cryptography throughout

**3.3 Audit and Accountability (9 requirements) - All Met**
- CloudTrail logs all API calls and data access
- Logs centralized in dedicated S3 bucket with 90-day retention
- GuardDuty provides real-time analysis
- Log access restricted to DevOps team
- Automated alerts on critical events

### Areas Requiring Remediation

**3.2 Awareness and Training (3 requirements) - 1 Met, 2 Not Met**
- Gap: No formal security awareness training program (3.2.1) - 3 point deduction
- Gap: No insider threat awareness training (3.2.3) - 3 point deduction
- Training happens informally; needs documented program with completion tracking

**3.4 Configuration Management (9 requirements) - 8 Met, 1 Not Met**
- Gap: Baseline configurations not fully documented (3.4.1) - 3 point deduction
- Using Terraform for infrastructure-as-code but baselines not explicitly documented
- Need to formalize baseline documentation and approval process

**3.11 Risk Assessment (6 requirements) - 5 Met, 1 Not Met**
- Gap: No formal vulnerability scanning program (3.11.2) - 3 point deduction
- AWS Inspector runs occasionally but not on defined schedule
- Need to implement continuous vulnerability scanning

**3.14 System and Information Integrity (13 requirements) - 12 Met, 1 Not Met**
- Gap: No file integrity monitoring (3.14.10) - 1 point deduction
- Application code integrity verified via git signatures
- Need to implement host-based file integrity monitoring for EC2 instances

## Point Deduction Summary

| Control ID | Control Title | Deduction | Priority |
|------------|---------------|-----------|----------|
| 3.2.1 | Security awareness training | 3 points | High |
| 3.2.3 | Insider threat training | 3 points | High |
| 3.4.1 | Baseline configurations | 3 points | Medium |
| 3.11.2 | Vulnerability scanning | 3 points | High |
| 3.14.10 | File integrity monitoring | 1 point | Low |
| **Total** | | **13 points** | |

**Final Score: 110 - 13 = 97**

## Remediation Plan Summary

All gaps have documented remediation plans with target completion within 90 days:

1. **Security Awareness Training (Q2 2026)**
   - Procure KnowBe4 platform
   - Develop custom training modules
   - Mandatory completion for all employees
   - Estimated cost: $3,000/year

2. **Vulnerability Scanning (Q2 2026)**
   - Configure AWS Inspector on weekly schedule
   - Integrate with GuardDuty for alerting
   - Establish remediation SLA (Critical: 7 days, High: 30 days)
   - No additional cost (AWS service included)

3. **Configuration Baselines (Q3 2026)**
   - Document current Terraform configs as approved baselines
   - Implement change control process
   - Quarterly baseline review
   - Internal effort only

4. **File Integrity Monitoring (Q3 2026)**
   - Deploy OSSEC or AWS Systems Manager
   - Configure monitoring on critical system files
   - Establish baseline and alert thresholds
   - Estimated cost: $0-500/year

**Projected Score After Remediation: 110 out of 110**

## Strengths and Differentiators

CloudSync's cloud-native architecture and use of FedRAMP-authorized services provides significant security advantages:

- **Leveraged FedRAMP Controls:** Many physical and infrastructure controls (3.7, 3.8, 3.10 families) met through AWS FedRAMP authorization
- **Strong Identity Management:** Okta SSO with MFA eliminates password-based attacks
- **Comprehensive Logging:** CloudTrail and GuardDuty provide visibility across entire environment
- **Infrastructure as Code:** Terraform ensures consistent, auditable deployments
- **Encryption Everywhere:** Data encrypted at rest and in transit using FIPS-validated cryptography

## Assessment Limitations

- Physical security controls assessed based on AWS FedRAMP documentation rather than direct inspection
- Self-assessment conducted by internal personnel; not independently verified by C3PAO
- Assessment represents point-in-time snapshot as of April 15, 2026

## Conclusion

CloudSync Inc. demonstrates a strong security posture appropriate for handling CUI in a cloud environment. The identified gaps are well-understood and have clear remediation paths. The score of 97 out of 110 reflects CloudSync's commitment to protecting customer data and meeting DoD cybersecurity requirements.

With remediation plans on track for completion by Q3 2026, CloudSync will achieve full compliance with all 110 NIST SP 800-171 requirements.
