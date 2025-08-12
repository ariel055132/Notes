# Test 4 - Question 55
## Question
* A company has a legacy application that process data in two parts. The second part of the process takes longer than the first, so the company has decided to *rewrite the application as two microservices* running on Amazon ECS that can *scale independently*.
* How should a solutions architect integrate the microservices?

## Option
* A. Implement code in microservice 1 to send data to an Amazon S3 bucket. Use S3 event notifications to invoke microservice 2.
* B. Implement code in microservice 1 to publish data to an Amazon SNS topic. Implement code in microservice 2 to subscribe to this topic.
* C. Implement code in microservice 1 to send data to Amazon Kinesis Data Firehose. Implement code in microservice 2 to read from Kinesis Data Firehose.
* D. Implement code in microservice 1 to send data to an Amazon SQS queue. Implement code in microservice 2 to process messages from the queue.

## Answer
* D. Implement code in microservice 1 to send data to an Amazon SQS queue. Implement code in microservice 2 to process messages from the queue.

## Explanation
* Microservices with SQS can be used to create a loosely coupled architecture, where the microservices can scale independently. Second MS can scale based on the number of messages in the message queue.

* Options A & B are wrong as using S3 event notifications or SNS cannot help scale the second microservice as they would more of push fire and forget notification.
* Option C is wrong as Kinesis Data Firehose does not support MS as its target. Kinesis Data Firehose is the easiest way to reliably load streaming data into data lakes, data stores and analytics tools. It can capture, transform, and load streaming data into Amazon S3, Amazon Redshift, Amazon Elasticsearch Service, and Splunk, enabling near real-time analytics with existing business intelligence tools and dashboards you’re already using today.

