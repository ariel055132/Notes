# Security in the Cloud
* How to secure resource in AWS Cloud


## AWS Directory Service
* Implement a directory on AWS / Connect an existing directory service into AWS
1. AWS Managed Microsoft Active Directory (AD)
   * Deploy a pair of High Availability of Windows Server Domain Controllers (DCs) in AWS Cloud
   * Connect the Microsoft Active Directory (ADs) to Domain Controllers.
     * Use the same directory from windows in AWS

   * Fully managed AWS service
   * Best choice if you have more than 5000 users / need a trust relationship set up
   * Can perform schema extensions
   * Can setup trust relationships to with on-premises Active Directories:
     * On-premise users and groups can access resources in either domain using SSO
     * Requires a VPN or Direct Connect connection
   * Can be used as standalone AD in the AWS cloud
   * Source: source/Security/

   * AD Connector 
     * Redirects directory request to on-premise Active Directory 
     * Best choice when you want to use an existing Active Directory with AWS services
     * Small size - designed for organization up to 500 users
     * Large size - designed for organization up to 5000 users
     * Requires a VPN or Direct Connect connection
     * Join EC2 instances to your on-premise AD through AD connector
     * Login to the AWS Management Console using your on-premise Ad DCs for authentication
     * Source: source/Security/AD_Connector.png

   * Simple AD 
     * Inexpensive Active Directory-Compatible service with common directory features
     * Standalone, fully managed, directory on the AWS cloud
     * Simple AD is generally the least expensive option
     * Best choice for less than 5000 users and do not need advanced AD features
     * Feature include:
       * Manage user accounts / groups
       * Apply group policies
       * Kerberos-based SSO 
       * Supports joining Linux or Windows based EC2 instances

## Identity providers and federation
* Ways to federate to AWS
* Take our identity source (on premises Active Directory) and link it with AWS (authentication & authorization), able to access other systems without having to re-authenticate
  * identity: one username and password, one location where the users is stored

### SAML Identity Federation
1. Users log in to Active Directory, put their username and password in and gets sent to Active Directory (aka. LDAP Identity store) to validate that they are who they say there are.
2. The ADFS (Active Directory Federation Server) checks with Active Directory that the user is properly authenticated and sends back something called a SAML assertion.
    * SAML assertion proves that the user is who they say they are
3. The application will send the SAML assertion to the security token service (AWS STS) on AWS using an API call
    * STS: service on AWS that provides temporary security credentials
4. Users can use the temporary security credentials to access the Table

### Web Identity Federation
1. Users can authenticate with social IDPs inside the application (e.g Amazon, Google, Faccebook)
2. The application will make a call to the AWS Security Token Service (STS)
3. AWS STS will return a temporary security credentials to application for further access.
* Ref: source/Security/IAM_Web_IdentityFederation.png

### IAM Identity Center 
* Successor to AWS Single Sign-On (SSO)
* *Enables centralized permissions management and SSO (Single Sign on)*
  * SSO: Able to access to multiple systems through one username and password
* Identity sources can be Identity Center directory, Active directory, standard providers using SAML 2.0
* Integration with organizations -> access to data sources with the accounts in the organization
* Also can add additional AWS accounts
* Ref: source/Security/IAM_IdentityCenter.png

### Amazon Cognito
* used for adding *sign-in and sign-up functionality* to *web and mobile applications*
* *User Pools*: Store the user identities, federated to an identity source
* *Identity Pools*: Getting temporary, limited-privilege credentials for AWS services


* Ref: source/Security/Amazon_Cognito.png (Use Cases / Examples)

### Encryption Primer
* For KMS keys and Cloud HSM and certificates using AWS Certificate Manager
1. *Encryption in Transit*
   * Encrypting data as it traverse the network （傳輸資料的時候有加密 / 使用加密通道進行資料傳送）
   * The data will be decrypted when it reaches the destination 
   * E.G: SSL certificate
2. *Encryption at rest*
   * The actual data itself, not just the channel over the network  (資料先進行加密，然後再傳送)
* *Asymmetric Encryption*
  * Public key cryptography
  * Message encrypted with the public key can only be decrypted with the private key
  * Message encrypted with the private key can only be decrypted with the public key
  * In general, we will have the public key, and we can *encrypted the data with public key*. However, the person who has the *private key is able to decrypt the data*
* *Symmetric Encryption*
  * Use the *same key* for both encryption and decryption

