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

   * AD Connector 
     * Redirects directory request to on-premise Active Directory 
     * Best choice when you want to use an existing Active Directory with AWS services
     * Small size - designed for organization up to 500 users
     * Large size - designed for organization up to 5000 users
     * Requires a VPN or Direct Connect connection
     * Join EC2 instances to your on-premise AD through AD connector
     * Login to the AWS Management Console using your on-premise Ad DCs for authentication

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
* 