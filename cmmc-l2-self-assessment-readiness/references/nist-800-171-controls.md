# NIST SP 800-171 Rev 2 Controls Reference

This document lists all 110 security requirements from NIST SP 800-171 Rev 2 organized by the 14 families, with associated assessment objectives from NIST SP 800-171A.

## Family: 3.1 Access Control (AC) - 22 Requirements

### 3.1.1 Limit system access to authorized users
**Assessment Objectives:**
- [a] Authorized users are identified
- [b] Processes acting on behalf of authorized users are identified
- [c] Devices (including other systems) authorized to connect to the system are identified
- [d] System access is limited to authorized users
- [e] System access is limited to processes acting on behalf of authorized users
- [f] System access is limited to authorized devices

**Methods:** Examine (policy, procedures, access control lists), Interview (system admins), Test (attempt unauthorized access)

### 3.1.2 Limit system access to transaction and function types
**Assessment Objectives:**
- [a] The types of transactions and functions that authorized users are permitted to execute are defined
- [b] System access is limited to the defined transaction and function types for authorized users

**Methods:** Examine (authorization policies, system configurations), Interview (admins, users), Test (privilege verification)

### 3.1.3 Control CUI flow in accordance with approved authorizations
**Assessment Objectives:**
- [a] Approved authorizations for controlling the flow of CUI within the system are defined
- [b] Approved authorizations for controlling the flow of CUI between interconnected systems are defined
- [c] The flow of CUI is controlled in accordance with approved authorizations

**Methods:** Examine (data flow policies, system configurations), Interview (data owners), Test (data flow controls)

### 3.1.4 Separate duties of individuals
**Assessment Objectives:**
- [a] Duties of individuals requiring separation are defined
- [b] The duties of individuals are separated

**Methods:** Examine (separation of duties policy, role definitions), Interview (management), Test (role assignments)

### 3.1.5 Employ least privilege
**Assessment Objectives:**
- [a] Privileged accounts are identified
- [b] The concept of least privilege is employed, allowing only authorized accesses for users (and processes acting on behalf of users) necessary to accomplish assigned tasks

**Methods:** Examine (privilege policies, access lists), Interview (admins), Test (user privilege verification)

### 3.1.6 Use non-privileged accounts except for specific admin functions
**Assessment Objectives:**
- [a] Functions that require privileged accounts are identified
- [b] Non-privileged accounts are used when accessing non-security functions

**Methods:** Examine (privileged access policy), Interview (admins, users), Test (account usage observation)

### 3.1.7 Prevent non-privileged users from executing privileged functions
**Assessment Objectives:**
- [a] Privileged functions are defined
- [b] Non-privileged users are prevented from executing privileged functions
- [c] Capture of privileged function execution is prevented

**Methods:** Examine (authorization policies), Interview (admins), Test (privilege escalation attempts)

### 3.1.8 Limit unsuccessful logon attempts
**Assessment Objectives:**
- [a] The number of consecutive invalid logon attempts is defined
- [b] The system enforces a limit on consecutive invalid logon attempts by a user during a defined time period

**Methods:** Examine (access control policy, system configurations), Interview (admins), Test (logon attempt limits)

### 3.1.9 Provide privacy and security notices
**Assessment Objectives:**
- [a] System use notification messages or banners are displayed before granting system access
- [b] The notification message or banner states appropriate privacy and security information

**Methods:** Examine (system banners, policy), Interview (users), Test (banner display verification)

### 3.1.10 Use session lock after defined inactivity
**Assessment Objectives:**
- [a] The period of inactivity after which the system initiates a session lock is defined
- [b] The system initiates a session lock after the defined period of inactivity

**Methods:** Examine (session lock policy), Interview (users, admins), Test (session lock timing)

### 3.1.11 Terminate sessions after defined conditions
**Assessment Objectives:**
- [a] Conditions or trigger events that require session disconnect are defined
- [b] User sessions are automatically terminated after any of the defined conditions or trigger events

**Methods:** Examine (session management policy), Interview (admins), Test (session termination)

### 3.1.12 Monitor and control remote access sessions
**Assessment Objectives:**
- [a] Remote access sessions are monitored
- [b] Remote access sessions are controlled

**Methods:** Examine (remote access policy, logs), Interview (admins), Test (remote access monitoring)

### 3.1.13 Employ cryptographic mechanisms for remote access
**Assessment Objectives:**
- [a] Cryptographic mechanisms to protect the confidentiality of remote access sessions are implemented

**Methods:** Examine (remote access configuration), Interview (admins), Test (encryption verification)

### 3.1.14 Route remote access via managed access control points
**Assessment Objectives:**
- [a] Managed network access control points are identified
- [b] Remote access is routed through managed network access control points

**Methods:** Examine (network diagrams, configurations), Interview (network admins), Test (access path verification)

### 3.1.15 Authorize remote execution of privileged commands
**Assessment Objectives:**
- [a] Privileged commands authorized for remote execution are identified
- [b] Authorization mechanisms for remote execution of privileged commands are employed

