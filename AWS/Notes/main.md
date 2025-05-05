# Questions
1. A company is deploying an application in three AWS Regions using an Application Load Balancer. **Amazon Route 53** will be used to distribute traffic between these Regions.
Whihc Route 53 should a architect use to provide the MOST **high-performing experience**?
   * 基本上是在考 Routing 53 的 哪個 Routing Policy 可以提升 Performance
   * Alias record with a latency policy *(This This This)*
   * Alias record with a geolocation policy
   * Geolocation Policy does not help improve performance, but helps route traffic based on the location of the users.

2. A company has an **application that runs on Amazon EC2 instances within a private subnet in a VPC**. The instances access data in an Amazon S3 bucket in the same AWS Region. The VPC contains a NAT gateway in a public subnet to access the S3 bucket. The company wants to **reduce costs** by replacing the NAT gateway without compromising security or redundancy.
Which solution meets these requirements?
    * Replace the NAT gateway with a NAT instance
      * 題目都要 replace NAT Gateway 了，換成 NAT instance 沒用
    * Replace the NAT gateway with an internet gateway
    * Replace the NAT gateway with a gateway VPC endpoint (*This This This*)
      * Gateway VPC Endpoint: Used for connect to AWS Secret in VPC privately
    * Replace the NAT gateway with a AWS Direct Connect connection
      * Direct Connection: Establish a dedicated network connection from on-premises servers to AWS

3. A company hosts more than 300 global websites and applications. The company requires a platform to **analyze more than 30 TB of clickstream data each day**.
What should a solutions architect do to transmit and process the clickstream data? 
    * Design an AWS Data Pipeline to archive the data to an Amazon S3 bucket and run an Amazon EMR cluster with the data to generate analytics.
    * Create an Auto Scaling group of Amazon EC2 instances to process the data and send it to an Amazon S3 data lake for Amazon Redshift to use for analysis.
      * Auto Scaling Group 只負責擴展 instance 的數量，並不會進行資料轉移等處理
    * Cache the data to Amazon CloudFront. Store the data in an Amazon S3 bucket. When an object is added to the S3 bucket, run an AWS Lambda function to process the data for analysis.
      * CloudFront 只負責將資料給 Regional Edge Server，再下放給 Users，這個選項看不懂。
    * Collect the data from Amazon Kinesis Data Streams. Use Amazon Kinesis Data firehose to transmit the data to an Amazon S3 data lake. Load the data in Amazon Redshift for analysis. (*This This This*)
    * *Source: source/Analytics/AWS_RealTimeClickStream.png* 

4. A company runs an application on Amazon EC2 instances. The application is **deployed in private subnets in three Availability Zones of the us-east-1 Region**. The instances must be able to **connect to the internet to download files**. The company wants a design that is highly available across the Region.
Which solution should be implemented to ensure that there are no disruptions to internet connectivity?
    * Application 設置在 Private Subnets，然後要連線到外面的網路去獲取資料 -> NAT Gateway / NAT instances
    * Deploy a NAT instance in a private subnet of each Availability Zone.
      * NAT instances / gateway should be in public subnet. 
    * Deploy a NAT gateway in a public subnet of each Availability Zone. (*This This This*)
    * Deploy a transit gateway in a private subnet of each Availability Zone.
    * Deploy an internet gateway in a public subnet of each Availability Zone.

5. A media company has an application that **tracks user clicks on its websites and performs analytics** to provide **near-real time recommendations**. The application has a fleet of Amazon EC2 instances that receive data from the websites and send the data to an Amazon RDS DB instance. Another fleet of EC2 instances hosts the portion of the application that is continuously checking changes in the database and executing SQL queries to provide recommendations. Management has requested a redesign to decouple the infrastructure. The solution must ensure that data analysts are writing SQL to analyze the data only. No data can the lost during the deployment.
What should a solutions architect recommend?
    * 看到 analytics，real time recommendations -> Kinesis 系列
    * Use *Amazon Kinesis Data Streams* to capture the data from the websites. *Kinesis Data Firehose* to persist the data on Amazon S3, and *Amazon Athena* to query the data.
      * Amazon Athena allows users to use interactions for writing SQL queries, not real-time = = ?
    * Use Amazon Kinesis Data Streams to capture the data from the websites. Kinesis Data Analytics to query the data, and Kinesis Data Firehose to persist the data on Amazon S3. (*This This This*)
    * Use Amazon Simple Queue Service (Amazon SQS) to capture the data from the websites, keep the fleet of EC2 instances, and change to a bigger instance type in the Auto Scaling group configuration.
    * Use Amazon Simple Notification Service (Amazon SNS) to receive data from the websites and proxy the messages to AWS Lambda functions that execute the queries and persist the data. Change Amazon RDS to Amazon Aurora Serverless to persist the data.

6. A user owns a **MySQL database** that is accessed by various clients who expect, at most, 100 ms latency on requests. Once a record is stored in the database, it is rarely changed. Clients only access one record at a time.
Database access has been increasing exponentially due to increased client demand. The resultant load will soon exceed the capacity of the most expensive hardware available for purchase. The user wants to migrate to AWS, and is **willing to change database systems**.
Which service would alleviate the database load issue and *offer virtually unlimited scalability for the future?
    * Amazon RDS
    * Amazon DynamoDB （*This This This*)
      * DynamoDB provide a fully managed NoSQL data storage solution with the ability to scale as per the demand.
    * Amazon Redshift
      * Redshift 是 Data warehouse solution，與題目無關
    * Amazon Data Pipeline
      * Data Pipeline 是轉移資料的 Solution，與題目無關

7. A company stores 200 GB of data each month in Amazon S3. The company needs to **perform analytics on this data at the end of each month** to determine the number of items sold in each sales region for the previous month.
Which analytics strategy is MOST cost-effective for the company to use?
    * 在進行分析之前，需要進行資料的預先
    * 不需要即時資料分析的話 -> Amazon Athena (透過 interactive 互動的方式來弄出對應的 SQL Queries 來進行資料獲取/分析)
    * Create an Amazon OpenSearch Service (Amazon Elasticsearch Service) cluster cluster. Query the data in Amazon ES. Visualize the data by using Kibana.
    * Create a table in the AWS Glue Data Catalog. Query the data in Amazon S3 by using Amazon Athena. Visualize the data in Amazon QuickSight. （*This This This*)
    * Create an Amazon EMR cluster. Query the data by using Amazon EMR, and store the results in Amazon S3. Visualize the data in Amazon QuickSight.
    * Create an Amazon Redshift cluster. Query the data in Amazon Redshift, and upload the results to Amazon S3. Visualize the data in Amazon QuickSight.

8. A company is hosting a **static website on Amazon S3** and is using **Amazon Route 53 for DNS**. The website is experiencing increased demand from around the world. The company must **decrease latency for users who access the website.**
Which solution meets these requirements MOST cost-effectively?
    * 若看到只是放 Static XX 不在 CloudFront，而在其他AWS 服務，基本上可以考慮用 CloudFront 來減低 latency，提升服務質素
    * Replicate the S3 bucket that contains the website to all AWS Regions. Add Route 53 geolocation routing entries.
      * 複製 S3 buckets，並把它們放到不同地方，其實很貴
      * 複製和資料持續更新的花費其實蠻多
    * Provision accelerators in AWS Global Accelerator. Associate the supplied IP addresses with the S3 bucket. Edit the Route 53 entries to point to the IP addresses of the accelerators.