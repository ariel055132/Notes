# AWS Serverless Application
* Serverless
  * Do not have to manage anything underneath the platform at all, all of them done by platform (ready to use)
* AWS Lamdba, message buses, notification services, orchestration services
* API Gateway: Connect to an application via a rest API or an HTTP API

## Serverless Services 
* **No instances** to manage (No need to manage EC2)
* No hardware provision (coz No instances)
* No management of operating systems or software
* **Capacity provisioning and patching is handled automatically**
* Provides automatic scaling and high availability
* Developers just need to provided their code / applications to run

## Event-Driven Architecture
* use events to trigger and communicate between services.

* For example, 
* When a user is going to upload a file through a static website (==event).
* The AWS lamdba is triggered and process the file, the file will be put into S3.
* The SQS queue / CloudWatch will be triggered (something is inside S3)
* It may process the message with SNS or email, or store the log inside the DB in AWS.

## AWS Lamdba
* One of the serverless services from amazon
* Execute code only when needed and scales automatically
* Maximum execution time: 15 mins (No applicable to run services which exceed 15 mins)
* You pay only for the compute time you consume
* Ref: https://docs.aws.amazon.com/lambda/latest/dg/welcome.html
### Benefits
1. No servers to manage
2. Continuous scaling
3. Millisecond biling
4. Integrates with almost other AWS services
### Invocations
* Functions can executed concurrency
1. Synchronous (同步)
   * Wait for the function to process the event and return a response
   * Error handling happens client side (retries, exponential backoff)
   * E.G: CLI, SDK, API Gateway
2. Asychronous (非同步)
   * Event is queued for processing and a response is returned immediately
   * Retries up to 3 times
   * E.G: S3, SNS, Cloudwatch events
3. Event source mapping 
   * Lamdba polls the source (Check whether the source need Lamdba do something)
   * E.G: SQS, Kinesis Data Streams, DynamoDB Streams
### Use Cases
1. Data Processing
   * AWS Lamdba can instantly scale out more than 18k vCPUs to meet resource-intensive and unpredictable demand
   * AWS Kinesis
   * AWS S3
2. Run Interactive web and mobile backends / Serverless backends
3. 

## Application Integration Service
1. **Simple queue service (SQS)**
   * (What it does): Message queue, store and forward patterns
     * The application will do something, it may generate some response and logs.
     * The response and logs will be input into the messaging queue.
     * Another application may dig in the message queue and seek whether they need to do something.
   * (Use Cases): Building distrbuted / *decoupled* applications
2. **Simple Notification Service**
   * (What it does): Set up, and send notifications from the cloud
   * (Use Cases): Sending notifications (SNS / Email) when *CloudWatch* alarm is triggered 
3. **Step functions**
   * Orchestration & Worflow
   * (What it does): Out of the box coordinations of AWS service components with visual workflow
   * (Use Cases): Order processing workflow
4. Simple Workflow Service
   * (What it does): Need to support external processes / specialized execution logic
   * (Use Cases): Human-enabled workflows like an order fulfilment system / procedural requests
   * Step functions is prefered
5. Amazon MQ (Message Queue)
   * (What it does): *Message broker services* for Apache Active MQ and RabbitMQ
   * (Use Cases): Need a message queue that supports industry standard APIs and protocols
6. Amazon Kinesis
   * (What it does): Collect, process, and analyze *streaming data*
   * (Use Cases): Collect data from IoT devices for later processing

### Kinesis vs SQS vs SNS
* Kinesis
   1. Consumers pull data
   2. As many consumers as you need
   3. Routes related to records the same record processor
   4. Multiple applications can access stream concurrently
   5. Ordering at the shard level
   6. Can consume records in correct order at later time
   7. Must provision throughput

* SQS (Simple Queue Service)
   1. Consumers pull data
   2. Data is deleted after being consumed
   3. Can have as many workers (consumers) as you need
   4. No ordering gruarantee (Except with FIFO queues)

## Amazon SQS (Simple Queue Service)
* Pull-based: the consumer pulls the message from the queue
1. **Decoupling** (解耦)
   * When a backend system receives a call, it immediately responds with a request identifier and then asynchronously processes the request
   * When the web is getting busy suddenly, it can just put the message into the queue. The otherside will process the message in queue after they finished their original task.
   * NO dependency on the two different processing layers actually talking directly synchronously
2. **Direct Integration**
   * both web/app tiers connect to each other directly
   * all of them must keep up with workload or failure will occur 
   * -> We need decoupled integration
* Ref: source/Serverless/DecouplingWithSQSQueue.png
### Queue Types
1. **Standard Queue**
   * *Unlimited Throughput*: Supports a nearly unlimited number of transactions per second (TPS) per API action. 每秒訊息的傳輸量(TPS)幾乎是沒有限制
   * *Best-effor ordering*: Try best to maintain the ordering of the sent message  盡可能維持訊息的順序
   * *At-least-once delivery*: A message is delivered at least once, but occasionally more than one copy of a message is delivered 每個訊息至少傳送一次，但有時候同一個訊息不只傳送一次
   * If your application can handle messages that *might arrive more than once or out of order*, it is recommended to use Standard Queues.
      1. Allocating tasks to multiple worker nodes - E.G, handling a high volume of credit card validation requests
2. **FIFO (First-In First-Out) Queue** 
   * *High Throughput*: Support 300 messages per second
   * *First-In-First-Out Delivery*: The order in which messages are sent and received is strictly preserved
   * *Exactly-Once Processing*: A message is delivered once and remains available until a consumer processes and deletes it. Duplicates are not introduced into the queue. 
   * Requires the **Message Group ID** and **Message Deduplication ID** parameters to be added to messages
   * *Message Group ID*: Tag that specifies that a message belongs to a specific messge group in order to guaranteed message belongs to same message group to be processed in a FIFO order
   * *Message Deduplication ID*: The token used for deduplication of messages within the deduplication interval. Ensure exactly once processing
