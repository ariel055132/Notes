# 149. Max Points on a Line

## Content

* Given an array of `points` where `points[i] = [xi, yi]` represents a point on the **X-Y** plane, return *the maximum number of points that lie on the same straight line*.

```
Input: points = [[1,1],[2,2],[3,3]]
Output: 3
```

```
Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
```



## Solution 1: Simulation

* Simulate with the example input, you can observe that when the points lie on the same straight line, it means that the slope between these points are the same.
* The formula of calculate the slope = (y2 - y1) / (x2 - x1)
* For example
  * Slope between (1, 1) and (2, 2): (2 - 1) / (2 - 1) = 1
  * Slope between (1, 1) and (3, 3): (3 - 1) / (3 - 1) = 1
  * Slope between (2, 2) and (3, 3): (3 - 2) / (3 - 2) = 1

* Therefore, we can calculate the slope of each coordinates. Then find the maximum number of times some slope occurs among the calculated values



1. Iterate over all points. Let the current point be points[i]. Maintain a hashmap cnt to count the slopes.
   * For each *j*/=*i* calculate the slope of the vector points[j] - points[i] and add this value to the hashmap (cnt).
   * Let result be the maximum number of occurences of some slope value in the hashmap.
   * Update the answer with result + 1. (+1 because the points also lies on the line)

```java
class Solution149 {
    public int maxPoints(int[][] points) {
        if (points.length == 1) {
            return 1;
        }
        int result = 0;

        for (int i = 0; i < points.length; i++) {
            Map<Double, Integer> map = new HashMap<>();
            for (int j = i + 1; j < points.length; j++) {
                double slope = calculateSlope(points[i], points[j]);

                if (map.containsKey(slope)) {
                    int count = map.get(slope);
                    map.put(slope, ++count);
                } else {
                    map.put(slope, 1);
                }

                result = Math.max(result, map.get(slope));
            }
        }
        return result + 1;
    }

    private double calculateSlope(int[] pt1, int[] pt2) {
        int x1 = pt1[0], x2 = pt2[0];
        int y1 = pt1[1], y2 = pt2[1];
        // Vertical line --> inf. slope
        if (x1 == x2) {
            return Double.MAX_VALUE;
        }
        // Horizontal line --> slope == 0
        if (y1 == y2) {
            return 0;
        }
        // Normal Case --> Calculate the slope with formula (y2 - y1) / (x2 - x1)
        return (double) (y2 - y1) / (double) (x2 - x1);
    }
}
```

