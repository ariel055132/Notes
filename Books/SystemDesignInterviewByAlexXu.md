# System Design Interview by Alex Xu

## Chap 1. Scale From Zero to Millions of users
* Discusses building systems progressively, from simple architecture to large-scale deployments
* Key Terminologies

### Simple Architecture
1. Server
2. Database

### Terminology
#### Scalability
1. Vertical Scaling
   * Scale-Up
   * Adding more power to servers
2. Horizontal Scaling
   * Scale-Out
   * Adding more servers 
* Note: Horizontal scaling is more desirable
  * It is impossible to add unlimited CPU and memory to a single server 
  * Vertical Scaling does not have failover and redundancy. It means if one server goes down, the website/app goes down with it completely 
3. Load Balancer
  * Distributes incoming traffic among web servers that are defined in a load-balancer set

#### Database
1. Relational Database (RDBMS)
   * E.G: MySQL, Oracle DB, PostgreSQL
2. Non-Relational Database (NoSQL)
   * DynamoDB, MongoDB 
   * Advantage: Super-low latency, unstructured data, need to serialize and deserialize data, store massive amount of data (?)
3. Replication
   * Creating copies of database to improve reliability, availability, and performance
   * **Master Database** (Original): Handles write operations (INSERT, UPDATE, DELETE)
   * **Slave Database** (Copies): Handles read operations (QUERY)
   * Master-Slave Replication: Data flow from master to slaves (ensure data integrity)

#### Caching
* *Temporary Storage area* that store the result of expensive responses or frequently accessed data in memory so that subsequent requests are served more quickly
* E.G: Redis
* **Cache Flow**
  1. Web server receives request and checks cache for data
  2. **Cache hit**: Return cache data directly to client
  3. **Cache miss**: 
    * Query database from database
    * Store result in cache for further request
    * Return response to client
* **Cache Consideration**

#### Content Delivery Network (CDN) 