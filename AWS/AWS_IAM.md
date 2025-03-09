# AWS Identity and Access Management (IAM)

## What is IAM?
* A place allows us to *create user*, *role*, *federated user*, make application before making a request for an action or operation on an AWS resource.

## How to use IAM?
* First, We need to login to AWS IAM via console, CLI, and API. We need to **authenticate** ourself. (Showing who we are, trying to prove who we are.)
* After login in, we can create user, role, policy......
* After that, when we are trying to make a request for an action or operations on an AWS resource. AWS determines whether to **authorize** the request (deny/allow)
* **To conclude, the user need to authenticate himself, then perform authorized operations in the console.**

## Terminology
1. Principal
   * A person/user or application that can make a request for an *action* or *operation* on an AWS resource.
   * Before send request, thet must be authenticated
2. Account Root User
   * User has full permissions, the first account created
   * Cannot restrict most 
   * Avoid using it + enable MFA (multifactor authentication)
   * Create only create 5000 individual user account at most with one root user
3. Users
   * Have **no permissions by default** 
     * Before granting the permmision through policy, AWS will deny all the requests from users
   * The users gains the *permissions* applied to the *group* through the *policy*.
   * *Friendly name* : alias of Amazon resources name (e.g: Adrian)
   * *Amazon resources name*: A unique identifier in AWS (e.g. aws:12234234235 :user/Adrian)
4. User Groups
   * A collection of users.
   * You can add multiple common users, and then applying permission policies to the same group 
   * It is easier to manage the permission for those users.
5. Roles
   * An identity which has permissions assigned to it via policy
   * For example, if you are a development role, you can take on the development permissions
   * Does not have any static credentials
   * Help to prevent accidential access to or modification of sensitive resources
6. Policies
   * defines the permissions for the identities or resources they are associated with.
   * AWS determines whether to **authorize** (allow/deny) the request by checking policies
   * For more, watch Types of policy

## Types of policy
1. Identity-based policy
   * attached to **users, groups, or roles**
2. Resource-based policy
   * attached to a **resource** 
   * define permissions for a principal/user accessing the resource
3. IAM permission boundaries: set the maximum permissions an identity-based policy can grant an IAM entity
4. AWS Organizations services control policies (SCP): specify the maximum permissions for an organization
5. Session Policy: used with AssumeRole* API actions

## Root User VS IAM User
* Root user
   1. Use email address to login
   2. Unrestricted permissions (difficult to restrict)
* IAM user
   1. Use Friendly name to login + AWS account ID or alias
   2. Limited permissions (Can be limited via policy)

## Authentication Methods
* Before perform operations in AWS console, we need to authenticate ourselfes.
* There are several ways to login to AWS IAM as the following
1. API / CLI
   * Access Keys (Combined with Access Keys ID, Secret access keys, aka. long term credentials) are used for *programmatic* access.
2. Console Password 
   * Username, Password, MFA Token can be used to login to *AWS Management Console*
3. SSL/TLS certificates
   * Used for *server*.
* Multi Factor Authentication (MFA)
  * Use multiple alternative to login (such as password, biometric, physical device...)
  * ~Something you have

## Permission Boundaries
* Define the maximum permissions that are available to an IAM entity via an identity based policy
* Prevent **privilege escalation attack**
  * *Vertical attacks*: An attacker gains access to an account with the intent to perform actions as that user. (直接獲得帳號的Access權限，並以該用戶的身分進行操作)
  * *Horizontal attacks*: Gain access to accounts with limited permissions requiring an escalation of privileges, such as to an administor role, to perform the desired actions (透過獲取/新增具有一定權限的帳戶，並通過提升他們的權限來執行攻擊)

## Policy Evaluation
* What is happening when somebody tries to make access to a particular resource
* Why evaluation is need? 
  * All permissions are not allowed by default, everything is denied before setting up policy to allow some of the resource access / application activation.
1. Any **explicit deny** ?
   * explicit deny: override any allow.
   * Yes -> Deny
   * No -> Step 2.
2. Is the principal's account a member of an organization with an applicable SCP?

3. Does the request resources have a resource-based policy?


## Steps for Authorizing Requests to AWS
1. **Authentication**: ~Logging In (checks the identity of the user) to AWS IAM
   * Console, CLI, API
2. User **Forming Request context** with the following:
   * **Actions** - the actions / operation the principal(users) wants to perform
   * **Resources** - the AWS resource object upon which actions are performed
   * **Principal** - the user, role, federated user, or application that sent the request
   * **Environment Data** - Information about the IP address, user agent, SSL status, time of day
   * **Resource Data** - data related to the resource that is being requested
