# Dynamo DB
* Fully managed NoSQL database service, Serverless
* Key/value store and document store (no schema)
* Non-relational, key-value type of database
* Fully serverless service
* Push button scaling

## Feature
1. Serverless
2. Highly available
3. NoSQL type of database with Name / Value structure
4. Horizontal scaling
5. DynamoDB stream
6. DynamoDB Accelerator (DAX)
7. Transaction Options
8. Backup 
9. Global Tables

## DynamoDB Time to Live (TTL)
* Enables a per-item timestamp to determine when an item is no longer needed
* After the data and time of the specified timestamp, DB deletes the item from the table without consuming any write throughput
* Good: Help reduce storage and manage the table size over time

## Primary Keys
1. *Partition Key* (aka. Hash key)
   * Simple primary key, composed of one attribute
   * Used as input to an internal hash function; the output from the hash function determines the partition where the item will be stored (使用Partition Key來計算資料存放節點)
   * No two items in a table can have the same partition key value. (otherwise, collision is happen)
2. *Partition Key and Sory Key* (aka. Hash and Range Key)
   * Sorted by sort key value

## DynamoDB Streams
* Capture a **time-ordered** sequence of **item-level changes** made to a data in a table and store this information in a log for up to **24 hours**
1. KEYS_ONLY - Key attributes of the modified item
2. NEW_IMAGE - Entire item, after it was modified (~updated data)
3. OLD_IMAGE - Entire item, before it was modified (~original data)
4. NEW_AND_OLD_IMAGE - Both NEW_IMAGE and OLD_IMAGE

## DynamoDB Accelerator (DAX)
* fully managed, highly available, **in-memory cache** for DynamoDB 
* improve the READ and WRITE performance of DynamoDB tables to microseconds with read-through cache and a write-through cache
* DAX is optimized for DynamoDB (~Best Practice)

## DynamoDB Global Tables


## Amazon RedShift
* SQL based Data-warehouse solution (for data analysis, OLAP)
* use Amazon EC2 instances
* keeps 3 copies for your data
* Continuous backup

### Data Sources
1. Amazon RDS
2. Amazon DynamoDB
3. Amazon EMR
4. Amazon S3
5. Amazon Data Pipeline
6. AWS Glue
7. Amazon EC2
8. On-Premises Server

### Use Case
* Perform complex queries on massive collections of **structured** and **semi-structured** data and get fast performance
* Frequently accessed data that needs a consistent, highly strucutred format
* Use Spectrum for direct access of S3 objects in a data lake

## Amazon Elastic Map Reduce (EMR)
* Managed cluster platform that simplifies running big data frameworks including Apache Hadoop and Apache Spark
1. Used for **processing data** for analytics and business intelligence
2. Transforming and moving large amounts of data
3. Perform extract, transform, and load (ETL) function 

## Amazon Kinesis data streams
1. Amazon Kinesis Data Analytics
   * Use Apache Flink for processing data streams
2. Amazon Kinesis Data Firehose
   * Loads data straight to destinations