# Test 3 - Question 8
## Question
* A company is developing a chat application that will be deployed on AWS. The application stores the messages by using a *key-value data model*. Groups of users typically read the messages multiple times. A solutions architect must select a database solution that will *scale for a high rate of reads* and will *deliver messages with microsecond latency*.
* Which database solution will meet these requirements?


## Option
* A. Amazon Aurora with Aurora Replicas
* B. Amazon DynamoDB with DynamoDB Accelerator (DAX)
* C. Amazon Aurora with Amazon ElastiCache for Memcached
* D. Amazon Neptune with Amazon ElastiCache for Memcached


## Answer
* B. Amazon DynamoDB with DynamoDB Accelerator (DAX)

## Thinking
* 那時候忽略了為 key-value data model，需要 noSQL 類型的
* Option A, C 的 Aurora 為 relational data base model，並非 key-value 
* Option D 的 Neptune 是 graph database
* 所以只剩 Option B