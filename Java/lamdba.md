# Java lamdba
* Lamdba Expression 為 Java 8 的重大更新。
* 目的是讓程式碼看起來更簡潔，提高執行效能

# lamdba in Java Collection Framework
* 為引入Lamdba Expression，Java 8 新增了 java.util.function 包，

## forEach
* 方法簽名為：void forEach(Consumer<? super E> action)
* Consumer只是一個function接口，裡面只有一個待實作方法void accept(T t)
* 作用：對Container中的每一個element執行action
```java
Example: 假設有一個String的List，需要打印出其中長度>3的String
// for loop
ArrayList<String> list = new ArrayList<>(Arrays.asList("I", "love", "you", "too"));
for(String str : list){
    if(str.length()>3)
        System.out.println(str);
}
// lamdba + forEach()
list.forEach( str -> {
        if(str.length()>3)
            System.out.println(str);
});
```