3. **Evaluating** Request context
   * Checking whether *user* can have policies to use the resources via **identity-based policy**
   * Checking whether *resource* have the rights to use via **resource-based policy**
4. **Determining** whether the request is *allowed* or *denied*

## Determination Rules
1. By default, all requests are implicitly denied (through the roor user has full access)
2. An explicit allow in an identity-based or resources-based policy overrides this default
3. If a permissions boundary, Organization SCP, or session policy is present, it might override the allow with an implicit deny

## 
* identity-based policy & Resource-based policy: 全部
* identity-based policy & Permission Boundary: and
* identity-based policy & SCP: and

## IAM policy structure
* Each AWS service has its own set of actions that describe tasks you can perform with that service -> API
* Written as *json*
```json
{
   "Version": "2012-10-17",
   "Statement": [
      {
         "Effect": "Allow",
         "Action": [
            "s3:*",
            "dynamodb:GetItem"
         ],
         "Resource": [
            "resource1",
            "resource2"
         ]
      }
   ]
}
```
* Statement: a block of code and has a series of individual **actions**, effects **resources**.
* All properties (Action, Resource) in a single statement block are evaluated together
* A policy may contain more than one permission statement.
* **Effect** is either *allow* or *deny*, we wanna deny something or allow it.
* **Action** lists the specific resource operations that the policy affects. (whay specifically we want to allow or deny)
* **Resource** lists the specific resources that the policy applies to.

## AWS IAM Best practices
1. Require human users to use federation with an identity provider to access AWS using **temporary credentials**. 
2. **Requite workloads to use temporary credentials with IAM roles to access AWS**
   * Create Users
   * Add user to user Groups
   * Apply (privilege) policies to user Groups
   * Users access to AWS with policies
   * More safety because no need to use long-time credentials
3. MFA
4. Rotate access keys regularly for use cases that require long-term credentials
5. Safeguard root user credentials & do not use them for everyday tasks
6. Apply Least-privilege permissions (give users the permission they need only)
7. **Get started with AWS managed policies** & move toward least-privilege policies
   * AWS generated some common policies with different situations
   * Reference from them, and optimize it
8. Use **IAM Access Analyzer** to generate least-privilege policies based on access activity
9. Clean up unused users, roles, permissions, policies, and credentials regularly
10. Use condition in IAM policies to further restrict access
    * With specified IP address
11. Verify public and cross-account access to resources with IAM Access Analyzer
12. Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions
13. Establish permissions guardrails across multiple accounts

## Architecture Patterns
1. A select group of users / priviledged users only should be allowed to change their IAM passwords. 
   * Create a group for the users and apply a permissions policy that grants the iam:ChangePassword API permission
2. An Amazon EC2 instance must be delegated with permissions to an Amazon Dynamo DB table. 
   * Create a role and assign a permissions policy to the rolw that grants access to the database service.
3. A company has created their first AWS account. They need to assign permissions to users based on job function. 
   * Use AWS managed policies that are aligned with common job functions
4. A solution architect needs to restrict access to an AWS service based on the source IP address of the requester. -> Create an IAM permissions policy and use the *Condition element* to control access based on source IP address.
5. A developer needs to make programmatic API calls from the AWS CLI. -> Instruct the developer to create a set of access keys and use those for programmatic access.
6. A group of users require full access to all Amazon EC2 API actions. -> Create a permissions policy that uses a wildcard(*) for the Action element relating to EC2 

## Exam Cram
* IAM is used to securely control individual and group access to AWS resources
* Manage: Users, Groups, Access policies, Roles, User credentials, password policies, MFA, CLI credentials
* New Users are created with NO access to any AWS services, only login to AWS console
* Permissions must be explicitly granted to allow a user to access an AWS service

* IAM is global (not apply to regions)
* eventually consistent
* Authentication methods: Console password (AWS Management Console), Access keys (programmatic access), Server Certificates (SSL/TLS certficates)
 
## Q/A
1. What is the best practice for applying permissions to many users who perform the same job role?
   * Add the users to an IAM group and apply a permissions policy to the group.
   * (Easier to control the permission at the same time.)
2. **Which IAM identity is used for assigning permissions to multiple users?
   * *Group* (not policy)
   * Although IAM policy can assign permissions, you should use a group to assign the permissions to multiple users.
3. How can you add an extra level of security to your root account?
   * Adding MFA 
4. Which IAM entity can be used to delegate (委派) permissions?
   * *Role*
   * It's good to provide permissions to resources for users and services without using permanent credentials.
5. Which element of an IAM policy document can be used to specify that a policy should take effect only if the caller is coming from a specific source IP address?
   * *Condition* (Action, Resource, Effect)
6. 