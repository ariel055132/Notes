# Overview
1. Create a accounts in AWS
2. *Account Root User* (Full control over the account, should not use it until you are needed to do so)
3. Use *AWS IAM* to create users, groups. roles and policies.
    * Create a *user* first, you may setup its *roles*.
    * Create a *group* to put the user into.
    * Associate a *policy* that has permissions to that group 

# How to Login to AWS
* After creating the user, you can login to AWS via **AWS Management Console**.
* Authentication: We have different approaches to authentiate through *console, API, CLI*. (Prove who we are, what we say we are)
* Authorization: Create resources across AWS regions. (Grants rights to use the resources.)