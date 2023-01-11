# 2244. Minimum Rounds to Complete All Tasks

## Content

* You are given a **0-indexed** integer array `tasks`, where `tasks[i]` represents the difficulty level of a task. In each round, you can complete either 2 or 3 tasks of the **same difficulty level**.
* Return *the **minimum** rounds required to complete all the tasks, or* `-1` *if it is not possible to complete all the tasks.*



```
Input: tasks = [2,2,3,3,2,4,4,4,4,4]
Output: 4
Explanation: To complete all the tasks, a possible plan is:
- In the first round, you complete 3 tasks of difficulty level 2. 
- In the second round, you complete 2 tasks of difficulty level 3. 
- In the third round, you complete 3 tasks of difficulty level 4. 
- In the fourth round, you complete 2 tasks of difficulty level 4.  
It can be shown that all the tasks cannot be completed in fewer than 4 rounds, so the answer is 4.
```

```
Input: tasks = [2,3,3]
Output: -1
Explanation: There is only 1 task of difficulty level 2, but in each round, you can only complete either 2 or 3 tasks of the same difficulty level. Hence, you cannot complete all the tasks, and the answer is -1.
```



## Solution 1: Counting

* The question shows that we are given N integers, we can group them with size two or three. We need to find out whether it is possible to group with them. If we can, what is the minimum number of groups needed.
* We cannot group the integer with frequency 1 as the minumum size of the group is 2. Return -1 when we face this situation.
* To find the minimum number of groups for other integers, we can divide the integer into three groups.
  * For the cases Integers that are multiples of 3 (e.g: 3, 6, 9...), we can group with them with size of three directly, it results to **rounds/3**.
  * For the cases Integers that leaves remainder of 1 after divide by 3 (e.g: 4, 7, 10...), we need an extra round to group all of them, it results to **rounds/3 + 1**. (How to group: 2 + 2)
  * For the cases Integers that leaves remainder of 2 after divide by 3 (e.g: 5, 8, 11...), we also need an extra round to group all of them, it also results to **rounds/3 + 1**. (How to group: 3 + 2)
* Sum up the rounds the steps above to find the minimum round.



## Steps

1. Iterate over the integers in the array **tasks**, store the frequency of each integers in the map/hashmap **freq**.
2. Initialize the answer variable **result** to 0.
3. Iterate over the frequencies in the hashmap/map **freq** with its frequency **count**: 
   * If count equals to 1, we need to stop the iteration, return **-1**.
   * If count is divisible by 3, we need to add **count/3** to the answer variable.
   * Otherwise, add **count/3 + 1** to the answer variable.
4. Return the answer variable.



```java
class Solution2244 {
    public int minimumRounds(int[] tasks) {
        Map<Integer, Integer> map = new HashMap<>();
        // Iterate over the integer in the array, and store the corresponding result in a map
        for (int task : tasks) {
            if (map.containsKey(task)) {
                int count = map.get(task);
                map.put(task, ++count);
            } else {
                map.put(task, 1);
            }
        }

        int result = 0;

        for (int count : map.values()) {
            if (count == 1) {
                return -1;
            }
            if (count % 3 == 0) {
                result += count / 3;
            } else {
                result += count / 3 + 1;
            }
        }
        return result;
    }
}
```

