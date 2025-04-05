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

## Infrastructure as Code (IAC) with AWS CloudFormation
### Components
1. Template
   * The *JSON / YAML text file* that contains the instructions for building out the AWS environment
2. Stacks
   * The *entire environment* described by the *template* and created, updated, and deleted as a single unit 
3. StackSets
   * The extentsion of stacks by enabling you to create, update, or delete stacks across multiple accounts and regions with a single operation
4. Change Sets
   * A summary of proposed changes to your stack that will allow you to see how those changes might impact your existing resources before implementing them

### Procedure
1. Define infrastructure patterns in a *template* file using *code* (JSON / YAML formats)
2. CloudFormation builds *infrastructure* according to the template
   * Define instances in VPC with Auto Scaling Group

### Advantages
* *Reusability* and *consistency* improvement