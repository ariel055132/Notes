# AWS Identity and Access Management (IAM)

## Objectives



## Authentication Methods
* There are several ways to login to AWS IAM.
1. API / CLI
   * Access Keys (Combined with Access Keys ID, Secret access keys, aka. long term credentials) -> IAM -> AWS API
2. Console
   * Username, Password, MFA Token (Optional) -> IAM -> Management Console.
* Multi Factor Authentication
  * Use multiple alternative to login (such as password, biometric, physical device...)

## Terminology
1. Account Root User
   * User has full permissions
   * Avoid using it + enable MFA (multifactor authentication)
2. Users
   * up to 5000 individual user account can be created.
   * Have no permissions by default

   * The users gains the *permissions* applied to the *group* through the *policy*.
   * *Friendly name* : 
   * *Amazon resources name* : 

3. User Groups
   * A collection of users.
   * You can add multiple common users, and then applying permission policies to the same group (determine what users are allowed to do, what API actions are they allowed)\
   * It is easier to manage the permission for those users.
4. Roles
   * An identity which has permissions assigned to it via policy
5. (identity-based) Policies
   * defines the permissions for the identities or resources they are associated with.

## Types of policy
1. Identity-based policy: attached to users, groups, or roles
2. Resource-based policy: attached to a resource; define permissions for a principal/user accessing the resource
3. IAM permission boundaries: set the maximum permissions an identity-based policy can grant an IAM entity
4. AWS Organizations services control policies (SCP): specify the maximum permissions for an organization or OU

## Permission Boundaries
* Define the maximum permissions that are available to an IAM entity via an identity based policy
* Prevent **privilege escalation attack**
  * Vertical attacks: An attacker gains access to an account with the intent to perform actions as that user. (直接獲得帳號的Access權限，並以該用戶的身分進行操作)
  * Horizontal attacks: Gain access to accounts with limited permissions requiring an escalation of privileges, such as to an administor role, to perform the desired actions (透過獲取/新增具有一定權限的帳戶，並通過提升他們的權限來執行攻擊)

## Policy Evaluation
* What is happening when somebody tries to make access to a particular resource
* Why evaluation is need? All permissions are not allowed by default, everything is denied.
1. Any **explicit deny** ?
   * explicit deny: override any allow.
   * Yes -> Deny
   * No -> Step 2.
2. Is the principal's account a member of an organization with an applicable SCP?

3. Does the request resources have a resource-based policy?


## Steps for Authorizing Requests to AWS
1. Authentication: ~Logging In (checks the identity of the user)
2. User **Forming Request context** with the following:
   * **Actions** - the actions / operation the principal(users) wants to perform
   * **Resources** - the AWS resource object upon which actions are performed
   * **Principal** - the user, role, federated user, or application that sent the request
   * **Environment Data** - Information about the IP address, user agent, SSL status, time of day
   * **Resource Data** - data related to the resource that is being requested
3. **Evaluating Request context**
   * Checking whether *user* can have policies to use the resources via **identity-based policy**
   * Checking whether *resource* have the rights to use via **resource-based policy**
4. Determining whether the request is allowed or denied

## Determination Rules
1. By default, all requests are implicitly denied (through the roor user has full access)
2. An explicit allow in an identity-based or resources-based policy overrides this default
3. If a permissions boundary, Organization SCP, or session policy is present, it might override the allow with an implicit deny