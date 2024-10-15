# Amazon Relational Database Service - RDS
* A web service that makes it easier to setup, operate, and scale a relational database in the cloud


## RDS Components


### Aurora Multi-Master
* All nodes allow read/writes
* Available for MySQL only
* up to 4 read/write nodes
* cannot have corss-region replicas
* can work with active-active and active-passive workloads
* can restart read/write DB instance without impacting other instances

### Aurora Serverless
* router fleet: Controls connections that are coming to db
* Apply ACU (Aurora Capacity Unit) 
1. Infrequently used applications
2. Variable & Unpredictable workloads

## RDS Proxy
* Database proxy for RDS
  * Manage connection from different source, such as lamdba
* Highly available across multiple AZs
* Objective: Increase scalability, falut tolerance, and security
  1. Reduce stress on CPU/MEM
  2. Shares infrequently used connections
  3. Drivers increased efficiency
  4. High availability with failover
  5. Control authentication methods 

## ElastiCache
* In-memory database (High performance and low latency)
* often used for caching data that comes from other database
* Implementations of Redis and Memcached
* key/value store
* can be put in front of databases such as RDS and DynamoDB
* Run on Amazon EC2 instance, choose an instance family/type