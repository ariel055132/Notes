# Dynamo DB
* Fully managed NoSQL database service, Serverless
* Key/value store and document store (no schema)
* Non-relational, key-value type of database
* Fully serverless service
* Push button scaling

## Feature
1. Serverless
2. Highly available
3. NoSQL type of database with Name / Value structure
4. Horizontal scaling
5. DynamoDB stream
6. DynamoDB Accelerator (DAX)
7. Transaction Options
8. Backup 
9. Global Tables

## DynamoDB Time to Live (TTL)
* Enables a per-item timestamp to determine when an item is no longer needed
* After the data and time of the specified timestamp, DB deletes the item from the table without consuming any write throughput
* Good: Help reduce storage and manage the table size over time

## Primary Keys
1. *Partition Key* (aka. Hash key)
   * Simple primary key, composed of one attribute
   * Used as input to an internal hash function; the output from the hash function determines the partition where the item will be stored (使用Partition Key來計算資料存放節點)
   * No two items in a table can have the same partition key value. (otherwise, collision is happen)
2. *Partition Key and Sory Key* (aka. Hash and Range Key)
   * Sorted by sort key value

## DynamoDB Streams
* Capture a **time-ordered** sequence of **item-level changes** made to a data in a table and store this information in a log for up to **24 hours**
1. KEYS_ONLY - Key attributes of the modified item
2. NEW_IMAGE - Entire item, after it was modified (~updated data)
3. OLD_IMAGE - Entire item, before it was modified (~original data)
4. NEW_AND_OLD_IMAGE - Both NEW_IMAGE and OLD_IMAGE