* Dead Letter Queue
   * Used for analyze/handling message failure in SQS queue 
   * it is a **standard or FIFO queue** that has been specified as a dead-letter queue in the configuration of **another standard or FIFO queue**.
   * You can set aside and isolate message that cannot be processed correctly to determine why their processing did not succeed
   * Failures: ReceiveCount > maxReceiveCount for queue --> Cannot receive the message
   * *Use Redrive Policy*: Enable Redrive Policy
   * *Dead Letter Queue*: Specify the queue to use as a dead-letter queue
   * *Maximum Receives*: Specify the maximum receives before a messagge is sent to the dead-letter queue
* Delay Queue
  * postpone the delivery of new messages to consumers for a number of seconds
### Short Polling AND Long Polling
* Polling: where and how your consumer is trying to find messages in the queue
1. Short Polling (短輪詢): return the message **immediately** 
   * Regardless of whether the server has updated data or not, requests are frequently sent, which may result in repeated and inefficient requests. (不管 Server 端有沒有更新資料，都會頻繁地發送 Request，可能會出現頻繁又無效的 request。)
   * Each request establishes a complete connection, and the HTTP/1.1 headers are not compressed. If the data updates are relatively small, a large portion of the transmission will consist of repeated headers. (每次 Request都是完整的連線，HTTP/1.1 的 Header 是沒有壓縮的，如果每次更新的資料其實不多，會發現大部份都是在傳輸重複的 Header。)
   * Polling occupies HTTP connections, frequently opening and closing TCP/IP connections. (Polling會佔用 HTTP 連線，頻繁地開啟與關閉 TCP/IP 連線。)
2. Long Polling: retrieve message whthin **some seconds** 
   * Not suitable for scenarios where messages are updated frequently. (不適合頻繁更新訊息的狀況。)
   * If a connection issue occurs, Long Polling has to wait until a timeout before sending a new request, which may result in delays in data retrieval. (如果某次連線出了問題，Long Polling 必須等到 timeout 後才會發新的 request，資料的獲取上會出現延遲。)
   * Each request establishes a complete connection, and the headers are not compressed. (跟Short Polling一樣，每次 Request都是完整連線，且Header 是沒有壓縮的。)

## Amazon SNS (Simple Notification Service)
* Highly available, durable, secure, fully managed publisher/subscribers **messaging service**
* Provides high-throughput, *push-based*, many-to-many messaging
* Components: 
  1. Publisher: Endpoint where send the information
  2. SNS Topic: "access point" for allowing recipients to dynamically subscribe for identical copies of the same notification
  3. Subscribers: Actual Services / endpoint where the information is received

### Procedure
1. Event Producer (*Publisher*) sends one message to one of the Amazon SNS Topic
2. *Amazon SNS Topic* will forwards the message to different *subscibers* (Lamdba, Web Application, etc.) via Transport Protocols

### Amazon SNS + Amazon SQS Fan-Out
* You can subscribe one / more Amazon SQS Queues to an Amazon SNS topic
* Amazon SQS manages the subscription and any necessary permissions
* When you publish a message to a topic, Amazon SNS sends the message to every subscribed queue

## AWS Step Function
* Build distributed applications as a series of steps in a *visual workflow* (state machines)
1. Define the steps of your workflow. (*JSON-Based Amazon States Language*)
2. Start the execution to visualize and verify the steps of your applications are operating as intended. 
   * AWS Step function *operates and scales* the steps of your application and underlying compute for you to help ensure your application executes reliably under increasing demand

## AWS EventBridge
* Serverless Event-bus, building distrbuted event-bus applications
1. **Event sources** generates events, those events will enter **EventBridge Event Bus**
2. EventBridge Event Bus will distribute the events to different **target** according to the rules.

* Event sources will process and generate state changes (*events*)
* Events will sent to *eventBridge event bus*
* The information is then *processed by rules* (Done by AWS Step Function) 
* The final / processed information will be sent through to various destinations

## AWS API Gateway
* Front door to your business logic or your application on AWS
* Can import Swagger / OpenAPI 3.0 definitions (YAML / JSON)

### Deployment Types
1. Edge-optimized endpoint
   * Amazon CloudFront (AWS Cloud) -> Amazon API Gateway
   * Reduce latency for requests from around the world
2. Regional endpoint
   * Services in the same (region) -> Amazon API Gateway
   * Reduced latency for requests that originate in the same region
   * Can also configure your own CDN and protect with WAF
3. Private Endpoint
   * Services in the same (VPC) -> Amazon API Gateway
   * Securely expose your REST APIs only to other services within your VPC or connect via Direct Connect

### Structure of a REST API
* A web Application will make a request via a published API
* The APIs will map the *request parameters* (GET, POST, PUT) of *method request* to the *format* required by the backend
* The request will be sent to endpoint / backend server
* The backend server will process the requests and send back the response to endpoint
* The endpoint will map the *status codes*, *headers*, and *payload* received from backend into format for client

### Integration
1. API Gateway + Lamdba functions
  * Proxy Integration: Just pass through the message, no changes / process is made
  * Custom Integration: Do some customized operations before pass the message
2. API Gateway + HTTP Endpoint
  * HTTP proxy integration
  * HTTP custom integration
3. For *AWS service action* you have the AWS integration of the non-proxy type only

### Caching
* Add cache by provisioning an *Amazon API Gateway cache* and specifying its size in gigabytes