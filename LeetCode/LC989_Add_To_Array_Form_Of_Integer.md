# 989. Add To Array Form Of Integer

# Content

* The **array-form** of an integer num is an array representing its digits in left to right order.
* For example, for `num = 1321`, the array form is `[1,3,2,1]`.

* Given `num`, the **array-form** of an integer, and an integer `k`, return *the **array-form** of the integer* `num + k`.

```text
Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
```

```
Input: num = [2,7,4], k = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455
```

```
Input: num = [2,1,5], k = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021
```



## Solution

* Add the number in a schoolbook way, column by column (digit by digit).
* For example, to add 274 and 181, we add 4+1, then 7+8, then 2+1. 
* When our addition result is more than 10, we need to add the carry 1 into the next column. The result is 455.
* Time Complexity: O(max(N, log K)), where N is the length of A
* Space Complexity: O(max(N, log K))

```java
public static List<Integer> addToArrayForm(int[] num, int k) {
		List<Integer> result = new ArrayList<>();
  	// add the results from the digit
		for (int i = num.length - 1; i >= 0; i--) {
			int sum = num[i] + k;
			int remainder = sum % 10;
			k = sum /= 10;
			result.add(remainder);
		}
  	// When the addition result is more than 10, carry the 1 into the next column
		while (k > 0) {
			result.add(k%10);
			k /= 10;
		}
		Collections.reverse(result);
		return result;
	}
```

 