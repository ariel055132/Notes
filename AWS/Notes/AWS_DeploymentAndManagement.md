# Deployment and Management
1. *AWS Cloud Formation*
   * Deploy infrastructure using code
2. *Elastic Beanstalk*
   * Platform as a service environment for deploying web apps / code
   * no need to focus on hardware
3. *AWS Config*
   * Manage configuration and complicance for your resources 
4. *SSM Parameter Store, AWS Secret Manager*
   * Store secrets like database connection information
5. *AWS Resource Access Manager*
   * Share resources with other accounts

## Terminology
1. Infrastructure as a Service (IaaS) 
   * Create a virtual server (~VMs, instances)
   * need to take care of hardware, software, and the application you want to deploy 
2. Platform as a Service (PaaS)
   * The platform will take care of the hardware and software
   * Users only need to deploy the applications with their code
3. SaaS
4. Web Servers
   * Standard applications that listen for and then process HTTP requests
   * Port 80
   * Place message in the Amazon SQS queue
5. Workers
   * Specialized applications that have a background processing task that *listens for messages on an Amazon SQS queue* (Polls the message from the queue)
   * Should be used for long-running tasks 

## Infrastructure as Code (IAC) with AWS CloudFormation
### Components
1. Template
   * The *JSON / YAML text file* that contains the instructions for building out the AWS environment
2. Stacks
   * The *entire environment* described by the *template* and created, updated, and deleted as a single unit 
3. StackSets
   * *The extentsion of stacks* by enabling you to create, update, or delete stacks across multiple accounts and regions with a single operation
4. Change Sets
   * *A summary of proposed changes to your stack* that will allow you to see how those changes might impact your existing resources before implementing them
   * (points out the differences between the deployed infrastructure and the new template file that is going to supply, user can confirm whether the difference is correct and determine to continue or cancel the change)

### Procedure
1. Define infrastructure patterns in a *template* file using *code* (JSON / YAML formats)
2. CloudFormation builds *infrastructure* according to the template
   * Define instances in VPC with Auto Scaling Group

### Advantages
* *Reusability* and *consistency* improvement
  * The template can be resused to another environment, no need to create another one from very beginning
  * As the content of template file is not changed greatly, the consistence of the template file improved

## Platform as a Service (PaaS) with AWS Elastic Beanstalk

### General Intro of AWS Elastic Beanstalk
* Provides a UI to monitor and manage the health of applications
* Managed platform update deploy the latest version of software and patches (Automate Update)

### Procedure
1. Users uploads source code to AWS Elastic Beanstalk
2. AWS Elastic Beanstalk will launched the application in EB Environment
   * Elastic Load Balancing (ELB), Auto Scaling Group (ASG) will be used automatically

### Layers 
1. Applications
   * Contain *environments*, *environment configurations*, and *application versions*
2. Environments
   * An application version that has been deployed on AWS Resources
   * The resources are configured and provisioned by AWS Elastic Beanstalk
   * The environment is comprised of all the resources created by Elastic Beanstalk and not just an EC2 instance with your uploaded code
3. Application version
   * A specific reference to a section of deployable code
   * Point typically to an Amazon S3 bucket containing the code
   * *Versions* can be applied to any *environment* (E.G: Development, Production) 

## AWS Systems Manager 
* Managing resources such as Amazon EC2

### AWS Systems Manager Parameter Store (SSM Paramater Store)
* Storing secrets and configuration information (data) with secure and hierarchical storage
* Store data such as passwords, database strings, and license codes as parameter values
* Store values as *plaintext* (unencrypted) or *ciphertext* (encrypted)
* *Reference values by using the unique name* that you specified when you created the parameter
  * ~Tags in Gitlab
* No native rotation of keys
  * Key rotation: The process of creating new encryption keys to replace existing keys, the primary goal 
  * (difference with AWS Secrets Manager which does it automatically)

