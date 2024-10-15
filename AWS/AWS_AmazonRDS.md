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
### Usecase
1. Data that is relatively static and frequently accessed
2. Applications that are tolerant of stale data
3. Data is slow and expensive to get compared to cache retrieval
4. Require push-button scalability for memory, writes and reads
5. Often used for storing session state
### Examples
1. Web session store
   * Load
2. Database caching
   * Cache popular queries to offload work from RDS and return results faster to users
3. Leaderboards
   * Use cache to provide a live leaderboard for millions of users of your mobile app
4. Streaming data dashboards
### Scaling
1. Memcached
   * Add nodes to a cluster
   * Scale vertically - node create a new cluster manually
2. Redis
   * Cluster mode disabled
     * add replica or change node type
     * create a new cluster and migrates data
   * Cluster mode enabled
     * Online resharding to add or remove shards; vertically scaling to change node type
     * Offline resharding to add or remove shards change node type or upgrade engine
   * 