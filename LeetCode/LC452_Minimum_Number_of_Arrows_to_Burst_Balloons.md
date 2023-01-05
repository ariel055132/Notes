# 452. Minimum Number of Arrows to Burst Balloons

* There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array `points` where `points[i] = [xstart, xend]` denotes a balloon whose **horizontal diameter** stretches between `xstart` and `xend`. You do not know the exact y-coordinates of the balloons.
* Arrows can be shot up **directly vertically** (in the positive y-direction) from different points along the x-axis. A balloon with `xstart` and `xend` is **burst** by an arrow shot at `x` if `xstart <= x <= xend`. There is **no limit** to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.
* Given the array `points`, return *the **minimum** number of arrows that must be shot to burst all balloons*.

```
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
```

```
Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.
```

```
Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].
```



## Solution 1: Greedy

* We know that eventually we have to shoot down every balloon, so for each ballon there must be an arrow whose position is between **balloon[0]** and **balloon[1]** inclusively. Given that, we can sort the array of balloons by their **ending position**. Then we make sure that **while we take care of each balloon in order, we can shoot as many following balloons as possible.**

1. Sort the array with ending positions.
2. Check how many balloons user can shoot down with one shot aiming at the position of the current balloon.
3. Skip all of these balloons and start again from the next one that needs another arrow.

```java
public int findMinArrowShots(int[][] points) {
        if (points.length == 0) {
            return 0;
        }
  			// 1. Sort the array with ending positions
        Arrays.sort(points, (a, b) -> Integer.compare(a[1], b[1]));
				
  			// (Optional) Print the sorted 2D array to check whether the sorting is succeed.
        for (int[] point : points) {
            for (int coord : point) {
                System.out.print(coord + " ");
            }
            System.out.println();
        }
				
  			// 2. Set the arrowPosition, check how many balloons user can shot down with one shot.
        int arrowPosition = points[0][1];
        int result = 1; // One arrow is needed to brust all balloons
        for (int i = 0; i < points.length; i++) {
          	// Skip the balloons that can shot down with one shot
            if (arrowPosition >= points[i][0]) {
                continue;
            }
          	// Start again from the next one that needs another arrow, increment result.
            result++;
            arrowPosition = points[i][1];

        }
        return result;
    }
```

