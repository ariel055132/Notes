# Monitoring, Logging and Auditing
1. CloudWatch 
2. CloudTrail
3. EventBridge
4. Metrics Analysis and Tracing

## CloudWatch
* Performance Monitoring Tool, alarms, log collection and automated action

### Core Features
1. CloudWatch Metrics 
   * Send time-ordered data points to CloudWatch (**Performance Monitoring Tool**)
2. CloudWatch Alarms
   * Perform actions to auto-scaling or stop, start, or to terminate instances
   * Send notifications using SNS actions
   * (**Alarms**)
3. CloudWatch Logs
   * Centralized collection of system and application logs (**Log Collection**) 
4. CloudWatch Events / Eventbridge
   * Stream of system events describing changes to AWS resources and can trigger actions (**Automated Action**)

### CloudWatch Metrics
* Metrics and sent to CloudWatch for AWS services
* EC2 metrics are sent every **5 minutes** by default, it does not include memory utilization or disk usage
* Details EC2 monitoring sends every **1 minute**(chargeable)
* Unified CloudWatch Agent sends system-level metrics for EC2 and on-premises servers
* System-level metrics include memory and disk usage
* (You have EC2 and CloudWatch, then EC2 instances is sending metrics either every 5 minutes / 1 minute. If you install the Unified CloudWatch Agent, you also get additional information includes memory and disk usage)
* Can publish custom metrics using CLI or API
  * *Standard resolution*: Data having a **one-minute** granularity 
  * *High resolition*: Data at a granularity of **one second**
  * 資料顆粒度...(～詳細程度)

### CloudWatch Alarms
1. Metric alarm
   * Performs one or more actions based on a single metric
   * OK (metric is within a threshold)
   * ALARM (Outside a threshold)
   * INSUFFICIENT_DATA (Not enough data)
2. Composite alarm
   * Uses a rule expression and takes into account multiple alarms

### CloudWatch Logs
* Amazon EC2 / On-premises servers will send the *application logs* to Amazon CloudWatch.
  * If Unified CloudWatch agent is installed on EC2 / On-premises servers, *system logs* are also send to Amazon CloudWatch.
  * Lamdba can also be input to Amazon CloudWatch, but permission is required
* CloudWatch export the collections of logs to Amazon S3 / Kinesis Data Streams / Kinesis Data Firehose for data processing.

### Unified CloudWatch Agent
* Collect System-logs
* The logs will send to CloudWatch when it is generated. (The logs will not be loss even the instances is terminated)

### CloudTrail
* Capture information about the **API actions** that are happening in your AWS account
  * *Management Events* (data about management operation that are performed on resources in AWS account)
  * *Data events* (resources operations performed in resource, S3)
  * *Insights events* 
* Management events are logged and retained for 90 days

1. CloudTrail record the API actions, and It may do the following actions:
* S3 Bucket can create a trail for indefinite retention, and also enable log file integrity validation (check whether the log file is modified...)
* Notifications can be triggered through SNS topic when CloudTrail publishes log files
* Forward logs to CloudWatch Logs
* Forward logs to CloudWatch Events and trigger a Lamdba function

### Metrics Analysis and tracing
1. *AWS X-ray*
   * Visualize the components of your application
   * Identify performance bottlenecks
   * Troubleshoot request that resulted in an error
   * *X-ray agent* is required (X-ray SDK is used to capture metadata for requests made to databases)
2. *Promethesus*  
   * Monitor and alert on the performance of containerized workloads
   * Automatically scales the ingestion, storage, alerting, and querying of operational metrics as workloads grow and shrink
3. *Grafana*
   * Data Visualization of monitoring and opreational data

## Architecture Patterns
1. Need to stream logs from Amzon EC2 instances in an Auto Scaling Group **(?)**
   * Install the Unified CloudWatch Agent and collect logs files in Amazon CloudWatch
2. Need to collect from EC2 instances with a **1 second granularity**
   * Create a custom metric with *high resolution*
   * Standard resolution: one minute granularity
3. The application logs from on-premises servers must be proessed by AWS Lambda in real time
   * Install the unified CloudWatch Agent on the servers and use a subscription filter in CloudWatch to connect to a Lamdba function.