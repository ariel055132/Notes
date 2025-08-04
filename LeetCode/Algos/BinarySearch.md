# Binary Search
## What is Binary Search?
* Reduce the search space by half at each step
* Input usually needs to be **sorted**
* ![Binary Search Visualization](../Src/BinarySearchExample.png)
## Why Binary Search?
* Fast
* Time Complexity: T(n) = T(n/2) + O(eval)
  * T(n/2): reduce the search space by half
  * O(eval): determine the value is needed or not
* O(log(range)) * O(eval) (Binary Search) vs (linear scan) O(range) * O(eval) 
* When the number range is greater than 10^7, consider using Binary Search

## Template
1. [left, right)
* Time complexity: O(log(right - left)*(f(m) + g(m)))
* Space complexity: O(1)
```python
def binary_search(left, right):
    while left < right:
        # The middle index
        mid = left + (right - left) // 2
        if f(mid): 
            # Find the value you needed, do something below (Optional)
            return mid
        if g(mid):
            # If the value is less than mid, set the new range as [left, mid)
            right = mid
        else:
            # Otherwise (the value is greater than mid), set the new range as [mid + 1, right)
            left = mid + 1
    # Not found the value needed
    return left 
```

2. 