**Methods:** Examine (authorization policies), Interview (admins), Test (remote privileged command execution)

### 3.1.16 Authorize wireless access prior to allowing connections
**Assessment Objectives:**
- [a] Wireless access points are identified
- [b] Wireless access to the system is authorized prior to allowing such connections

**Methods:** Examine (wireless access policy), Interview (network admins), Test (wireless authorization mechanisms)

### 3.1.17 Protect wireless access using authentication and encryption
**Assessment Objectives:**
- [a] Wireless access to the system is authenticated
- [b] Wireless access to the system is encrypted

**Methods:** Examine (wireless security configuration), Interview (network admins), Test (wireless security controls)

### 3.1.18 Control connection of mobile devices
**Assessment Objectives:**
- [a] Mobile devices that process, store, or transmit CUI are identified
- [b] Connection of mobile devices is controlled

**Methods:** Examine (mobile device policy), Interview (admins, users), Test (mobile device connection controls)

### 3.1.19 Encrypt CUI on mobile devices and mobile computing platforms
**Assessment Objectives:**
- [a] Mobile devices and mobile computing platforms that process, store, or transmit CUI are identified
- [b] Cryptographic mechanisms to protect and control information on mobile devices and mobile computing platforms are implemented

**Methods:** Examine (encryption policy, mobile device configuration), Interview (users), Test (encryption verification)

### 3.1.20 Verify and control connections to external systems
**Assessment Objectives:**
- [a] External systems that may be connected to the organizational system are identified
- [b] Connections to external systems are verified
- [c] Connections to external systems are controlled

**Methods:** Examine (external connection policy, firewall rules), Interview (admins), Test (connection controls)

### 3.1.21 Limit use of portable storage devices on external systems
**Assessment Objectives:**
- [a] Restrictions on the use of organization-controlled portable storage devices by authorized individuals on external systems are identified
- [b] Use of organization-controlled portable storage devices by authorized individuals on external systems is limited

**Methods:** Examine (portable media policy), Interview (users, admins), Test (portable storage controls)

### 3.1.22 Control CUI posted or processed on publicly accessible systems
**Assessment Objectives:**
- [a] Individuals authorized to post or process information on publicly accessible systems are identified
- [b] Procedures to ensure CUI is not posted or processed on publicly accessible systems are identified and implemented
- [c] A review process is in place prior to posting of any content to publicly accessible systems

**Methods:** Examine (public posting policy, review process), Interview (content managers), Test (posting controls)

## Family: 3.2 Awareness and Training (AT) - 3 Requirements

### 3.2.1 Ensure managers, system admins, and users are aware of security risks
**Assessment Objectives:**
- [a] Managers and systems administrators of the organizational system are made aware of the security risks associated with their activities
- [b] Users of the organizational system are made aware of the security risks associated with their activities
- [c] Managers, systems administrators, and users are made aware of applicable policies, procedures, and processes regarding the security of the system

**Methods:** Examine (training records, awareness materials), Interview (managers, admins, users), Test (awareness verification)

### 3.2.2 Ensure personnel are trained to carry out assigned information security roles
**Assessment Objectives:**
- [a] Information security-related duties, roles, and responsibilities are identified
- [b] Personnel with assigned information security roles and responsibilities are trained to carry out those roles and responsibilities before being granted access to CUI or the system

**Methods:** Examine (training policy, training records), Interview (personnel, management), Test (competency verification)

### 3.2.3 Provide security awareness training on recognizing and reporting threats
**Assessment Objectives:**
- [a] Security awareness training on recognizing and reporting potential indicators of insider threat is provided to managers and employees

**Methods:** Examine (training materials, records), Interview (employees, managers), Test (threat awareness verification)

## Family: 3.3 Audit and Accountability (AU) - 9 Requirements

### 3.3.1 Create and retain audit logs
**Assessment Objectives:**
- [a] Events to be logged are defined
- [b] The content of audit records needed for each defined event type is determined
- [c] Audit records are created (generated)
- [d] Audit records, once created, contain the defined content

**Methods:** Examine (audit policy, log configurations), Interview (admins), Test (audit record generation)

### 3.3.2 Ensure actions can be traced to individual users
**Assessment Objectives:**
- [a] The content of audit records is determined
- [b] Audit records contain the content necessary to support after-the-fact investigations of security incidents

**Methods:** Examine (audit logs), Interview (admins), Test (user action traceability)

### 3.3.3 Review and update logged events
**Assessment Objectives:**
- [a] Logged events are reviewed and updated

**Methods:** Examine (event review records, policy), Interview (management, admins), Test (review process verification)

### 3.3.4 Alert on audit failure events
**Assessment Objectives:**
- [a] Personnel or roles to be alerted in the event of an audit logging process failure are identified
- [b] An alert is generated in the event of an audit logging process failure

**Methods:** Examine (alert configuration), Interview (admins), Test (alert generation)

### 3.3.5 Correlate audit record review, analysis, and reporting
**Assessment Objectives:**
- [a] Audit records are reviewed
- [b] Audit records are analyzed
- [c] Audit record review, analysis, and reporting processes are correlated for investigation and response to indications of unlawful, unauthorized, suspicious, or unusual activity

