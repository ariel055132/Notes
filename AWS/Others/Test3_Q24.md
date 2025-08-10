# Test 3 - Question 24
## Question 
* A company wants to migrate its MySQL database from on premises to AWS. The company recently experienced a database outage that significantly impacted the business. To ensure this does not happen again, the company wants a reliable database solution on AWS that *minimizes data loss* and *stores every transaction on at least two nodes*.
* Which solution meets these requirements?

## Option
* A. Create an Amazon RDS DB instance with synchronous replication to three nodes in three Availability Zones.
* B. Create an Amazon RDS MySQL DB instance with Multi-AZ functionality enabled to synchronously replicate the data.
* C. Create an Amazon RDS MySQL DB instance and then create a read replica in a separate AWS Region that synchronously replicates the data.
* D. Create an Amazon EC2 instance with a MySQL engine installed that triggers an AWS Lambda function to synchronously replicate the data to an Amazon RDS MySQL DB instance.

## Answer
* B. Create an Amazon RDS MySQL DB instance with Multi-AZ functionality enabled to synchronously replicate the data.

## Explanation
* Why other options are incorrect:
  1. A. Create an Amazon RDS DB instance with synchronous replication to three nodes in three Availability Zones
    * This describes a multi-node cluster, which can be achieved with the Multi-AZ DB cluster option.
    * While this is an excellent solution for high availability and performance, the simpler Multi-AZ single-standby option (Option B) also meets the core requirements of the question by ensuring transactions are stored on at least two nodes.
  2. C. Create an Amazon RDS MySQL DB instance and then create a read replica in a separate AWS Region that synchronously replicates the data
    * *Amazon RDS read replicas use asynchronous replication*.
    * This means that there's a delay (replication lag) between the primary instance and the replica
    * Therefore, this solution does not minimize data loss, as some recent transactions may not have been replicated before an outage occurs
  3. D. Create an Amazon EC2 instance with a MySQL engine installed that triggers an AWS Lambda function to synchronously replicate the data to an Amazon RDS MySQL DB instance
    * It would be a significant administrative burden and would not offer the built-in reliability, durability, and automatic failover capabilities of a fully managed service like Amazon RDS Multi-AZ. 
    * The company would be responsible for building, monitoring, and maintaining the entire replication process, which is prone to error and would likely not be as robust as the AWS-provided solution.

## Thinking
* 先忽略 Option C，首先 Read Replica 的功能是提高 read performane，其次 Read Replica 是 asynchronously transmit
* Option A, Option B 其實看起來都蠻一樣的，只是一個是 3 az, 一個是 2 az, 那選 2 az 就好
* 那時候也不確定為啥會選 Option D，而不選 Option B。。