## AWS Config
1. Evaluate AWS resource configuration for desired settings
2. Get a snapshot of the current configurations of resources that are associated with your AWS account
3. Retrieve configurations of resources that exist in your account
4. Retrieve historical configuration of one or more resources
5. Receive a notification whenever a resource is created, modified, or deleted
6. View relationships between resources
* Use *rules* to define config

## AWS Serets Manager
* Stores and rotate secrets safely without the need for code deployments
* Offers *automatic rotation of credentials* for
  * Amazon RDS (Relational Databasees Service, such as MySQL, PostrgreSQL, and Amazon Aurora)
  * Amazon Redshift
  * Amazon DocumentDB
* For other service, use *Amazon Lamdba* to implement automatic rotation

## Difference between AWS Secrets Manager & SSM Parameter Store
1. Automatic Key Rotation
   * (Secrets Manager): built-in for some services, use Lamdba for others
   * (SSM Parameter Store): No native key rotation, can use custom Lambda
2. Key/Value Type
   * (Secrets Manager): String / Binary (encrypted), 64 bit, much longer
   * (SSM Parameter Store): String, StringList, SecureString (encrypted)
3. Hierarchical Keys
   * (Secrets Manager): No
   * (SSM Parameter Store): Yes
4. Price
   * (Secrets Manager): Charges apply per secret
   * (SSM Parameter Store): Free for standard, charges for advanced

## AWS Resource Access Manager (RAM)
* Share resources within your accounts / across accounts
* Can be used to share:
  1. AWS App Mesh

## RPO, RTO, and DR Strategies
1. Recovery Point Objective (RPO)
   * 預防
   * Measurement of the amount of data that can be acceptably lost
   * Measured in seconds, minutes, or hours
   * Example:
     * You can acceptably lose 2 hours of data in a database (2hr RPO)
     * This means backups must be taken every 2 hours 
   * Strategies:
     * Milliseconds - Seconds: Synchronous Replication
     * Seconds - Minutes: Asynchronous Replication 
     * Minutes - Hours: Snapshots, Cloud Backup, Disk to Disk (D2D)
     * Hours - Days: Offsite, Tradition Backups, Tape Backups
2. Recovery Time Objective (RTO)
   * 發生意外時，預期修復所需之時間
   * Measurement of the amount of time it takes to restore after a disaster event
   * Measured in seconds, minutes, or hours 
   * Example:
     * The IT department expect it to take 4 hours to bring applications online after a disaster (4hr RTO)
     * This would be an RTO of 4 hours
   * Strategies
     * Milliseconds / Seconds: Fault Tolerance
     * Seconds - Minutes: High Availability, Load Balancing, Auto Scaling
     * Minutes - Hours: Cross-site recovery (Cloud), Automated Recovery
     * Hours - Days: Cross-site recovery (Cloud / On-permises), Manual Recovery
3. Disaster Recovery 
   * Backup and Rsstore
     * Low priority workloads
     * Provision / Restore after event
     * Lowest Costs
   * Pilot Light
     * Data Replicated
     * Service idle / off
     * Resources activated after event
     * Higher Costs
   * Warm Standby
     * Minimum resources always running
     * Business Critical Workloads
     * Scale up / out after event
     * Much higher Costs
   * Multi-site active
     * Zero downtime
     * Near Zero Data Loss
     * Mission Critical Workloads
     * Highest Costs
* Disaster Recovery (DR) Architecture on AWS, Part I: Strategies for Recovery in the Cloud
* Disaster Recovery (DR) Architecture on AWS, Part III: Pilot Light and Warm Standby

## Architecture Patterns
1. Applications must *authenticate* to Amazon Aurora and need to securely store credentials. *Automatic Credential rotation is required* on a monthly basis.
   * Use AWS Secrets Manager to store the credentials
   * Update the app to retrieve credentials from Secrets Manager
   * Enable automatic monthly rotation
2. Company currently use Chef Cookbooks to manage infrastructure and is moving to cloud. Need to minimize migration complexity.
   * Use AWS OpsWorks for Chef Automate
3. Need a managed environment for running a simple web application. App processes incoming data which can take several minutes per task
   * Use an Elastic Beanstalk environment with a web server for the app front-end