# AWS Identity and Access Management (IAM)

## Objectives



## Authentication Methods

1. API / CLI
   * Access Keys
2. Console
   * Username, Password



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