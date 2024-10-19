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

### Overall Procedure
1. *Producers* capture and **send data** to Kinesis
2. In *Kinesis*, the data is then captured and **stored in shard for processing**
3. *Consumers* process the data and save the data to **destinations** with Kinesis client library (KCL)
4. We can use analytial tools to analysis them

### Kinesis Data Firehose
1. Producers send data to Firehose (Kinesis)
2. Firehose data is send to another AWS service for storing, data can be optionally processed/transformed using AWS Lamdba
* Near real-time delivery (~60 seconds latency)

### Kinesis Client Library (KCL)
* Help you consume and process data from a Kinesis data stream
* KCL enumerates shards and instantiates a record processor for each shard it manages
* Each shard is processed by exactly one KCL worker
* A record processor maps to exactly one shard

## Kinesis Data Analytics
* Provides real-time SQL processing for streaming data
* Provides analytics for data coming in from Kinesis Data Streams and Kinesis Data Firehose
* Destinations can be Kinesis Data Streams, Kinesis Data Firehose, or AWS Lamdba

## Amazon Athena 
* Serverless service that we can use to run SQL queries against data
* Can be connected to other data source with Lamdba
* Data can be in CSV, TSV, JSON, Parquet and ORC formats
* Use a managed data catalog (AWS Glue) to store information and schemas about the databases and tables
### Optimizing Athena
1. Partition your data
2. Bucket your data (Bucket the data within a single partition)
3. Use Compression (esp. Apache Parquet / Apache ORC)
4. Optimize file sizes
5. Optimize columnar data store generation
6. Optimize ORDER BY and Optimize GROUP BY
7. Use approximate functions
8. Only include the columns that you need

## AWS Glue
* used as metadata catalog
* Fully managed ETL service, for preparing data for analysis
* Discovers data and store the metadata in the AWS Glue Data Catalog
* Use a crawler to populate the AWS Glue Data Catalog with tables

## Amazon OpenSearch service (ElasticSearch)
* Successor to **Amazon Elasticsearch Service**
* Distributed search and analytics suite
* Support queries using SQL syntax
* Scale by adding / removing instances
* Availability in up to three Availability Zones
* Backup using snapshots
* Encryption at-rest and in-transit
1. Fully Managed
   * Search, visualiza, and analyze *text and unstructured data*
2. Petabyte Scale
3. Secure
   * Deploy to Amazon VPC and integrates with IAM
4. Highly Available
5. Scalable
   * You can scale up by deploy nodes and replicas across different AZs

### Deployment
1. Define cluster (number of instance, instance type, storage option)
2. Ingest data into opensearch service domains, you may visualize the data with Kibana DashBoard
3. Deploy cluster
   * VPC (secure intra VPC communications)
   * VPN / Proxy 
   * No IP-based access policies

### Access Control
1. Resource-based policies (aka. domain access policy)
2. Identity-based policies
   * Attached to users or roles
3. IP-based policies 
   * Restrict access to one or more IP addresses or CIDR blocks
4. Fine-grained access Control
   * Role-based access Control
   * Security at the index, document, and field level
   * OpenSearch DashBoard multi-tenancy
   * HTTP basic authentication for OpenSearch and OpenSearch Dashboards

## ELK Stack
* *E*lasticsearch, *L*ogstash, *K*ibana
* Used to aggregate logs from systems and applications, analyze these log
* Connect them to Amazon OpenSearch Service

