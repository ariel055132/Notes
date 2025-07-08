# Question 540
## Question

C. is chose
Amazon RDS Multi-AZ Cluster (not just traditional Multi-AZ) supports read scaling by providing readable standby instances, including a reader endpoint.
	•	This provides:
	•	High availability (automated failover between AZs)
	•	Improved performance (read queries go to reader instance, not primary)
	•	Operational efficiency (no custom replication setup)
	•	Reporting queries can use the reader instance, offloading the primary instance.

A. DMS + Multi-region RDS
    * AWS DMS is good for initial migrations and ongoing replication, but managing multiple RDS instances across regions adds operational complexity.
	* Not the most efficient setup for this use case.

B. RDS Single-AZ + read replica in same AZ
	* Single-AZ lacks high availability.
	* You can’t create read replicas in the same AZ — they are placed in different AZs for fault tolerance.
	* RDS Oracle read replicas are only supported with Oracle Enterprise Edition and limited use cases.

D. Multi-AZ RDS instance + Aurora
	* Aurora is not a drop-in replacement for Oracle without application and schema changes.
	* Would require migrating from Oracle to Aurora, which may involve high migration cost and effort.
	* Also, Aurora is not available in standard RDS Oracle configurations.