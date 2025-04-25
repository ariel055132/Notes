# Web, Mobile, ML and Cost Management

## AWS Amplify and AppSync
1. Amplify
   * Tools and features for *building full-stack applications on AWS*
2. Amplify Studio
   * *Visual interface* for building web and mobile apps
   * Add AWS services not available within Amplify Studio using the *AWS Cloud Development Kit (CDK)* 
   * Connect mobile and web apps using *Amplify Libraries* for iOS, Android, Flutter, and web
3. AppSync
   * *Fully Managed service that makes it easy to develop GraphQL APIs for fetch, change, and subscribe to data from servers*
   * For example, different modules are used to use APIs to communicate and integrate their service
   * AppSync will create a unified API layer to faster the communication

## AWS Device Farm
* *application testing service* used for web and mobile apps
1. Automated testing
   * Test your app in parallel against *a massive collection of physical devices* in the AWS Cloud.
   * No need to buy different types of machine and set them up before testing.
   * Use *automated testing framework* to test.
   * No need to write or maintain test scripts

## Machine Learning and AI services
1. **AWS Rekognition**
   * Identify information in images. (Identify objects, facial analysis, celebrity recognition)
2. **Amazon Transcribe**
   * Add speech to text capabilities to applications
   * Recorded speech can be converted to text before it can be used in applications
   * Use a deep learning process called *automatic speech recognition (ASR)* to convert speech to text quickly and accurately
3. **Amazon Translate**
   * Neural machine translation service that delivers fast, high-quality, and affordable *language translation*
   * Use deep learning models to deliver more accurate and more natural *sounding translation*
   * Localize content such as website and application for your diverse users
4. **Amazon Comprehend**
   * Use machine learning to *uncover information in unstructured data* (NLP service)
5. **Amazon Lex**
   * Conversational AI for Chatbots
   * Build conversational interfaces into any application using voice and text
6. **Amazon DevOps Guru**
   * Cloud operations service for improving *application operational performance and availability*
   * Detect behaviors that deviate from operating patterns
   1. Automatically detect operational issues
   2. Resolve issues with ML-powered insights
   3. Elastically scale operational analytics
   4. Use ML to reduce alarm noise  
7. **Amazon CodeGuru Security**
   * Detect, track, and fix code *security vulnerabilities* anywhere in the development cycle using ML and automated reasoning
   * Integrates with IDEs and CI/CD tools
   * Automated bug tracking
   * Assisted remediation through suggested code fixes
   * Offers performance optimization recommendations
   * Detect anomalies in application profiles

## AWS License Manager
* Used to *manage licenses from software vendors* (Microsoft, Oracle, SAP, IBM...)
* Centralized management of software licenses for *AWS* and *on-premises resources*
* Can *track license usage* including when licensed based on virtual cores (vCPUs), sockets, or number of machines
* Distribute, activate, and track software licenses across accounts and throughout an organization
* Enforce limits across multiple Regions

## AWS Compute Optimizer
* *Recommends optimal AWS resources for your workloads / instances* to reduce costs and improve performance
* Use *machine learning to analyze historical utilization metrics*
* Results:
  1. Findings
  2. Current instance type
  3. Current On-demand price
  4. *Recommended instance type*
  5. *Recommened on-demand price*
* Also for:
  1. Amazon EC2 instances
  2. Amazon EBS volumes
  3. AWS Lamdba functions 
* Results can be viewed in the console or via the CLI

## AWS Cost Management Tools
1. **AWS Cost Explorer**
   * A *free tool* that allows you to view charts of your costs
   * Can view *cost data for the past 13 months* + *forecast how much you are likely to spend* over the next three months
   * Used to discover patterns in how much you spend on AWS resources over time and to identify cost problem areas
   * Identify service usage statistics such as:
        1. Which services you use the most
        2. View metrics for which AZ has the most traffic
        3. Which linked account (linked accounts to the same organization) is used the most 

2. **AWS Cost & Usage Report**
   * *Publish AWS billing reports to an Amazon S3 bucket*
   * Reports breaks down costs by: Hour, day, month, product, product resource, tags
   * Can update the report to *three times a day*
   * Create, retrieve, and delete report using the AWS CUR API Reference

3. **AWS Price List API**
   * *Query the prices of AWS services*
   * Price List Service API (Query API) - query with JSON
   * AWS Price List API (Bulk API) - query with HTML
   * Alerts via Amazon SNS when prices change 