**Methods:** Examine (SIEM configuration, analysis procedures), Interview (security team), Test (correlation processes)

### 3.3.6 Provide audit record reduction and report generation
**Assessment Objectives:**
- [a] An audit record reduction capability is provided
- [b] A report generation capability is provided

**Methods:** Examine (reporting tools, procedures), Interview (admins), Test (report generation)

### 3.3.7 Provide system capability for audit information analysis
**Assessment Objectives:**
- [a] The system provides a capability to process audit records for events of interest based on defined criteria

**Methods:** Examine (SIEM capabilities, queries), Interview (security analysts), Test (audit analysis)

### 3.3.8 Protect audit information and tools
**Assessment Objectives:**
- [a] Audit information is protected from unauthorized access
- [b] Audit information is protected from unauthorized modification
- [c] Audit information is protected from unauthorized deletion
- [d] Audit tools are protected from unauthorized access, modification, and deletion

**Methods:** Examine (access controls on logs), Interview (admins), Test (audit protection mechanisms)

### 3.3.9 Limit management of audit functionality to privileged users
**Assessment Objectives:**
- [a] A subset of privileged users is identified
- [b] Management of audit functionality is limited to the identified subset of privileged users

**Methods:** Examine (access policies, RBAC configuration), Interview (admins), Test (audit management access)

## Family: 3.4 Configuration Management (CM) - 9 Requirements

### 3.4.1 Establish and maintain baseline configurations
**Assessment Objectives:**
- [a] Baseline configurations are developed and documented for the system
- [b] Baseline configurations include software, firmware, and hardware components
- [c] Baseline configurations are maintained

**Methods:** Examine (baseline documentation, CM tools), Interview (admins), Test (baseline compliance)

### 3.4.2 Establish and enforce security configuration settings
**Assessment Objectives:**
- [a] Security configuration settings are established for IT products employed in the system
- [b] Security configuration settings are enforced

**Methods:** Examine (configuration standards, system configurations), Interview (admins), Test (configuration enforcement)

### 3.4.3 Track, review, approve/disapprove, and log changes
**Assessment Objectives:**
- [a] Changes to the system are tracked
- [b] Changes to the system are reviewed
- [c] Changes to the system are approved or disapproved with explicit consideration for security impact analysis
- [d] Changes to the system are logged

**Methods:** Examine (change logs, change management procedures), Interview (change board), Test (change process)

### 3.4.4 Analyze security impact of changes prior to implementation
**Assessment Objectives:**
- [a] Security impact analyses of proposed changes to the system are conducted prior to change implementation

**Methods:** Examine (security impact analysis documentation), Interview (change managers), Test (analysis process)

### 3.4.5 Define, document, approve, and enforce access restrictions
**Assessment Objectives:**
- [a] Physical and logical access restrictions associated with changes to the system are defined
- [b] Physical and logical access restrictions associated with changes to the system are documented
- [c] Physical and logical access restrictions associated with changes to the system are approved
- [d] Physical and logical access restrictions associated with changes to the system are enforced

**Methods:** Examine (access restriction policies), Interview (admins), Test (access control enforcement)

### 3.4.6 Employ least functionality principle
**Assessment Objectives:**
- [a] Essential capabilities for the system are identified
- [b] The system is configured to provide only essential capabilities
- [c] Prohibited or restricted functions, ports, protocols, and services are identified
- [d] The use of prohibited or restricted functions, ports, protocols, and services is prevented or restricted

**Methods:** Examine (system configuration, ports/services documentation), Interview (admins), Test (functionality restrictions)

### 3.4.7 Restrict, disable, or prevent software program execution
**Assessment Objectives:**
- [a] User-installed software is identified
- [b] The execution of user-installed software is restricted, disabled, or prevented based on one or more of the following: software program usage and restrictions, software program rules, or rules authorizing software program terms and conditions

**Methods:** Examine (application control policies), Interview (admins, users), Test (software execution controls)

### 3.4.8 Apply deny-by-exception (blacklist) or allow-by-exception (whitelist) policy
**Assessment Objectives:**
- [a] A deny-by-exception policy to prohibit the execution of unauthorized software programs is identified and employed, OR
- [b] An allow-by-exception policy to authorize the execution of authorized software programs is identified and employed

**Methods:** Examine (application control configuration), Interview (admins), Test (policy enforcement)

### 3.4.9 Control and monitor user-installed software
**Assessment Objectives:**
- [a] User-installed software is controlled
- [b] User-installed software is monitored

**Methods:** Examine (software inventory, monitoring tools), Interview (admins), Test (control mechanisms)

## Family: 3.5 Identification and Authentication (IA) - 11 Requirements

### 3.5.1 Identify users, processes, and devices
**Assessment Objectives:**
- [a] System users are identified
- [b] Processes acting on behalf of users are identified
- [c] Devices accessing the system are identified

**Methods:** Examine (user accounts, device inventory), Interview (admins), Test (identification mechanisms)