## AWS Key Management Service (KMS)
* Used to create and manage *symmetric* and *asymmetric* encryption keys (aka. KMS keys)
* The *KMS keys* are protected by hardware security modules (HSMs), primary resources in AWS KMS
* Used to be known as "customer master keys" or CMKs
* the keys contain the *key material* used to encrypt and decrypt data
  * *Encryption at rest*
* User can import their own key material
* An Original KMS Keys can encrypted data up to *4KB* in size
* For larger files, need to generate, encrypt, and decrypt with *Data Encryption Keys (DEKs)*

### Types of Keys
1. Customer Managed Keys
   * Generated by users
2. AWS Managed Keys
   * *Created, managed, and used on your behalf by an AWS service* that is *integrated with AWS KMS*
   * Cannot manage these keys, rotate them, or change their key policies
   * Cannot use them in cryptographic operation directly; Only the AWS services that create these key can use them 

### Alternative Key Stores
1. External Key Stores (XKS)
   * Keys can be *stored outside of AWS* to meet regulatory requirements
   * Create a KMS key in AWS KMS external key stores
   * All keys are generated and stored in an external key manager
   * When using an XKS, key material never leaves HSM
2. Custom Key Stores
   * Create KMS Keys in an AWS CloudHSM custom key stores
   * All keys are generated and stored in an AWS CloudHSM cluster that you own and manage
   * Cryptographic operation are performed solely in the AWS CloudHSM cluster you own and manage
   * Therefore, customer key store are not available for asymmetric KMS keys

### Data Encryption Keys (DEKs)
* RECALL: An Original KMS Keys can encrypted data up to *4KB* in size
* Use data keys if you need to encrypt large amounts of data
* You can use *AWS KMS to generate, encrypt, and decrypt data keys*
* AWS KMS does not store, manage, or track data keys, or perform cryptographic operations with data keys (KMS 不會自行使用 data keys 進行密碼操作而已，使用者透過 KMS 執行相關操作)
* Users must *use and manage data keys outside of AWS KMS*

### KMS Keys and Automatic Rotation
* Ref: source/Security/KMS_Keys_Rotation.png
1. Automatic key rotation is supported only on *symmetric encryption (Use the same key material for encryption / decryption)* KMS keys with key material that AWS KMS generates (*Origin = AWS_KMS*)
2. *Automatic Rotation generates new material every year* (for AWS managed key & AWS own key, optional for customer managed keys)
3. The *properties of the KMS keys do not change* when the key is rotated, only *changes the key material* used for encryption
   * Properties: Key ID, *Key ARN(?)*, Region, Policies, permissions... 
   * Users do not need to change application refer to the Key ID / key ARN of the KMS key
4. If user enables key rotation, AWS KMS *rotates the KMS key (material) automatically every year (365 days)*
5. Automatic key rotation not supported, *do it manually*:
   * Asymmetric KMS keys
   * HMAC KMS keys
   * KMS keys in custom key stores
   * KMS keys with imported key material
* AWS owned key
  * The key that out of user control
  * not only used for one user account, general usage

### Manual Rotation
* Creating a new KMS key with a different key ID
* Users must update the applications with the new Key ID
* Can use *alias* to represent a KMS key so no need to modify application code
  * In application, use alias to refer to the keys
  * When creating a new KMS key, alias refers to the new keys

### Key Policies
* Define management and usage permissions for KMS keys
* Multiple policy statements can be combined to specify separate administrative and usage permissions
* Permissions can be specified for delegating use of the key to AWS services (aka. *Grant*)
  * Using Grants for *temporary permissions* as they can be used without modifying key policies or IAM policies (~Roles in IAM)
  * To share snapshots with another accounts user must specify *Decrypt* and *CreateGrant* permissions
  * *kms:ViaService* condition key can be used to limit key usage to specific AWS services
* *Cryptographic erasure* means removing the ability to decrypt data and can be achieved when using *imported key material* and deleting that key material (*DeleteImportedKeyMaterial API*)
* An InvalidKeyId exception when using SSM Parameter Store indicates the KMS key is not enabled

## AWS Cloud HSM
* Cloud-baed hardware security module (HSM)
* Generate and use your own encryption keys on the AWS Cloud
* CloudHSM runs in your Amazon VPC
* Use FIPS 140-2 level 3 validated HSMs 
* Managed service and automatically scales
* Retain control of your encryption keys - you control access
  * (AWS has no visibility of your encryption keys)

### Use Cases
* Offload SSl/TLS processing from web servers
* Protect private keys for an issuing certificate authority (CA)
* Store the master for Oracle DB Transparent Data Encryption
* Custom key store for AWS KMS - retain control of the HSM that protects the master keys

