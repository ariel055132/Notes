# Java lamdba
* Lamdba Expression 為 Java 8 的重大更新。
* 目的是讓程式碼看起來更簡潔，提高執行效能

# lamdba in Java Collection Framework
* 為引入Lamdba Expression，Java 8 新增了 java.util.function 包，

# Collections的方法
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

## sort()
* 方法簽名為：void sort(Comparator<? super E> c)
* 作用：拖過方法c的比較方法對Container的element進行Sorting，並儲存sorting後的結果
```java
// Example：假設有一個String List，需要按照String中每一個element的長度對List進行排序
// for loop
Collections.sort(list, new Comparator<String>() {
            @Override
            public int compare(String str1, String str2) {
                // 也可以這樣寫：return str1.length() - str2.length();
                return Integer.compare(str1.length(), str2.length());
            }
});
// lamdba
list.sort((str1, str2) -> {
    // list.sort((str1, str2) -> str1.length()-str2.length());
    return Integer.compare(str1.length(), str2.length());
});
```

# Map的方法
## forEach()
* 其實和Collections的forEach()方法差不多，只是Container從List換成Map
```java
// Example：假設有一個key為number，value為char/string的Map，要輸出Map中所有mapping關係
// for loop
Map<Integer, String> map = new HashMap<>();
    map.put(1, "one");
    map.put(2, "two");
    map.put(3, "three");
    // for loop
    for (Map.Entry<Integer, String> entry : map.entrySet()) {
        System.out.println(entry.getKey() + " = " + entry.getValue());
    }
    // lamdba
    list.forEach((k, v) -> System.out.println(k + " = " + v));

```

## getOrDefault(key, default value)
* 方法簽名：V getOrDefault(Object key, V defaultValue)
* 作用：按照給定的Key查詢Map中對應的Value，若沒有找到則return default value
* 與get的差別：get不會處理空值，但getOrDefault會處理空值
```java
// Example: 假設有一個key為number，value為char/string的Map，需要輸出Key值為4的value，若沒有的話，輸出No value
Map<Integer, String> map = new HashMap<>();
map.put(1, "one");
map.put(2, "two");
map.put(3, "three");
// 以往作法：containsKey() + if-else 進行判斷
if (map.containsKey(4)) {
    System.out.println(map.get(4));
} else {
    System.out.println("No Value");
}
// 使用getOrDefault()   
System.out.println(map.getOrDefault(3, "No value")); // three
System.out.println(map.getOrDefault(4, "No value")); // No value
```

## putIfAbsent(key, default value)
* 方法簽名：V putIfAbsent(K key, V value)
* 若map不存在key值，或者key值的mapping 值為null時，將value指定的值放入到Map中，否則不對Map進行修改
* 與Put的相同之處：如果之前沒有添加過相同的key-value，put()和putIfAbsent()兩種方法所return的值均為null
* 與Put的不同：如果以前有添加過相同的key-value，put會用新的value replace調原本的value，並return 原本的value；但putIfAbsent則不會用新的value進行replace。
```java
Map<Integer, String> map = new HashMap<>();
System.out.println(map.put(1, "one")); // null 
System.out.println(map.get(1)); // one

System.out.println();

System.out.println(map.put(1, "one V2")); // one
System.out.println(map.get(1)); // one V2

System.out.println();

System.out.println(map.putIfAbsent(1, "one V3")); // one V2
System.out.println(map.get(1)); // one V2

System.out.println();

System.out.println(map.putIfAbsent(2, "two")); // null
System.out.println(map.get(2)); // two
```

# Stream
* 中間操作 (intermediate operations):
* 結束操作 (terminal operations): 完成中間操作的同時，return stream的最終結果。計算完成後，該stream就會失效。
  * forEach(), **collect()**, count(), reduce()
* 可以透過看method的return value來判斷該method時中間操作，結束操作
  * 若return value為stream，則大多數為中間操作；否則是結束操作

## filter()
* 方法簽名：Stream<T>filter(Predicate<? super T> predicate)
* 目的：return 一個只滿足predicate條件元素的Stream
* 作用：過濾stream中與設定條件相符的元素，並將相關結果組成一個新的stream

# Reference
1. https://objcoding.com/2019/03/04/lambda/#lambda-and-anonymous-classesi
2. https://blog.csdn.net/cnds123321/article/details/113793574
3. https://javarush.com/tw/groups/posts/tw.3974.177java-8--java-stream-