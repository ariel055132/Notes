# 66. Plus One

## Content

* You are given a **large integer** represented as an integer array `digits`, where each `digits[i]` is the `ith` digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading `0`'s.
* Increment the large integer by one and return *the resulting array of digits*.



```
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
```

```
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
```

```
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
```



## Solution 1: Simulation

1. Move along the input array starting from the end of array.
2. Set all the nines at the end of array to zero.
3. If we meet a non-nine digit, we would increase it by one. The job is done - return digits.
4. We are here because all the digits were equal to nine. Now they have all been set to zero. We then append the digit 1 in front of the other digits and return the result.



## Code

```java
public int[] plusOne(int[] digits) {
        for (int i = digits.length - 1; i >= 0; i--) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }
            digits[i] = 0;
        }
        digits = new int[digits.length + 1];
        digits[0] = 1;
        return digits;
    }
```

* Let N be the number of elements in the input list (aka length of the list)
* Time Complexity: O(N), since we need one loop along the input list
* Space Complexity: O(N), we need the length of the whole list to save the answer.