# Question 536
A company wants to provide data scientists with near real-time read-only access to the
company's production Amazon RDS for PostgreSQL database. The database is currently
configured as a Single-AZ database. The data scientists use complex queries that will not
affect the production database. The company needs a solution that is highly available.
Which solution will meet these requirements MOST cost-effectively?

A.Scale the existing production database in a maintenance window to provide enough
power for the data scientists.
B.Change the setup from a Single-AZ to a Multi-AZ instance deployment with a larger
secondary standby instance. Provide the data scientists access to the secondary
instance.
C.Change the setup from a Single-AZ to a Multi-AZ instance deployment. Provide two
additional read replicas for the data scientists.
D.Change the setup from a Single-AZ to a Multi-AZ cluster deployment with two readable
standby instances. Provide read endpoints to the data scientists


A. Scale the existing production database
	* Increases cost (larger instance) and risks performance impact on the production system.
	* Does not isolate analytics traffic from production — against best practices.

B. Multi-AZ with a larger secondary standby
	* Multi-AZ standby instances are not readable — they are only used for failover.
	* So, data scientists cannot query the standby, making this ineffective.

D. Multi-AZ cluster with two readable standby instances
	* Sounds like Amazon Aurora, not standard RDS PostgreSQL.
	* If using Aurora, this would work, but it’s more expensive and requires switching engine — not the most cost-effective option.

instance deployment (instance <-> replica (一個 passive standby)) 只建 instance，需要額外成本建立 replica
cluster deployment (instance + replica （多了2個 active standby)) 在建立 cluster 的時候，已經包含 replica了(可以利用 active standby 當作 read replica)，成本比較低