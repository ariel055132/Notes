# Spring Security 

## 什麼是 Spring Security
* 全面，高度可定製的安全框架
* 執行 Authentication (身分驗證)，Authorization (認證授權)
  * Authentication: 確保用戶身分
  * Authorization: 確保用戶有足夠的權限進行Resource的訪問

## Pom 設定
```java
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
<dependencies>
```
* 加了以上的 dependencies 後，啟 Application，打 localhost:8080 會自動跳轉到登入畫面
* Username: user
* Password: Console Search Using generated security password: 