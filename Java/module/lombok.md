# LomBok
* 一個 Java library
* 可以透過簡單的注解省略 Java 的 code，像是 setter、getter、logger…等
* 目的在消除冗長的 code 和提高開發效率

## Install Lombok
```
<!-- https://mvnrepository.com/artifact/org.projectlombok/lombok -->
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <version>1.18.34</version>
    <scope>provided</scope>
</dependency>
```
* Remember to enable Annotation Processing before execute programs

## Basic Annotation
### @Getter
* 自動生成 Getter 方法
### @Setter
* 自動生成 Setter 方法
### @AllArgsConstructor
* 自動生成 class 中所有欄位的 constructor
### @NoArgsConstructor
* 生成一個空欄位的 constructor
* 若 class 中有 param 是 final，不能使用 @NoArgsConstructor，除非使用 @NoArgsConstructor (force = true)
### @ToString
* 生成 class 中的param ToString method
### @EqualsAndHashCode
* 生成 Equals 的方法與 HashCode 計算
### @Builder
* 生成 builder 設計模式
* 處理多個 parm 生成情況
* 幹掉 NoArgsConstructor...

## Note
* Why Lombok can generate the codes with Annotation?
    * Java Compile Steps:
    1. Parse and Enter (所有文件會被Parse成語法樹)
    2. Annotation Processing (使用Annotaion處理器，對語法樹進行處理，若在處理途中產生新的文件，新的文件也會被 Compile)
    3. Analyze and Generate (Syntax Tree會被分析稱java class) 