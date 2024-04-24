# Java lamdba
* Lamdba Expression 為 Java 8 的重大更新。
* 目的是讓程式碼看起來更簡潔，提高執行效能

# lamdba in Java Collection Framework
* 為引入Lamdba Expression，Java 8 新增了 java.util.function 包，

## forEach()
* 方法簽名為：void forEach(Consumer<? super E> action)
* Consumer只是一個function接口，裡面只有一個待實作方法void accept(T t)
* 作用：對Container中的每一個element執行action
```java
// Example: 假設有一個String的List，需要打印出其中長度>3的String
// for loop 實現
ArrayList<String> list = new ArrayList<>(Arrays.asList("I", "love", "you", "too"));
for(String str : list){
    if(str.length()>3)
        System.out.println(str);
}
// lamdba + forEach() 實現
list.forEach( str -> {
        if(str.length()>3)
            System.out.println(str);
});
```

## removeIf()
* 方法簽名為：boolean removeIf(Predicate<? super E> filter)
* Predicate為接口，filter為條件，待實現方法：boolean test(T t)
* 作用：刪除Container中所有滿足filter條件的element
```java
// Example：假設有一個String的List，需要刪除其中所有長度大於3的String
// for Loop + Iterator
ArrayList<String> list = new ArrayList<>(Arrays.asList("I", "love", "you", "too"));
Iterator<String> it = list.iterator();
while (it.hasNext()) {
    if (it.next().length() > 3) {
        it.remove();
    }
}
// removeIf() + lamdba
list.removeIf(str -> str.length() > 3);
```

## replaceAll()
* 方法簽名為：void replaceAll(UnaryOperator<E> operator)
* UnaryOperator為接口，待實現方法：T apply(T t)
* 作用：對每個element執行operator指定的operation，並利用新的操作結果來替換原來的element
```java
// Example: 假設你有一個String List，需要將List中所有長度大於三的element轉換成UpperCase，其他element保持不變
List<String> list = new ArrayList<>(Arrays.asList("I", "Love", "You", "too"));
// for loop
for (int i = 0; i < list.size(); i++) {
    String str = list.get(i);
    if (str.length() > 3) {
        list.set(i, str.toUpperCase());
    }
}
// lamdba
list.replaceAll(str -> {
    if (str.length() > 3) {
        return str.toUpperCase();
    }
    return str;
});
```

# Reference
1. https://objcoding.com/2019/03/04/lambda/#lambda-and-anonymous-classesi