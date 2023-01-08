# 347. Top K Frequent Elements

## Content

* Given an integer array `nums` and an integer `k`, return *the* `k` *most frequent elements*. You may return the answer in **any order**.

```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

```
Input: nums = [1], k = 1
Output: [1]
```



## Solution 1: HashMap

1. Build a hashmap to count the frequencies of each number in array nums
2. Sort the hashmap from the keyset of hashmap by the value of number
3. Transfer results from list to integer array.

```java
class Solution347 {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new TreeMap<>();
        for (int num : nums) {
            if (map.containsKey(num) == false) {
                map.put(num, 1);
            } else {
                int count = map.get(num);
                map.put(num, ++count);
            }
        }
        List<Integer> list = new ArrayList<>(map.keySet());
        Collections.sort(list, (a, b) -> map.get(b) - map.get(a));
        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = list.get(i);
        }


        return result;
    }
}
```

