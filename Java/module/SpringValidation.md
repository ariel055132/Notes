# Spring Boot Validation
* 參數驗證機制
* 檢查API的請求參數是否合法，沒有問題，才不會有預期外的資料出現，導致系統發生不可預期的結果

## 安裝方式
```
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-validation</artifactId>
</dependency>
```

## 如何使用
1. 定義
2. 在欄位加上 Annotation

## 常用 Annotation
| Annotation     | Content  |
|---             |---       |
|@NotNull        | 不能為 null，空白無法阻擋，故用在非 String 的欄位比較好 (E.G. List, Set...)|
|@Null           | 必須為 null |
|@Size(min,max)  | 限制欄位長度 (可用在 String, List...)   |
|@NotBlank       | 必須為**字串**，且含有至少一個非空白 char，不得為null          |
|@Digits(integer,fraction) | 必須為**數字**，指定數字位數的最大長度，integer代表整數部分   | 
|@Negative / @Positive | 必須為**數字**，指定負或正值 (不接受0)      | 
|@NegativeOrZero / @PositiveOrZero | 必須為**數字**，指定負或正值 (接受0)   |
|@Future / @Past  | **日期/時間**類型，必須為未來/過去的時間        |
|@FutureOrPresent / @PastOrPresent | **日期/時間**類型，必須為未來/過去 或當下的時間       |

## 自定義Validation
* SpringValidation 能做的 Validation
1. 建立 Annotation
   ```java

   ```
2. 建立 Validator
3. 在對應欄位使用 Annotation
4. 啟動 Validator