--- 
marp: true
theme: gaia
---

# Amazon AWS IAM

Start Date: 21-1-2025
Finished Date: ?
Presenter: Adrian

---

# Overview

- What is IAM?
- IAM Concepts (Users, Group, Roles, Policy)

--- 

# What is IAM?

- AWS **I**dentity and **A**ccess **M**anagement Service
- Used to securely control individuals and group access to AWS resources (權限管理，限制使用者在AWS使用資源範圍)

---

# IAM Concepts Figure
![bg 70%](https://github.com/ariel055132/Notes/blob/main/AWS/source/IAM/AWS_IAM_ConceptOverview.png?raw=true)

---

![bg 80%](https://github.com/ariel055132/Notes/blob/main/AWS/source/IAM/AWS_IAM_Users_UserGps_Roles_Policies.png?raw=true) 

---

# IAM Concepts 說明
1. **Users**: An entity that represents a person or service (AWS 的登入帳號，目的是存取AWS裡面的資源)
2. **Group**: A collection of users and have policies attached to them (許多User的集合，在Group底下的Users將統一繼承Group被設定的Policy)
3. **Roles**: An identity which has permissions assigned to it via policy (權限綁定，被設計出來給不是 User 和 Group 使用)
4. **Policy**: Defines the permissions for the identities or resources they are associated with (規範使用者的AWS使用資源權限)

---

![bg 90%](https://github.com/ariel055132/Notes/blob/main/AWS/source/IAM/AWS_IAM_Users.png?raw=true)

--- 

# IAM Users / Principals

- *Root User* : has **full permissions**, permissions cannot be changed, avoid using it, login with **email address**
- *IAM User* : Created to represent applications, up to 5000 users per AWS Account， login with **username/password or access keys**
- Permissions limited by permisson policy, login with friendly name + AWS account ID
- By default **users cannot access anything in your account** before any policies is assigned
- 正常的User在一開始被創建的時候是沒有任何權限，只是能登入進 AWS Console

--- 

![bg 90%](https://github.com/ariel055132/Notes/blob/main/AWS/source/IAM/AWS_IAM_UsersGps.png?raw=true)

---

# IAM Groups

- **Collections of users** & have policies attached to them 
- No nested groups (groups within groups)
- 可以一次賦予多個使用者相同的權限

---

# IAM Roles

- Delegate permissions to resources for users and services （讓 IAM User/Group、AWS Resource(例如：EC2 instance)、臨時需要存取 AWS 資源的外部帳號 … 等取得權限用的機制)
- Temporary security credentials by **AWS Security Token Services (STS)**

---

# IAM Security Token Service （STS）

---

# IAM Policies
* Documents that define permissions and can applied to users, groups and roles (定義使用者可在AWS資源中做什麼事情)
* AWS 會在執行 API 列明的動作前，將檢查 Policies 中是否允許執行相關動作
* Types of Policies:
  1. Identity-based policies
  2. Resources-based policies
  3. IAM permission boundaries
  4. AWS Organizations service control policies (SCP)

---

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": "*",
      "Resource": "*"
    }
  ]
}
```
* **Effect** is either *allow* or *deny* (允許/拒絕資源存取)
* **Action** lists the specific resource operations that the policy affects (Policies 的具體資源操作種類)
* **Resource** lists the specific resources that the policy applies to (Policies 適用的資源)

---

![bg 80%](https://github.com/ariel055132/Notes/blob/main/AWS/source/IAM/AWS_IAM_AuthenticationMethods.png?raw=true)

---

# Authentication Methods
- 在AWS Console / Command Line 執行相關動作前，需要進行身分認證，認證方法分為三種：
 1. *API / CLI*: 若透過 **CLI / 程式** 登入 AWS，則需要 Access Keys
 2. *Console Password*: 若需要登入 **AWS Console**，則輸入 Username, Password & MFA Token 
 3. *SSL/TLS certificates*: **Server** 使用 SSL 進行認證

---

# IAM Best Practice
