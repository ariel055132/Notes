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