### 3.5.2 Authenticate users, processes, and devices
**Assessment Objectives:**
- [a] System users are authenticated
- [b] Processes acting on behalf of users are authenticated
- [c] Devices accessing the system are authenticated

**Methods:** Examine (authentication configuration), Interview (admins, users), Test (authentication mechanisms)

### 3.5.3 Use multifactor authentication
**Assessment Objectives:**
- [a] Multifactor authentication is implemented for local access to privileged accounts
- [b] Multifactor authentication is implemented for local access to non-privileged accounts
- [c] Multifactor authentication is implemented for network access to privileged accounts
- [d] Multifactor authentication is implemented for network access to non-privileged accounts

**Methods:** Examine (MFA configuration), Interview (users, admins), Test (MFA enforcement)

### 3.5.4 Replay-resistant authentication mechanisms
**Assessment Objectives:**
- [a] Replay-resistant authentication mechanisms are employed

**Methods:** Examine (authentication protocols), Interview (security engineers), Test (replay attack resistance)

### 3.5.5 Prevent reuse of identifiers
**Assessment Objectives:**
- [a] Previously used individual, group, role, or device identifiers are prevented from being reused for a defined time period

**Methods:** Examine (identifier management policy), Interview (admins), Test (identifier reuse prevention)

### 3.5.6 Disable identifiers after defined period of inactivity
**Assessment Objectives:**
- [a] A time period of inactivity after which an identifier is disabled is defined
- [b] Identifiers are disabled after the defined time period of inactivity

**Methods:** Examine (account management policy, configurations), Interview (admins), Test (inactive account handling)

### 3.5.7 Enforce minimum password complexity
**Assessment Objectives:**
- [a] Minimum password complexity requirements are defined
- [b] Password complexity requirements are enforced

**Methods:** Examine (password policy), Interview (admins, users), Test (password complexity enforcement)

### 3.5.8 Prohibit password reuse
**Assessment Objectives:**
- [a] The number of generations during which a password cannot be reused is defined
- [b] Password reuse is prohibited for the defined number of generations

**Methods:** Examine (password policy, system configuration), Interview (admins), Test (password history enforcement)

### 3.5.9 Allow temporary password use for system logons only
**Assessment Objectives:**
- [a] Temporary passwords are allowed for system logons
- [b] Temporary passwords are restricted to immediate change upon first use

**Methods:** Examine (password procedures), Interview (admins, users), Test (temporary password workflow)

### 3.5.10 Store and transmit only cryptographically protected passwords
**Assessment Objectives:**
- [a] Passwords are cryptographically protected in storage
- [b] Passwords are cryptographically protected in transit

**Methods:** Examine (password storage mechanisms, transmission protocols), Interview (developers, admins), Test (password protection)

### 3.5.11 Obscure feedback of authentication information
**Assessment Objectives:**
- [a] Feedback of authentication information is obscured during the authentication process

**Methods:** Examine (authentication interface), Interview (users), Test (authentication feedback obscuration)

## Family: 3.6 Incident Response (IR) - 3 Requirements

### 3.6.1 Establish incident handling capability
**Assessment Objectives:**
- [a] An operational incident handling capability is established for organizational systems
- [b] The incident handling capability includes preparation, detection and analysis, containment, eradication, and recovery

**Methods:** Examine (incident response plan, procedures), Interview (IR team), Test (IR capability)

### 3.6.2 Track, document, and report incidents
**Assessment Objectives:**
- [a] Incidents are tracked
- [b] Incidents are documented
- [c] Incidents are reported to appropriate officials and authorities

**Methods:** Examine (incident tracking system, reports), Interview (IR team), Test (incident reporting process)

### 3.6.3 Test incident response capability
**Assessment Objectives:**
- [a] The incident response capability is tested

**Methods:** Examine (test plans, test results), Interview (IR team, management), Test (observe IR exercise)

## Family: 3.7 Maintenance (MA) - 6 Requirements

### 3.7.1 Perform maintenance with authorized personnel
**Assessment Objectives:**
- [a] Types of system maintenance personnel are identified
- [b] System maintenance is performed by authorized personnel
- [c] Types of maintenance activities for the system are identified and defined
- [d] System maintenance activities are performed by authorized personnel

**Methods:** Examine (maintenance policy, maintenance records), Interview (maintenance personnel), Test (authorization verification)

### 3.7.2 Ensure equipment is sanitized or destroyed per policy
**Assessment Objectives:**
- [a] Media sanitization and disposal policy is established
- [b] Equipment removed for off-site maintenance is sanitized of any CUI
- [c] Equipment is removed from organizational facilities for off-site maintenance only after required approvals are obtained
- [d] Equipment containing CUI is destroyed in accordance with the media sanitization and disposal policy

**Methods:** Examine (sanitization procedures, destruction records), Interview (IT staff), Test (sanitization process)

### 3.7.3 Ensure equipment maintenance and repairs are performed by authorized personnel
**Assessment Objectives:**
- [a] Maintenance tools used for equipment maintenance are inspected
- [b] Equipment maintenance and repairs are performed by authorized and qualified personnel

