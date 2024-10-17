# Analytics
* Introduce the analytical tools of AWS
1. Amazon RedShift
2. Amazon Elastic Map Reduce (EMR)
3. Amazon Kinesis

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

## Amazon Kinesis
1. Amazon Kinesis Data Analytics
   * Use Apache Flink for processing data streams
2. Amazon Kinesis Data Firehose
   * Loads data straight to destinations

### Procedure
1. *Producers* capture and send data to Kinesis
2. In Kinesis, the data is then captured and stored in shard for processing
3. Consumers process the data and save the data to destinations with Kinesis client library (KCL)

### Kinesis Data Firehose
1. Producers send data to Firehose (Kinesis)
2. Firehose data is send to another AWS service for storing, data can be optionally processed/transformed using AWS Lamdba