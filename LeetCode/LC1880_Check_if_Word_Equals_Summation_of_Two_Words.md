# 1880. Check if Word Equals Summation of Two Words

## Content

* The **letter value** of a letter is its position in the alphabet **starting from 0**. For example, 'a' -> 0, 'b' -> 1, 'c' -> 2, etc.
* The **numerical value** of some string of lowercase English letters s is the **concatenation** of the **letter values** of each letter in s, which is then **converted** into an integer.
* For example, if s = "acb", we concatenate each letter's letter value, resulting in "021". After converting it, we get 21.
* You are given three strings firstWord, secondWord, and targetWord, each consisting of lowercase English letters 'a' through 'j' **inclusive**.
* Return **true** if the **summation** of the **numerical values** of firstWord and secondWord equals the **numerical value** of targetWord, or false otherwise.



```
Input: firstWord = "acb", secondWord = "cba", targetWord = "cdb"
Output: true
Explanation:
The numerical value of firstWord is "acb" -> "021" -> 21.
The numerical value of secondWord is "cba" -> "210" -> 210.
The numerical value of targetWord is "cdb" -> "231" -> 231.
We return true because 21 + 210 == 231.
```

```
Input: firstWord = "aaa", secondWord = "a", targetWord = "aab"
Output: false
Explanation: 
The numerical value of firstWord is "aaa" -> "000" -> 0.
The numerical value of secondWord is "a" -> "0" -> 0.
The numerical value of targetWord is "aab" -> "001" -> 1.
We return false because 0 + 0 != 1.
```

```
Input: firstWord = "aaa", secondWord = "a", targetWord = "aaaa"
Output: true
Explanation: 
The numerical value of firstWord is "aaa" -> "000" -> 0.
The numerical value of secondWord is "a" -> "0" -> 0.
The numerical value of targetWord is "aaaa" -> "0000" -> 0.
We return true because 0 + 0 == 0.
```



## Solution: Simulation

1. Convert each character of each word to its numerical value.
   * HashMap, for loop
2. Check if the numerical values satifies the condition.



## Code

```java
static HashMap<Character, Character> hashMap = new HashMap<Character, Character>();

    static {
        hashMap.put('a', '0');
        hashMap.put('b', '1');
        hashMap.put('c', '2');
        hashMap.put('d', '3');
        hashMap.put('e', '4');
        hashMap.put('f', '5');
        hashMap.put('g', '6');
        hashMap.put('h', '7');
        hashMap.put('i', '8');
        hashMap.put('j', '9');
    }

    public boolean isSumEqual(String firstWord, String secondWord, String targetWord) {
        return getLetterValue(firstWord) + getLetterValue(secondWord) == getLetterValue(targetWord);
    }

    public int getLetterValue(String s) {
        int result = 0;
        String str = "";
        StringBuilder tmp = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            tmp.append(hashMap.get(s.charAt(i)));
        }
        str = tmp.toString();
        result = Integer.parseInt(str);
        return result;
    }
```

