# AWS Serverless Application
* Serverless
  * Do not have to manage anything underneath the platform at all, all of them done by platform (ready to use)
* AWS Lamdba
* API Gateway: Connect to an application via a rest API or an HTTP API

## Serverless Services 
* **No instances** to manage
* No hardware provision
* No management of operating systems or software
* **Capacity provisioning and patching is handled automatically**
* Provides automatic scaling and high availability

## Event-Driven Architecture


## AWS Lamdba
* One of the serverless services from amazon
* Execute code only when needed and scales automatically
* Maximum execution time: 15 mins (No applicable to run services which exceed 15 mins)
* You pay only for the compute time you consume
### Benefits
1. No servers to manage
2. Continuous scaling
3. Millisecond biling
4. Integrates with almost other AWS services
### Invocations
1. Synchronous (同步)
   * Wait for the function to process the event and return a response
   * Error handling happens client side (retries, exponential backoff)
2. Asychronous (非同步)
   * Event is queued for processing and a response is returned immediately
   * Retries up to 3 times
3. Event source mapping 

## Application Integration
1. **Simple queue service**
   * Message queuing service
2. **Simple Notification Service**
   * Sending notifications
3. **Step functions**
   * Orchestration & Worflow
4. Simple Workflow Service
5. Amazon MQ
6. Amazon Kinesis

## Amazon SQS (Simple Queue Service)
1. **Decoupling** (解耦)
   * When a backend system receives a call, it immediately responds with a request identifier and then asynchronously processes the request
   * When the web is getting busy suddenly, it can just put the message into the queue. The otherside will process the message in queue after they finished their original task.
2. **Direct Integration**
   * both web/app tiers connect to each other directly, all of them must keep up with workload or failure will occur
### Queue Types
1. **Standard Queue**
   * *Unlimited Throughput*: Supports a nearly unlimited number of transactions per second (TPS) per API action. 每秒訊息的傳輸量(TPS)幾乎是沒有限制
   * *Best-effor ordering*: Try best to maintain the ordering of the sent message  盡可能維持訊息的順序
   * *At-least-once delivery*: A message is delivered at least once, but occasionally more than one copy of a message is delivered 每個訊息至少傳送一次，但有時候同一個訊息不只傳送一次
2. **FIFO (First-In First-Out) Queue** 
   * *High Throughput*: Support 300 messages per second
   * *First-In-First-Out Delivery*: The order in which messages are sent and received is strictly preserved
   * *Exactly-Once Processing*: A message is delivered once and remains available until a consumer processes and deletes it. Duplicates are not introduced into the queue. 
   * Requires the **Message Group ID** and **Message Deduplication ID** parameters to be added to messages
   * *Message Group ID*: Tag that specifies that a message belongs to a specific messge group in order to guaranteed message belongs to same message group to be processed in a FIFO order
   * *Message Deduplication ID*: The token used for deduplication of messages within the deduplication interval. Ensure exactly once processing
* Dead Letter Queue
   * Used for analyze/handling message failure in SQS queue
   * You can set aside and isolate message that cannot be processed correctly to determine why their processing did not succeed
   * Failures: ReceiveCount > maxReceiveCount for queue --> Cannot receive the message
   * *Use Redrive Policy*: Enable Redrive Policy
   * *Dead Letter Queue*: Specify the queue to use as a dead-letter queue
   * *Maximum Receives*: Specify the maximum receives before a messagge is sent to the dead-letter queue
* Delay Queue
  * postpone the delivery of new messages to consumers for a number of seconds

### Short Polling AND Long Polling
* Short Polling: return the message **immediately** 
* Long Polling: retrieve message whthin **some seconds** 

## Amazon SNS (Simple Notification Service)
* Highly available, durable, secure, fully managed publisher/subscribers **messaging service**
### Procedure
1. Event Producer sends one message to one of the Amazon SNS Topic
2. Amazon SNS Topic will forwards the message to different subscibers (Lamdba, Web Application, etc.) via Transport Protocols

## AWS Step Function
* Build distributed applications as a series of steps in a visual workflow
1. Define the steps of your workflow. (JSON-Based Amazon States Language)
2. Start the execution to visualize and verify the steps of your applications are operating as intended. 

## AWS EventBridge
* Event-bus
1. Event sources generates events, those events will enter EventBridge Event Bus
2. EventBridge Event Bus will distribute the events to different destination according to the rules.