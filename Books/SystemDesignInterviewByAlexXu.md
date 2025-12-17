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
  1. Consider using cache when data is read frequently but modified infrequently
  2. Do not store important data in cache as it is volatile memory
  3. Design a proper expiration policy.
  4. Migrating failures: Setup miltiple cache servers
  5. **Eviction Policy**: Once the cache is full, any requests to add items to the cache might cause existing items to be removed. Least-recently-used (LRU) is most popular. (如果 Cache 的容量爆了怎麼辦？通常將最少使用的 Cache 資料拿掉)

#### Content Delivery Network (CDN) 
* A network of geographically despersed servers used to deliver static content.
* ~Cache, but for static content
* **CDN Workflow**
  1. User
* **CDN Consideration**
  1. Cost: CDNs are run by third-party providers (E.G: Amazon CloudFront), and you are charged for data transfers in and out of the CDN.
  2. Setting an appropriate cache expiry: 
  3. CDN fallback: Consider how your website/application copes with CDN failure. If there is a temporary CDN outage, clients should be able to detect the problem and request resources from the origin.
  4. Invalidating files: 

#### Stateful and Stateless web tier
* Stateful server remembers client data from one request to the next 
  * In another word, every request from the same client must be routed to the same server
  * Adding / removing servers is much more difficult.
  * E.G: Shopping website (need to save the latest shopping cart information of different clients)
* Stateless server keeps no state information
  * In another word, HTTP requests from users can be sent to any web servers
  * More simpler, more robust, and scalable
  * E.G: Weather checking website (always return the latest weather information to clients)