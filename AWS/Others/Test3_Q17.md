# Test 3 - Question 17
## Question
* A company has deployed a multiplayer game for mobile devices. The game requires live location tracking of players based on latitude and longitude. The data store for the game must support rapid updates and retrieval of locations.
* The game uses an *Amazon RDS for PostgreSQL DB instance* with read replicas to store the location data. During peak usage periods, the database is unable to maintain the performance that is needed for reading and writing updates. The game's user base is increasing rapidly.
* What should a solutions architect do to *improve the performance* of the data tier?

## Option
* A. Take a snapshot of the existing DB instance. Restore the snapshot with Multi-AZ enabled.
* B. Migrate from Amazon RDS to Amazon Elasticsearch Service (Amazon ES) with Kibana.
* C. Deploy Amazon DynamoDB Accelerator (DAX) in front of the existing DB instance. Modify the game to use DAX.
* D. Deploy an Amazon ElastiCache for Redis cluster in front of the existing DB instance. Modify the game to use Redis.


## Answer
* D. Deploy an Amazon ElastiCache for Redis cluster in front of the existing DB instance. Modify the game to use Redis.



## Explanation
* Why other options are incorrect:
  1. A. Take a snapshot of the existing DB instance. Restore the snapshot with Multi-AZ enabled. 
    * Multi-AZ is a high-availability feature, not a performance-scaling solution.
    * It provides a failover standby instance in a different Availability Zone but does not increase the read or write capacity of the database.
  2. B. Migrate from Amazon RDS to Amazon Elasticsearch Service (Amazon ES) with Kibana. 
    * Amazon Elasticsearch Service is a search and analytics engine, not a primary real-time database for transactional reads and writes like a gaming application requires
    * While it has some geospatial capabilities, it's not the right tool for live, high-frequency updates and simple retrieval of individual player locations.
  3. C. Deploy Amazon DynamoDB Accelerator (DAX) in front of the existing DB instance. Modify the game to use DAX.
    * DAX is an in-memory cache specifically for Amazon DynamoDB. It is not compatible with Amazon RDS for PostgreSQL. Therefore, this solution would not work.


## Thinking
* 題目是需要提升 PostgreSQL DB 的 performance
* Option A 不對的原因是 Multi-AZ enabled 主要是提升 High Availability，確保使用者可以在 Service / DB 掛掉的時候存取相關服務
* Option B 的 Amazon Elasticsearch Service + Kibana 主要是用來進行資料搜索 & 視覺化用，跟題目要求不符
* Option C 不對的原因是 PostgreSQL DB 應該是跟 Amazon Aurora (Relational Database: compatible with mySQL and PostgreSQL) 相容，DynamoDB 是相容 noSQL 
* 因此只剩 Option D
* 請看清楚題目 = =“