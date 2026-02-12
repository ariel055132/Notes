# Redis

## What is Redis?
* 一個高效的 key-value Database，主要用於 Caching，Session Management，Pub/Sub 等等。

## Key-Value Database
* 一種 NoSQL Database，儲存方式類似 Dictionary 或 Hash Table。
* 代表每一筆資料都有一個 unique 的 Key，對應到一個 Value。
* 這種類型的 Database 通常用於需要快速存取資料的場景

## Redis 基本操作
1. 存放資料
```java
語法：SET key value
SET user:1001 '{"name": "Alice", "age": 25, "email": "alice@example.com"}'
放入一筆資料，key 為 user:1001，value 為 {"name": "Alice", "age": 25, "email": "alice@example.com"}
```
2. 取得資料
```java
語法：GET key
GET user:1001
取得 key 為 user:1001 的資料 ({"name": "Alice", "age": 25, "email": "alice@example.com"})
```

## 常見的 Key-Value 資料庫
1. Redis
2. Amazon DynamoDB
3. Etcd
4. Memcached
* 通常 Redis 會常常和 Memcached 比較

## Redis + Java
```java

```