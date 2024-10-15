# Database
* Understand relational, NoSQL data storage options, data warehousing with their use cases

# Note
1. Database on EC2
  * Need full control over instance and databas
  * Third-party database engine
2. Amazon RDS
  * Need traditional relational database
  * Data is Well-formed and structured
3. Amazon Dynamo DB
  * NoSQL database
  * In-memory performance
  * High I/O needs
  * Dynamic Scaling
4. Amazon RedShift
   * Data warehouse
5. Amazon ElastiCache
   * Fast temporary storage for small amounts of data
   * In-memory database

## Amazon Database - RDS (Relational Database Service)
* Manage **Relational Database in the cloud**
* Use **Amazon EBS volumes** for storage
* Backups can be taken using **EBS snapshots**
  * (Automated) backup
  * (Manual) Backup the entire DB instance, not just individual databases
  * do not expire
* Scaling up (vertically)
  * Scales up by changing the instance type
  * 2 CPUs, 8 GB RAM change to 4 CPUs, 32 GB RAM
* Scaling out (horizontally)
  * Reads horizontally with **read** Replicas
### RDS Security
* You can only enable encryption for an Amazon RDS DB instance when you create it, not after the DB instance is created.
* In other words, **DB instances that are encrypted cannot be modified to disable encryption**
* AWS KMS is used for managing encryption keys
* You cannot have an encrypted read replica of an unencrypted DB instance
* You cannot have an unencrypted read replica of an encrypted DB instance
1. *RDS Security Group*
   * **Manage network access to Amazon RDS instances**
   * Database security group default to a **deny al access mode**, customers must specifically authorize network ingress.
   * You must set of IP addresses using CIDR notation, and only network traffic originating from these addresses is recognized by your Amazon RDS instance
   * For example, you set the IP address access port as 3306. It means that requests from port 3306 can be access to DB. Other ports cannot access.
2. *RDS Encryption*
   * Encrypte the connection with SSL/TLS
   * RDS encrypt will be done to DB Volume and DB Snapshot

## Amazon Aurora
* one of the database in RDS, developed by AWS
* **MySQL and PostgreSQL compatible** relational database built for the cloud, 5 times and 3 times faster than MYSQL and PostgreSQL database respectively
* Distributed, fault-tolerant, self-healing storage system that auto-scales up to 128TB per database instances
### Fault Tolerance
* Across three AZs
* Single logicaln volume
* Scales-out read requests
* can promote Aurora Replica to be the new primary or create new primary
* Can use auto-scaling to add replicas

## Note
### Relational VS Non-Relational Database
* *Relational* 
  1. Organized by tables, rows and columns
  2. Rigid Schema (SQL)
  3. Rules enforced within database
  4. Typically scaled vertically
  5. Support complex queries and joins
  * E.G: Amazon RDS, Amazon Aurora
* *Non-Relational*
  1. Varied Data storage models
  2. Flexible Schema (NoSQL), data stored in key-value pairs
  3. Rules can be defined in application code
  4. Scaled horizontally
  5. Unstructured, simple language that supports any kind of schema
  * Amazon DynamoDB
### Graph Database
* Store, manage, navigate relationship in data
1. Node
  * Present entities
2. Edge
  * Present relationships
3. Properties
  * Store information about nodes and edges
### Operational / Transactional VS Analytical
* *Operational / Transactional*
  1. Online Transaction Processing (OLTP)
  2. Production DBs that **process transactions**. E.G. adding customer records, checking stock availability
  3. Short transactions and simple queries
* *Analytical*
  1. Online Analytics Processing (OLTP), the source data comes from OLTP DBs
  2. Data warehouse. Typically, separated from the customer facing DBs. For **decision making**.
  3. Long transactions and complex queries
  * E.G: Amazon Redshift, Elastic MapReduce