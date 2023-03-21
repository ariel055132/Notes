# 58. Length of the last word

## Content

* Given a string s consisting of words and spaces, return the length of the last word in the string.

```
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
```



## Solution 1: Simulation

1. **Locate the last word** by starting from the end of the string. Iterate the string in reverse order. When we first come across a non-space character, we know that we are at the last character of the last word.
2. Once we locate the last word. Count the length of the last character. Return the length.

*  We can complete the two task within a single loop or multiple loop.



## Code

```java
class Solution {
    public int lengthOfLastWord(String s) {
        int result = 0;
				for (int i = s.length() - 1; i >= 0; i--) {
					if (s.charAt(i) != ' ') {
						result++;
					} else if (s.charAt(i) == ' ' && result != 0) {
						break;
					}
				}
			return result;
    }
}
```

* Time Complexity: O(N), where N is the length of the input string
* Space Complexity: O(1), only a constant memory is consumed to return the answer.