**Methods:** Examine (maintenance records, certifications), Interview (maintenance personnel), Test (qualification verification)

### 3.7.4 Require multifactor authentication for remote maintenance
**Assessment Objectives:**
- [a] Multifactor authentication is employed to establish nonlocal maintenance and diagnostic sessions via external network connections

**Methods:** Examine (remote maintenance procedures, MFA configuration), Interview (admins), Test (MFA enforcement for remote maintenance)

### 3.7.5 Supervise maintenance personnel without required access
**Assessment Objectives:**
- [a] Personnel who do not have the required access authorizations are identified
- [b] Maintenance personnel who do not have the required access authorizations are supervised during the performance of maintenance activities by approved personnel who are fully cleared, have the appropriate access authorizations, and are technically qualified
- [c] Maintenance activities performed by personnel who do not have the required access authorizations are reviewed

**Methods:** Examine (supervision procedures, access logs), Interview (supervisors), Test (supervision process)

### 3.7.6 Sanitize equipment with CUI before removal
**Assessment Objectives:**
- [a] Equipment containing CUI is sanitized prior to removal from organizational facilities for off-site maintenance or repairs
- [b] CUI is removed from equipment prior to removal from organizational facilities for off-site maintenance or repairs

**Methods:** Examine (sanitization procedures, maintenance logs), Interview (IT staff), Test (sanitization verification)

## Family: 3.8 Media Protection (MP) - 9 Requirements

### 3.8.1 Protect system media containing CUI
**Assessment Objectives:**
- [a] Media containing CUI is identified
- [b] Media containing CUI is protected

**Methods:** Examine (media protection policy, physical controls), Interview (personnel), Test (protection mechanisms)

### 3.8.2 Limit access to CUI on system media to authorized users
**Assessment Objectives:**
- [a] The type of media requiring restricted access is identified
- [b] Access to CUI on identified system media is limited to authorized users

**Methods:** Examine (access control policy, media handling procedures), Interview (users, admins), Test (access restrictions)

### 3.8.3 Sanitize or destroy media before disposal or reuse
**Assessment Objectives:**
- [a] Media to be sanitized or destroyed is identified
- [b] Media is sanitized using approved equipment, techniques, and procedures prior to disposal or release for reuse

**Methods:** Examine (sanitization procedures, destruction records), Interview (IT personnel), Test (sanitization effectiveness)

### 3.8.4 Mark media with CUI handling markings
**Assessment Objectives:**
- [a] System media containing CUI is identified
- [b] System media containing CUI is marked to indicate the distribution limitations, handling caveats, and applicable security markings (if any)

**Methods:** Examine (marking policy, labeled media), Interview (personnel), Test (marking compliance)

### 3.8.5 Control access to media containing CUI and maintain accountability
**Assessment Objectives:**
- [a] System media is identified
- [b] Access to system media containing CUI is controlled
- [c] Accountability for system media containing CUI is maintained

**Methods:** Examine (media accountability records, check-out logs), Interview (media custodians), Test (accountability procedures)

### 3.8.6 Implement cryptographic mechanisms to protect CUI stored on digital media
**Assessment Objectives:**
- [a] Digital media requiring encryption is identified
- [b] Cryptographic mechanisms are implemented to protect the confidentiality of CUI stored on digital media during transport outside of controlled areas

**Methods:** Examine (encryption policy, media configurations), Interview (IT staff), Test (encryption verification)

### 3.8.7 Control use of removable media on system components
**Assessment Objectives:**
- [a] Types of removable media are identified
- [b] Individuals authorized to use removable media types are identified
- [c] The use of removable media is controlled
- [d] The use of removable media on system components is restricted

**Methods:** Examine (removable media policy, usage logs), Interview (users, admins), Test (usage controls)

### 3.8.8 Prohibit use of portable storage devices when no controls are in place
**Assessment Objectives:**
- [a] Portable storage devices are identified
- [b] The use of portable storage devices is prohibited when such devices have no identifiable owner and when the security controls to protect the confidentiality of CUI cannot be identified

**Methods:** Examine (portable storage policy), Interview (users, security staff), Test (enforcement mechanisms)

### 3.8.9 Protect CUI backups in storage and transit
**Assessment Objectives:**
- [a] The confidentiality of backup CUI at storage locations is protected

**Methods:** Examine (backup procedures, encryption configuration), Interview (backup admins), Test (backup protection)

## Family: 3.9 Personnel Security (PS) - 2 Requirements

### 3.9.1 Screen individuals prior to authorizing access
**Assessment Objectives:**
- [a] Conditions for system access are identified
- [b] Individuals are screened prior to authorizing access to the system containing CUI
- [c] Individuals are rescreened in accordance with the defined conditions requiring rescreening

**Methods:** Examine (screening policy, background check records), Interview (HR, management), Test (screening process)

### 3.9.2 Ensure CUI access is protected during and after personnel actions
**Assessment Objectives:**
- [a] Personnel actions requiring review and confirmation for assignments or transfers with respect to access to CUI are identified
- [b] Access to CUI is protected during personnel actions such as terminations and transfers