## AWS Certificate Manager (ACM)
* Issuing SSL/TLS X.509 certificates (use for encryption in transit)
* Single domains, multiple domain names and wildcards
* Integrates with several AWS services including:
  1. Elastic Load Balancing
  2. Amazon CloudFront
  3. AWS Elastic Beanstalk
  4. AWS Nitro Enclaves
  5. AWS CloudFormation
* *Public certificates* are signed by the *AWS public Certificate Authority*
* User can also create a Private CA with ACM, then ACM can then issue private certificates
* User can import certificates from third-party issuers
* *ACM is used for encryption for transit, KSM is used for encryption at rest*

## AWS Web Application Firewall (WAF)
* Web Application firewall
* Allow users to create rules to filter web traffic based on conditions that include IP addresses, HTTP headers and body, or custom URIs 
  * ~Web ACLs (Access Control List)
* Easy to create rules that block *common web exploits* like *SQL injection* and *cross site scripting*

### Use Cases 
* Ref: source/Security/AWS_WAF_usecase.png

### Terminology
1. Web ACLs
   * Used to protect a set of AWS resources
2. Rules
   * Contains a statement that defines the inspection criteria
   * Also an action to take if a web request meets the criteria 
3. Rule Action
   * Tell AWS WAF what to do with a web request when it matches the criteria defined in the rule
   1. Count: *Count the request* but does not determine whether to block or allow t.
   2. Allow: *allow the request to be forwarded* to AWS resource for processing and response
   3. Block： *Block the request* and AWS resource responds with an HTTP *403 status code*
4. Rule Groups
   * Apply rules to groups 
   * Therefore, no need to set up rules to each user individually 
   * ~IAM user groups
5. IP Sets
   * Provides a collection of IP addresses and IP address ranges that you want to use together in a rule statement
6. Regex pattern set (?)
   * Provides a collection of regular expresions that you want to use together in a rule statement
* Match Statement
   * Ref: source/Security/AWS_WAF_MatchStatements.png 
   * Compare the web request or its origin against condition that you provide
   1. Geographic match
   2. IP set match
   3. Regex pattern set
   4. Size Constraint
   5.  

## Amazon Inspector
* Perform *network and host assessment* for EC2 services
  * Check for *security exposures and vulnerabilities* in EC2 instances
* Can be configured to run on a schedule
* Agent must be installed on EC2 for host assessments
* Network assessments do not required an agent (but agent is preferred)

### Network assessment
* Network configuration analysis to *check for ports reachable from outside the VPC* (檢查EC2 Service 開放了哪些接口)
* If the Inspector Agent is installed on your EC2 instances, the assessment also *finds processes reachable on port* (檢查哪些服務會使用已開放的 Port)
* Price based on the number of instance assessments

### Host Assessment
* *Vulnerable software* (CVE), Host hardening (CIS benchmarks), and security best practices
* *Requires an agent* (auto install with SSM Run Command)
* Price based on the number of instance assessments

## Amazon Macie
* Seldom appear in the exam question
* Use *Machine learning and pattern matching* to discover, monitor, and help you *protect sensitive data on Amazon S3* (Data security and data privacy service)

### How Macie protect data privacy?
1. Identify a variety of data types, including
   * PII (Personally Identifiable Information)
   * PHI (Protected Health Information)
   * Regulatory Documents
   * API Keys
   * Secret Keys
2. Identify changes to policy and access control lists
3. Continuously monitor the security posture of Amazon S3
4. Generate security findings that you can view using Macie console, AWS Security Hub, or Amazon EventBridge
5. Manage multiple AWS accounts using AWS Organizations

## Amazon GuardDuty
* Intelligent *threat detection service*
* Detects account compromise, instance compromise, malicious reconnaissance, and bucket compromise
* Integration
    1. AWS CloudTrail Management Events
    2. AWS CloudTrail S3 Data Events
    3. Amazon VPC Flow Logs
    4. DNS Logs

## AWS Shield
* *Protect against DDOS attacks* (Distributed denial of service attacks)
* Safeguards web application running on AWS with always-on detection and automatic inline mitigations
* Helps to minimize application downtime and latency 
* 2 Tiers
    1. Standard - No Cost (included with Amazon CloudFront) 
        * Provide network flow monitoring
        * Standardized protection and for the undelying AWS Service
    2. Advanced - 3k USD per month and 1 year commitment 

## Defense in Depth
* Refers to the practice of implementing security at multiple layers within your application and infrastructure
* So that if you do fail in your security, it will not lead to any major exposure.