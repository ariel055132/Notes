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
4. CloudWatch Events
   * Stream of system events describing changes to AWS resources and can trigger actions (**Automated Action**)

### CloudWatch Metrics
* Metrics and sent to CloudWatch for AWS services
* EC2 metrics are sent every **5 minutes** by default, it does not include memory utilization or disk usage
* Details EC2 monitoring sends every **1 minute**(chargeable)
* Unified CloudWatch Agent sends system-level metrics for EC2 and on-premises servers
* System-level metrics include memory and disk usage
* (You have EC2 and CloudWatch, then EC2 instances is sending metrics either every 5 minutes / 1 minute. If you install the Unified CloudWatch Agent, you also get additional information includes memory and disk usage)
* Can publish custom metrics using CLI or API
  * Standard resolution: Data having a one-minute granularity 
  * High resolition: Data at a granularity of one second
  * 資料顆粒度...(～詳細程度)

### CloudWatch Alarms
1. Metric alarm
   * Performs one or more actions based on a single metric
   * OK (metric is within a threshold)
   * ALARM (Outside a threshold)
   * INSUFFICIENT_DATA (Not enough data)
2. Composite alarm
   * Uses a rule expression and takes into account multiple alarms