**Methods:** Examine (termination procedures, access logs), Interview (HR, IT), Test (access revocation process)

## Family: 3.10 Physical Protection (PE) - 6 Requirements

### 3.10.1 Limit physical access to facilities and support infrastructure
**Assessment Objectives:**
- [a] Physical access authorizations are managed by designated officials
- [b] Physical access to organizational facilities containing CUI systems is limited to authorized individuals
- [c] Physical access to organizational systems containing CUI is limited to authorized individuals

**Methods:** Examine (access control policy, badge records), Interview (security personnel), Test (physical access controls)

### 3.10.2 Protect and monitor physical facility and support infrastructure
**Assessment Objectives:**
- [a] Physical access to facilities where organizational systems reside is monitored
- [b] Physical access to facilities where organizational systems reside is controlled

**Methods:** Examine (monitoring systems, logs), Interview (facility managers), Test (monitoring capabilities)

### 3.10.3 Escort visitors and monitor visitor activity
**Assessment Objectives:**
- [a] Visitors are escorted
- [b] Visitor activity is monitored

**Methods:** Examine (visitor logs, escort procedures), Interview (security personnel), Test (visitor management process)

### 3.10.4 Maintain audit logs of physical access
**Assessment Objectives:**
- [a] Audit logs of physical access are maintained for facilities where organizational systems reside
- [b] Audit logs of physical access are reviewed

**Methods:** Examine (physical access logs, review records), Interview (security staff), Test (log review process)

### 3.10.5 Control and manage physical access devices
**Assessment Objectives:**
- [a] Physical access devices to organizational facilities where systems reside are managed (inventoried)
- [b] Physical access devices to organizational facilities where systems reside are controlled

**Methods:** Examine (device inventory, management procedures), Interview (security managers), Test (device management)

### 3.10.6 Enforce safeguarding measures for CUI at alternate work sites
**Assessment Objectives:**
- [a] Alternate work sites for personnel with access to CUI are identified
- [b] Safeguarding measures are determined for identified alternate work sites
- [c] The determined safeguarding measures are enforced at alternate work sites

**Methods:** Examine (telework policy, security procedures), Interview (remote workers, managers), Test (safeguarding enforcement)

## Family: 3.11 Risk Assessment (RA) - 6 Requirements

### 3.11.1 Periodically assess risk
**Assessment Objectives:**
- [a] The frequency for conducting risk assessments is defined
- [b] Risk assessments of the system and the environment of operation are conducted at the defined frequency to identify risks
- [c] The risks identified through the risk assessment process are documented

**Methods:** Examine (risk assessment reports, methodology), Interview (risk managers), Test (risk assessment process)

### 3.11.2 Scan for vulnerabilities and identify unauthorized components
**Assessment Objectives:**
- [a] The frequency for vulnerability scanning is defined
- [b] Vulnerability scans are conducted at the defined frequency
- [c] Vulnerability scans are conducted when new vulnerabilities potentially affecting the system are identified and reported
- [d] Vulnerability scanning tools and techniques are employed to facilitate interoperability among tools
- [e] Vulnerability scanning tools and techniques are employed to automate parts of the vulnerability management process
- [f] Vulnerability scanning includes scanning for unauthorized components within the system

**Methods:** Examine (scan reports, scan schedule), Interview (security team), Test (vulnerability scanning process)

### 3.11.3 Remediate vulnerabilities
**Assessment Objectives:**
- [a] Vulnerabilities identified through the risk assessment process are remediated in accordance with organizational assessment of risk

**Methods:** Examine (remediation records, patch management), Interview (IT staff), Test (remediation process)

### 3.11.4 Update threat profile as threats evolve
**Assessment Objectives:**
- [a] A threat profile is developed based on threat intelligence
- [b] The threat profile is updated based on threat intelligence

**Methods:** Examine (threat profile, intelligence sources), Interview (threat analysts), Test (update process)

### 3.11.5 Conduct awareness activities about emerging threats
**Assessment Objectives:**
- [a] Awareness activities are conducted to communicate emerging threats and vulnerabilities to organizational personnel

**Methods:** Examine (threat bulletins, training materials), Interview (security awareness staff), Test (dissemination process)

### 3.11.6 Employ automated mechanisms for risk assessments
**Assessment Objectives:**
- [a] Automated mechanisms are employed to more thoroughly and effectively analyze risk

**Methods:** Examine (automated tools configuration), Interview (security analysts), Test (automated analysis capabilities)

## Family: 3.12 Security Assessment (CA) - 3 Requirements

### 3.12.1 Assess security controls periodically
**Assessment Objectives:**
- [a] The frequency for conducting security control assessments is defined
- [b] Security controls are assessed at the defined frequency to determine the extent to which the controls are implemented correctly, operating as intended, and producing the desired outcome with respect to meeting the security requirements for the system

**Methods:** Examine (assessment reports, assessment plan), Interview (assessors), Test (assessment procedures)

