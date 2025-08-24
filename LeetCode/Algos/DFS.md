* Complexity: O(n + m)
```java
void dfs(int currentNode) {
    visit[currentNode] = 1;
    for (all node u connect to currentNode) {
        dfs(u)
    }
}
```

* grid eligibility
```java
int count = 0;
// Invalid grid, return
if (grid.length == 0 || grid[0].length == 0) {
    return count;
}

int m = grid.length; 
int n = grid[0].length;
```

* Transform grid to a graph
```java
// horizontal
for (int i = 0; i < n; i++) {
    for (int j = 0; j < m - 1; j++) {
        if (grid[i][j] == 1 && grid[i][j+1] == 1) {
            // Do something
        }
    }
}

// Vertical
for (int i = 0; i < n - 1; i++) {
    for (int j = 0; j < m; j++) {
        if (grid[i+1][j] == 1 && grid[i][j] == 1) {
            // Do something
        }
    }
}
```

* disjoint set (Union find)
```java
int Find(int x) {
    while (parent[x] != x) {
        x = parent[x];
    }
    return x;
}

// Recursion
int Find(int x) {
    if (parent[x] == x) {
        return x;
    }
    return Find(parent[x]);
}

// Recursion (Update Parent / Path compression)
int Find(int x) {
    if (parent[x] == x) {
        return x;
    }
    return parent[x] = Find(parent[x]);
}

void Union(int x, int y) {
    if (Find(x) != Find(y)) {
        parent[Find(x)] = Find(y);
    }
}
```