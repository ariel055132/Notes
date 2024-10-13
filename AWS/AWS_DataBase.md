# Database
* Understand relational, NoSQL data storage options, data warehousing with their use cases

# Note
1. Database on EC2
  * Need full control over instance and databas
  * Third-party database engine
2. Amazon RDS
  * Need traditional relational database
  * Data is Well-formed and structured
3. Amazon Dynamo DB
  * NoSQL database
  * In-memory performance
  * High I/O needs
  * Dynamic Scaling
4. Amazon RedShift
   * Data warehouse
5. Amazon ElastiCache
   * Fast temporary storage for small amounts of data
   * In-memory database

## Note
### Relational VS Non-Relational Database
* *Relational* 
  1. Organized by tables, rows and columns
  2. Rigid Schema (SQL)
  3. Rules enforced within database
  4. Typically scaled vertically
  5. Support complex queries and joins
  * E.G: Amazon RDS, Amazon Aurora
* *Non-Relational*
  1. Varied Data storage models
  2. Flexible Schema (NoSQL), data stored in key-value pairs
  3. Rules can be defined in application code
  4. Scaled horizontally
  5. Unstructured, simple language that supports any kind of schema
  * Amazon DynamoDB
### Graph Database
* Store, manage, navigate relationship in data
1. Node
  * Present entities
2. Edge
  * Present relationships
3. Properties
  * Store information about nodes and edges
### Operational / Transactional VS Analytical
* *Operational / Transactional*
  1. Online Transaction Processing (OLTP)
  2. Production DBs that **process transactions**. E.G. adding customer records, checking stock availability
  3. Short transactions and simple queries
* *Analytical*
  1. Online Analytics Processing (OLTP), the source data comes from OLTP DBs
  2. Data warehouse. Typically, separated from the customer facing DBs. For **decision making**.
  3. Long transactions and complex queries
  * E.G: Amazon Redshift, Elastic MapReduce