### 3.12.2 Create and implement plans of action to remediate deficiencies
**Assessment Objectives:**
- [a] Plans of action are developed that describe how identified weaknesses or deficiencies in security controls will be remediated
- [b] Plans of action are implemented

**Methods:** Examine (POA&M, remediation status), Interview (system owners), Test (remediation tracking)

### 3.12.3 Monitor security controls to ensure ongoing effectiveness
**Assessment Objectives:**
- [a] Security controls are monitored on an ongoing basis to ensure the continued effectiveness of the controls

**Methods:** Examine (monitoring procedures, reports), Interview (security team), Test (monitoring capabilities)

## Family: 3.13 System and Communications Protection (SC) - 16 Requirements

### 3.13.1 Monitor, control, and protect communications at system boundaries
**Assessment Objectives:**
- [a] System boundary protection mechanisms are identified
- [b] Communications are monitored at managed interfaces
- [c] Communications are controlled at managed interfaces
- [d] Communications are protected at managed interfaces

**Methods:** Examine (network diagrams, firewall rules), Interview (network engineers), Test (boundary protection)

### 3.13.2 Employ architectural designs, software development, and systems engineering to reduce risk
**Assessment Objectives:**
- [a] Security engineering principles are employed in the specification, design, development, implementation, and modification of the system

**Methods:** Examine (design documentation, security requirements), Interview (architects, developers), Test (design analysis)

### 3.13.3 Separate user and system administrator functionality
**Assessment Objectives:**
- [a] User functionality is separated from system management functionality

**Methods:** Examine (system architecture, interface designs), Interview (admins, users), Test (functionality separation)

### 3.13.4 Prevent unauthorized information transfer via shared resources
**Assessment Objectives:**
- [a] Shared system resources are identified
- [b] Unauthorized information transfer via shared system resources is prevented

**Methods:** Examine (resource isolation mechanisms), Interview (system engineers), Test (information flow controls)

### 3.13.5 Implement subnetworks for publicly accessible components
**Assessment Objectives:**
- [a] Publicly accessible system components are identified
- [b] Subnetworks (physically or logically separated) for publicly accessible system components are implemented

**Methods:** Examine (network architecture, DMZ configuration), Interview (network admins), Test (network segmentation)

### 3.13.6 Deny network communications traffic by default and allow by exception
**Assessment Objectives:**
- [a] Network communications traffic is denied by default
- [b] Network communications traffic is allowed by exception (at managed interfaces)

**Methods:** Examine (firewall policies, default-deny rules), Interview (network engineers), Test (traffic filtering)

### 3.13.7 Prevent remote devices from simultaneous connections to multiple networks
**Assessment Objectives:**
- [a] Remote devices simultaneously connecting to the system and to other (external) networks are prevented from doing so

**Methods:** Examine (VPN configuration, split-tunneling controls), Interview (network admins), Test (connection restrictions)

### 3.13.8 Implement cryptographic mechanisms to prevent unauthorized disclosure during transmission
**Assessment Objectives:**
- [a] Cryptographic mechanisms are implemented to prevent unauthorized disclosure of CUI during transmission unless otherwise protected by alternative physical safeguards

**Methods:** Examine (encryption configuration, TLS settings), Interview (security engineers), Test (transmission encryption)

### 3.13.9 Terminate network connections at end of sessions
**Assessment Objectives:**
- [a] Network connections associated with communications sessions are terminated at the end of the sessions
- [b] Network connections associated with communications sessions are terminated after a defined period of inactivity

**Methods:** Examine (session management configuration), Interview (admins), Test (connection termination)

### 3.13.10 Establish and manage cryptographic keys
**Assessment Objectives:**
- [a] Cryptographic keys are established using organization-defined key generation, distribution, storage, access, and destruction requirements in accordance with applicable federal laws, Executive Orders, directives, regulations, policies, standards, and guidance
- [b] Cryptographic keys are managed using organization-defined key generation, distribution, storage, access, and destruction requirements in accordance with applicable federal laws, Executive Orders, directives, regulations, policies, standards, and guidance

**Methods:** Examine (key management procedures, KMS configuration), Interview (cryptographic officers), Test (key lifecycle)

### 3.13.11 Employ FIPS-validated cryptography
**Assessment Objectives:**
- [a] FIPS-validated cryptography is employed to protect the confidentiality of CUI

**Methods:** Examine (cryptographic module certificates), Interview (security engineers), Test (FIPS validation verification)

### 3.13.12 Prohibit remote activation of collaboration devices
**Assessment Objectives:**
- [a] Collaborative computing devices are identified
- [b] Remote activation of collaborative computing devices is prohibited, with explicit indication of use to users physically present at the devices

**Methods:** Examine (device configurations, collaboration tool settings), Interview (users, IT staff), Test (remote activation controls)

### 3.13.13 Control and monitor use of mobile code
**Assessment Objectives:**
- [a] Acceptable and unacceptable mobile code and mobile code technologies are identified
- [b] Use of mobile code is controlled
- [c] Use of mobile code is monitored

**Methods:** Examine (mobile code policy, web filtering), Interview (security team), Test (mobile code controls)

