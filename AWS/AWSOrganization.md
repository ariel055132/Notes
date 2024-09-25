# AWS Organization 
* It allows people to consolidate **mulitple AWS accounts** into an **organization** that **create and centrally manage**
  1. single bill in management account (aka. *consolidated billing*)
  2. *Apply centralized governance* across different AWS accounts

## Terminology
1. Management / Root / Master / Main Account
   * The account through which you create the Organization and then connects in the other accounts
2. Organizational Units (OUs)
   * A type of organizational container
   * Apply things like Service Control Policies, tag Policies
3. Consolidated Billing
   * Have a single bill in the management account
   * may be good when you get volume discount discount (~the more you use, the less you pay per unit)
   * Limit of 20 linked accounts for consolidated billing (default)
4. Paying Account (in Consolidated Billing)
   * independent and cannot access resources of other accounts
5. Linked Accounts (in Consolidated Billing)
   * all linked accounts are independent
6. Service Control Policies (SCPs)
   * control the *maximum available/enabled permissions*, not grant permission
   * must have all features enabled in Organization
   * can be applied to accounts or Organization Units (OUs)
   * affect only IAM users and roles, not resources policies
   * affect the root account in member accounts
7. Tag Policy
   * enforce tag standardization

## Migration
* Accounts can be migrated/moved between organizations
* In order to move accounts, must have root / IAM access to both the member and management accounts
* Use *AWS Organizations console* for *a few accounts*
* Use *AWS Organizations API / AWS CLI* if *many accounts* to migrate

## AWS Control Tower
* A topology to manage multiple AWS accounts

### Control Tower - Guardrails
1. Preventive Guardrails (預防性防護措施) 
   * disallow API actions using *SCPs (Service Control Policies)*, limit what action users and roles can perform in the AWS accounts within the organization
     > Disallow Deletion of CloudTrail Logs and S3 Logging Buckets
     > Disallow Public Read Access to S3 Buckets
     > Require Encryption on EBS Volumes
     > Disallow RDP / SSH Access from 0.0.0.0/0
2. Detective Guardrails
   * used for governance and compliance
   * Implemented using *AWS Config rules* and *lamdba functions*. Evaluate the configuration of AWS resources and generate alerts or reports when non-compliance is detected.
        > Detecting publicly accessible Amazon S3 buckets
        > Detect whether versioning is enabled for Amazon S3 buckets
        > Detect whether encryption is enable for Amazon RDS instances
        > Monitoring for IAM policies that grant overly broad permissions

### Control Tower - Shared Accounts
1. Management account
   * The account used to launch AWS Control Tower
2. Log archive account
3. Audit Account
   * Aggregates and stores logs collect from all other accounts in the landing zone. 
   * Secure account with restricted access.

## AWS Organizations VS Control Tower
### AWS Organization
* Manage multiple accounts
* Consolidated billing
* Organizational Units
* Service Control Policies
* Tag Policies
* Backup Policies

### AWS Control Tower
* Extends capabilities of AWS Organizations
* Landing Zone
* Federated Access (IAM Identity Center)
* Centralized Logging
* Account Factory

## Architecure Patterns
1. A company needs a method of quickly **creating AWS account programmatically**
   * Use the *Organizations API* to create the accounts programmatically
   * Notes: AWS Organization Console is good when you migrate a few accounts only. 
2. Users in a menber account in AWS Organizations should be restricted from making changes in IAM
   * Use a *Service Control Policy (SCP)* to deny access to IAM actions
3. An AWS account must be moved between Organizations
   * Migrate the account using the *AWS Organizations Console*.
4. **A solution architect created a new account through the Organizations console and needs to login to launch resources**
   * **The architect should switch roles to access the new account ??**
5. Multiple member accounts in AWS Organizations require the same permissions to be restricted using SCPs
   * Create an *Organization Unit (OU)* and add the member accounts then attach the *SCP* to the OU
6. The developers in a company each have their own AWS accounts for testing. The security team wish to enable **central governance**.
   * Create an AWS Organizations and send an invite to each developer's AWS account to join the Organization

## QA
1. Which can be used to enforce tag standardizations?
   * Tag Policy
2. AWS Organization Policies are applied to which following entities?
   * Root accounts or Organizational Units
3. Which is the main benefit of AWS Organization?
   * Consolidation of multiple AWS accounts into an organization (this)
   * Consolidated billing
   * OUs
   * Easy login for users