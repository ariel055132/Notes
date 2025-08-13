# Test 4 - Question 41
## Question
* A company is planning to migrate a business-critical dataset to Amazon S3. The current solution design uses a single S3 bucket in the us-east-1 Region with versioning enabled to store the dataset. The company's disaster recovery policy states that *all data must be available multiple AWS Regions*.
* How should a solutions architect design the S3 solution?

## Option
* A. Create an additional S3 bucket in another Region and configure cross-Region replication.
* B. Create an additional S3 bucket in another Region and configure cross-origin resource sharing (CORS).
* C. Create an additional S3 bucket with versioning in another Region and configure cross-Region replication.
* D. Create an additional S3 bucket with versioning in another Region and configure cross origin resource (CORS).

## Answer
* C. Create an additional S3 bucket with versioning in another Region and configure cross-Region replication.

## Explanation
* Option A is wrong as both source and destination buckets must have versioning enabled.
* Options B & D are wrong as Cross-origin resource sharing (CORS) defines a way for client web applications that are loaded in one domain to interact with resources in a different domain. With CORS support, you can build rich client-side web applications with Amazon S3 and selectively allow cross-origin access to your S3 resources.
  * CORS 是 for web 可以跨 bucket 獲取資料用，並非題目要的 data available multiple AWS Regions