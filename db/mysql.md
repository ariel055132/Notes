# MySQL 注意事項
* 在 application.properties 中設定的一些功能

## spring.jpa.hibernate.naming.physical-strategy=org.hibernate.boot.model.naming.PhysicalNamingStrategyStandardImpl 
```txt
// 確保JPA 找 Table 的時候不會進行 uppercase / lowercase 轉換，只根據 @Table 中定義的 name 進行查找
spring.jpa.hibernate.naming.physical-strategy=org.hibernate.boot.model.naming.PhysicalNamingStrategyStandardImpl
```
* *org.hibernate.boot.model.naming.PhysicalNamingStrategyStandardImpl* tells Hibernate not to change anything:
    * @Entity(name = "CustomerAccount") → table: CustomerAccount
    * @Column(name = "accountNumber") → column: accountNumber
	* If annotations are missing, Hibernate uses the Java name as-is.
	* No transformation like camelCase to snake_case.

## spring.jpa.hibernate.ddl-auto=update
```txt
// 確保 JPA 會自動根據 Table 目前的 Schema 進行 update
spring.jpa.hibernate.ddl-auto=update
```
* When you set *ddl-auto=update*, Hibernate compares your entity model with the current database schema and:
  1. Creates new tables if they don’t exist.
  2. Adds new columns to existing tables.
  3. Alters columns if their types have changed (limited support).
  4. Does NOT delete unused columns or drop tables.
* It can be used in local development, unit testing, but not in production:
  1. Local development -> convenient
  2. Unit testing -> fast schema setup
  3. Production -> risky (may cause unintended changes or failures)
