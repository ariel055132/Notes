# Test 3 - Question 28
## Question 
* A company hosts an online shopping application that stores all orders in an Amazon RDS for PostgreSQL Single-AZ DB instance. Management wants to *eliminate single points of failure* and has asked a solutions architect to recommend an approach to *minimize database downtime* without *requiring any changes to the application code*.
* Which solution meets these requirements?

## Option
* A. Convert the existing database instance to a Multi-AZ deployment by modifying the database instance and specifying the Multi-AZ option.
* B. Create a new RDS Multi-AZ deployment. Take a snapshot of the current RDS instance and restore the new Multi-AZ deployment with the snapshot.
* C. Create a read-only replica of the PostgreSQL database in another Availability Zone. Use Amazon Route 53 weighted record sets to distribute requests across the databases.
* D. Place the RDS for PostgreSQL database in an Amazon EC2 Auto Scaling group with a minimum group size of two. Use Amazon Route 53 weighted record sets to distribute requests across instances.



## Answer
* A. Convert the existing database instance to a Multi-AZ deployment by modifying the database instance and specifying the Multi-AZ option.

## Explanation
* Why other options are incorrect:
  * B. Create a new RDS Multi-AZ deployment. Take a snapshot of the current RDS instance and restore the new Multi-AZ deployment with the snapshot.
  * This is a valid way to create a Multi-AZ deployment, but it is more complicated than simply modifying the existing instance.
  * Modifying an existing Single-AZ instance to Multi-AZ is a built-in feature of Amazon RDS that automates this entire process.

## Thinking
* 題目提到的 eliminate single points of failure (SPOF)，基本上就是指出要提升 Availability
* 然後 Option C 和 Option D 基本上與 SPOF 不相關
* Read Replica 使用異步資料複製，有可能會導致資料缺失 (Option C)
* Option D 不對的原因是 RDS for PostgreSQL 無法放到 EC2 Auto Scaling group
* 所以只剩 Option B, Option A
* 忘記了 RDS 可以直接編輯原來的 instance 實現 multi-AZ deployment