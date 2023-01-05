# 997 Find the Town Judge

* In town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the judge.
* If the town judge exists, then
  1. The town judge trusts nobody.
  2. Everybody (except for the town judge) trusts the town judge
  3. There is exactly one person that satisifed propertities 1 and 2
* You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the people labeled bi.
* Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

```
Input: n = 2, trust = [[1,2]]
Output: 2
```

```
Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
```



## Solution 1: Two Arrays

* We can convert the input array trust as a graph with two arrays, in-degree and out-degree.
  * Outdegree: The number of directed edges going out of it --> represents the number of other people that trust the same person.
  * Indegree: The number of directed edges going into it --> Represents the number of people trusted by that person.

* Calculate the in-degree and out-degree by traversal the array trust
* Loop over the people (numbered from 1 to n) and check whether or not they meet the town judge criteria

```java
class Solution997 {
    public int findJudge(int n, int[][] trust) {
        if (trust.length < n - 1) {
            return -1;
        }
        int[] count = new int[n + 1];
        for (int[] relation : trust) {
            count[relation[0]]--;
            count[relation[1]]++;
        }

        // i = 1 because people labeled from 1 to n
        for (int i = 1; i <= n; i++) {
            if (count[i] == n - 1) {
                return i;
            }
        }
        return -1;
    }
}
```

