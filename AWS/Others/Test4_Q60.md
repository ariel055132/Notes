# Test 4 - Question 60
## Question
* A company is running a batch application on Amazon EC2 instances. The application consists of a backend with multiple Amazon RDS databases. The application is causing a high number of reads on the databases. A solutions architect must *reduce the number of database reads* while *ensuring high availability*.
* What should the solutions architect do to meet this requirement?

## Option
* A. Add Amazon RDS read replicas.
* B. Use Amazon ElastiCache for Redis.
* C. Use Amazon Route 53 DNS caching.
* D. Use Amazon ElastiCache for Memcached.

## Answer
* B. Use Amazon ElastiCache for Redis.

## Explanation
* While read replicas (option A) would help distribute reads, they still involve database queries. ElastiCache for Redis provides the most dramatic reduction in actual database reads by serving data directly from memory cache, which is exactly what's needed to address the "high number of reads" problem described.
* 題目是需要減少 database 的 read 次數
* 因此 Option A 的 Read Replicas 只是會分散 database 的 read 次數，但其實還是需要 database queries
* Option B 的 ElasticCache 可以直接通過 cache 機制來降低 read 次數