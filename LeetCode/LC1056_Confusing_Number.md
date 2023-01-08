# 1056. Confusing Number

## Content

* A **confusing number** is a number that when rotated `180` degrees becomes a different number with **each digit valid**.
* We can rotate digits of a number by `180` degrees to form new digits.
  * When `0`, `1`, `6`, `8`, and `9` are rotated `180` degrees, they become `0`, `1`, `9`, `8`, and `6` respectively.
  * When `2`, `3`, `4`, `5`, and `7` are rotated `180` degrees, they become **invalid**.
* Note that after rotating a number, we can ignore leading zeros.
  * For example, after rotating `8000`, we have `0008` which is considered as just `8`.
* Given an integer `n`, return `true` *if it is a **confusing number**, or* `false` *otherwise*.



## Solution 1: Simulation 

* By looking the example, we can notice that after rotating the string, each digit and positions of the whole digits are reversed.
* For example, the first digit of the input number is inverted and moved to the last digit.



* Therefore, we can split the process into following steps.
  1. Initialize a hashmap(map) that converts each valid digit to its inverted digit. Create an empty string(tmpString) to save the inverted numbers.
  2. Iterate over each digit of input number. If digit is not in the hashmap(map), return false. Otherwise, find the inverted digit and append it to the end of the string(tmpString). 
  3. Reverse tmpString.
  4. Check if tmpString equals the string representation of n, return true if not. 

```java
class Solution1056 {
    public boolean confusingNumber(int n) {
        Map<Character, Character> map = new HashMap();
        map.put('0', '0');
        map.put('1', '1');
        map.put('6', '9');
        map.put('8', '8');
        map.put('9', '6');
        String strN = Integer.toString(n);
        char[] charN = strN.toCharArray();
        StringBuilder sb = new StringBuilder();
        for (char c : charN) {
            if (!map.containsKey(c)) {
                return false;
            } else {
                sb.append(map.get(c));
            }
        }
        sb.reverse();
        return Integer.parseInt(sb.toString()) != n;
    }
}
```

