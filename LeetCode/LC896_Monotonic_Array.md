# 896. Monotonic Array

## Content

* An array is **monotonic** if it is either monotone increasing or monotone decreasing.
* An array `nums` is **monotone increasing** if for all `i <= j`, `nums[i] <= nums[j]`.
* An array `nums` is **monotone decreasing** if for all `i <= j`, `nums[i] >= nums[j]`.
* Given an integer array `nums`, return `true` *if the given array is monotonic, or* `false` *otherwise*.

```text
Input: nums = [1,2,2,3] 
Output: true --> monotonic increasing
```

```
Input: nums = [6,5,4,4]
Output: true --> monotonic decreasing
```

```
Input: nums = [1,3,2]
Output: false 
```



## Solution

* Check the adjacent elements in the array to determine if the array is monotone increasing or decreasing.
* To check whether the array A is monotone increasing / decreasing, just check A[i] <= A[i+1] / A[i] >= A[i+1] for all i with 1 or 2 **for loop**.



# Two Pass Solution (Steps)

* Traverse two times with for loop to check monotone increasing or monotone decreasing respectively
* Time Complexity: O(N), where N is the length of the array
* Space Complexity: O(1)

```java
class Solution {
    public boolean isMonotonic(int[] nums) {
        public boolean isMonotonic(int[] A) {
        return increasing(A) || decreasing(A);
    }

    public boolean increasing(int[] A) {
        for (int i = 0; i < A.length - 1; ++i)
            if (A[i] > A[i+1]) return false;
        return true;
    }

    public boolean decreasing(int[] A) {
        for (int i = 0; i < A.length - 1; ++i)
            if (A[i] < A[i+1]) return false;
        return true;
    }
}
```



# One Pass Solution (Steps)

* Traverse the array with one times and check whether it is monotonic increasing or monotone decreasing (with the definition in the question)
* Time Complexity and Space Complexity are the same as the above

```java
class Solution {
    public boolean isMonotonic(int[] nums) {
        boolean isIncrease = true;
        boolean isDecrease = true;
        for (int index = 1; index < nums.length; index++) {
            if (nums[index] > nums[index-1]) {
                isDecrease = false;
            } if (nums[index] < nums[index-1]) {
                isIncrease = false;
            } if (!isDecrease && !isIncrease) {
                return false;
            }
        }
        return true;
    }
}
```

