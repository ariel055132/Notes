# Test 5 - Question 29
## Question
* A manufacturing company wants to implement predictive maintenance on its machinery equipment. The company will install thousands of *IoT sensors that will send data to AWS in real time*.
* A solutions architect is tasked with implementing a solution that will *receive events in an ordered manner for each machinery asset* and *ensure that data is saved for further processing at a later time*.
* Which solution would be *MOST efficient*?

## Option
* A. Use Amazon Kinesis Data Streams for real-time events with a partition for each equipment asset. Use Amazon Kinesis Data Firehose to save data to Amazon S3.
* B. Use Amazon Kinesis Data Streams for real-time events with a shard for each equipment asset. Use Amazon Kinesis Data Firehose to save data to Amazon EBS.
* C. Use an Amazon SQS FIFO queue for real-time events with one queue for each equipment asset. Trigger an AWS Lambda function for the SQS queue to save data to Amazon EFS.
* D. Use an Amazon SQS standard queue for real-time events with one queue for each equipment asset. Trigger an AWS Lambda function from the SQS queue to save data to Amazon S3.

## Answer
* A. Use Amazon Kinesis Data Streams for real-time events with a partition for each equipment asset. Use Amazon Kinesis Data Firehose to save data to Amazon S3.

## Explanation
1. B. Amazon Kinesis Data Streams for real-time events with a shard + Amazon Kinesis Data Firehose
   * Shard 只是 for 分批上傳用
   * shard for each equipment would be extremely expensive and difficult to manage
2. C. Amazon SQS FIFO queue for real-time events with one queue for each equipment asset + Lambda
   * Creating a separate SQS FIFO queue for each equipment asset would be operationally complex and unscalable
   * You'd have to manage thousands of queues, which is a major administrative burden.
3. D. Amazon SQS standard queue for real-time events with one queue for each equipment
   * SQS standard queu does not guarantee event ordering