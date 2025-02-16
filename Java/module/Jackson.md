# Java Jackson
## What is Jackson? (From GPT)
* Jackson is a popular Java library used for *converting Java objects to JSON (JavaScript Object Notation) and vice versa*.
* It's widely used for handling JSON in Java applications due to its performance and ease of use.
* Jackson provides a set of tools for parsing and generating JSON content, making it ideal for both RESTful APIs and other JSON-related operations in Java.

## Jackson Modules
1. Jackson-core: Streaming
2. Jackson-annotation: Annotation
3. Jackson-databind: Desearialize and searialize support

## ObjectMapper
* Json 轉換工具，完成 Json 和 Java 的 Object 的互相轉換
* Serialize: Java Object 轉換為 Json
* Deserialize: Json 轉換成 Java Object

### 轉換例子
```java
/**
 * 定義 Entity 
 */
@Data // Getter, Setter, Constructor
@AllArgsConstructor 
@NoArgsConstructor // important!!
public class User {
	private int id;
	private String 
}

/**
 * Test 1: Java Object 與 Json 之間的轉換 
 * Test 2: List<Object> 轉為 Json
 * Test 3: Map<String, Object> 轉為 Json
 */
public class CarJsonTest {
    @Test
    @DisplayName("Test 1")
    public void test1() throws IOException {
        // Java Object to Json
        ObjectMapper objectMapper = new ObjectMapper();
        Car car1 = new Car("yellow", "renault");
        String json = objectMapper.writeValueAsString(car1);
        System.out.println(json);
        objectMapper.writeValue(new File("target/car.json"), car1);

        // Json to Java Object
        Car car2 = objectMapper.readValue(json, Car.class);
        System.out.println(car2.toString());
        System.out.println(car2.getType());
        System.out.println(car2.getColor());
    }  

    @Test
    @DisplayName("Test 2")
    public void test2() throws IOException {
        ObjectMapper objectMapper = new ObjectMapper();

        // List<Car> to Json
        List<Car> ulist = new ArrayList<>();
        Car car3 = new Car("red", "audi");
        ulist.add(car3);
        String jsonList = objectMapper.writeValueAsString(ulist);
        System.out.println(jsonList);
    }

    @Test
    @DisplayName("Test 3")
    public void test3() throws IOException {
        ObjectMapper objectMapper = new ObjectMapper();

        // Map<String, Car> to Json
        HashMap<String, Car> umap = new HashMap<>();
        Car car4 = new Car("blue", "bmw");
        umap.put("car4", car4);
        String mjson2 = objectMapper.writeValueAsString(umap);
        System.out.println(mjson2);

        // Json to Map<String, Car>
        Map<String, Car> map = objectMapper.readValue(mjson2, new TypeReference<Map<String, Car>>() {});
        System.out.println(map.get("car4").toString());
    }
}
```
* 若 Entity 沒有加 @NoArgsConstructor ，會導致 Error: **com.fasterxml.jackson.databind.exc.InvalidDefinitionException: Cannot construct instance of 'XXX'**
* 若 Entity 上同時使用了 @Data 和 @AllArgsConstructor Annotation，@AllArgsConstructor 會阻止 @Data 產生 無參數 的 Constructor，導致 Entity 只有全部參數的 Constructor，沒有無參數的 Constructor，導致 Deserialize 失敗

### 注意事項
* 執行 ObjectMapper 是非常可怕的事情，在面對 High Concurrency 的情況下，會造成性能瓶頸，官方方法：不要每次都new，盡量共用
1. 宣告變數
* 若不需要任何的 Config，直接使用 Spring default 好的 ObjectMapper 即可
```java
@Service
public class MyService {

	// Constructor Based Dependency Injection
    private final ObjectMapper objectMapper;
    
    @Autowired
    public MyService(ObjectMapper objectMapper) {
        this.objectMapper = objectMapper;
    }

    public String toJson(Something something) throws JsonProcessingException {
        return objectMapper.writeValueAsString(something);
    }
}
```
2. @Configuration
* 如果你需要全域設定，或是有多個不同設定的 ObjectMapper，建議使用此方法，並且注入時要用 @Qualifier，否則將會注入預設的 ObjectMapper Bean。
```java
@Configuration
public class JacksonConfiguration {

    @Bean("customObjectMapper")
    public ObjectMapper customObjectMapper() {
        return new ObjectMapper()
            .configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false)
            .configure(DeserializationFeature.FAIL_ON_INVALID_SUBTYPE, false);
    }

}
```

3. 包裝成 Utils
* 全域的 Class 若需要使用 Json 進行操作，直接Call Utils，確保都只有一個 utils 被使用