### 3.13.14 Control and monitor use of Voice over IP
**Assessment Objectives:**
- [a] Use of Voice over Internet Protocol (VoIP) technologies is controlled
- [b] Use of Voice over Internet Protocol (VoIP) technologies is monitored

**Methods:** Examine (VoIP security configuration), Interview (telecom admins), Test (VoIP controls)

### 3.13.15 Protect authenticity of communications sessions
**Assessment Objectives:**
- [a] The authenticity of communications sessions is protected

**Methods:** Examine (session authentication mechanisms), Interview (network engineers), Test (session authenticity verification)

### 3.13.16 Protect confidentiality of CUI at rest
**Assessment Objectives:**
- [a] The confidentiality of CUI at rest is protected

**Methods:** Examine (encryption at rest configuration, access controls), Interview (admins, data owners), Test (data protection verification)

## Family: 3.14 System and Information Integrity (SI) - 13 Requirements

### 3.14.1 Identify, report, and correct system flaws timely
**Assessment Objectives:**
- [a] System flaws are identified in a timely manner
- [b] System flaws are reported in a timely manner
- [c] System flaws are corrected in a timely manner

**Methods:** Examine (flaw remediation procedures, patch records), Interview (IT staff), Test (flaw handling process)

### 3.14.2 Provide protection from malicious code
**Assessment Objectives:**
- [a] Malicious code protection mechanisms are implemented at system entry and exit points
- [b] Malicious code protection mechanisms are updated whenever new releases are available
- [c] Malicious code protection mechanisms are configured to perform periodic scans and real-time scans of files from external sources at endpoints and network entry/exit points

**Methods:** Examine (antivirus configuration, update logs), Interview (admins), Test (malware protection)

### 3.14.3 Monitor system security alerts and advisories
**Assessment Objectives:**
- [a] System security alerts and advisories are monitored on an ongoing basis
- [b] Appropriate response actions are taken as a result of security alerts and advisories

**Methods:** Examine (alert monitoring procedures, response records), Interview (security team), Test (alert response process)

### 3.14.4 Update malicious code protection mechanisms
**Assessment Objectives:**
- [a] The system is updated with the latest malicious code protection mechanisms when new releases are available

**Methods:** Examine (update schedule, version information), Interview (admins), Test (update process)

### 3.14.5 Perform periodic scans and real-time scans
**Assessment Objectives:**
- [a] The system is scanned for malicious code at defined frequencies
- [b] Real-time scans of files from external sources are performed as the files are downloaded, opened, or executed

**Methods:** Examine (scan configuration, scan logs), Interview (admins), Test (scanning operations)

### 3.14.6 Monitor systems including network and user activities
**Assessment Objectives:**
- [a] The system is monitored to detect attacks and indicators of potential attacks
- [b] Unauthorized local, network, and remote connections are detected

**Methods:** Examine (monitoring tools, IDS/IPS configuration), Interview (security analysts), Test (detection capabilities)

### 3.14.7 Identify unauthorized use
**Assessment Objectives:**
- [a] Unauthorized use of the system is identified

**Methods:** Examine (usage monitoring logs, anomaly detection), Interview (security team), Test (unauthorized use detection)

### 3.14.8 Send alert messages to designated personnel
**Assessment Objectives:**
- [a] Alert messages are sent to designated personnel when indications of compromise or potential compromise occur

**Methods:** Examine (alerting configuration, notification records), Interview (incident responders), Test (alert delivery)

### 3.14.9 Identify unauthorized system components
**Assessment Objectives:**
- [a] Unauthorized hardware is identified
- [b] Unauthorized software is identified
- [c] Unauthorized firmware is identified
- [d] Appropriate actions are taken when unauthorized components are detected

**Methods:** Examine (asset inventory, discovery tools), Interview (admins), Test (unauthorized component detection)

### 3.14.10 Check file integrity with validation tools
**Assessment Objectives:**
- [a] Information and software integrity verification tools are employed to detect unauthorized changes to software and information

**Methods:** Examine (file integrity monitoring configuration), Interview (admins), Test (integrity checking)

### 3.14.11 Manage spam to protect system availability
**Assessment Objectives:**
- [a] Spam protection mechanisms are employed at system entry points

**Methods:** Examine (email filtering configuration), Interview (email admins), Test (spam filtering)

### 3.14.12 Monitor network communications for anomalous or prohibited content
**Assessment Objectives:**
- [a] Inbound communications traffic is monitored for unusual or unauthorized activities or conditions
- [b] Outbound communications traffic is monitored for unusual or unauthorized activities or conditions
- [c] Appropriate action is taken when unusual or unauthorized activities or conditions are detected

**Methods:** Examine (network monitoring tools, DLP configuration), Interview (security analysts), Test (traffic monitoring)

### 3.14.13 Control and monitor connections from information system components
**Assessment Objectives:**
- [a] Connections from components of the system to other systems are controlled and monitored

**Methods:** Examine (connection policies, monitoring logs), Interview (network engineers), Test (connection controls)
