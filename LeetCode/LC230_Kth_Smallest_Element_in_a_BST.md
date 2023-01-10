# 230. Kth Smallest Element in a BST

## Content

* Given the `root` of a binary search tree, and an integer `k`, return *the* `kth` *smallest value (**1-indexed**) of all the values of the nodes in the tree*.

```
Input: root = [3,1,4,null,2], k = 1
Output: 1
```



## Solution 1: InOrder Traversal

* InOrder Traversal of BST can build a sorted array in ascending order
* You may also use a global counter to count the traversal order of BST, and return the result --> Code below, space Complexity = O(1)
* Time Complexity: O(N)
* Space Complexity: O(N), O(1)

```java
// Space Complexity: O(1)
class Solution {
    private int counter = 0;
    private int result = -1; // final result

    public int kthSmallest(TreeNode root, int k) {
        inOrderTraverse(root, k);
        return result;
    }

    private void inOrderTraverse(TreeNode root, int k) {
        if (root == null) {
            return;
        }
        inOrderTraverse(root.left, k);
        if (++counter == k) {
            result = root.val;
            return;
        }
        inOrderTraverse(root.right, k);
    }

}
```

```java
// Space Complexity: O(N)
class Solution {
	public int kthSmallest(TreeNode root, int k) {
    ArrayList<Integer> nums = inOrderTraverse(root, new ArrayList<Integer>());
    return nums.get(k - 1); // -1 is needed because it is 1-indexed
  }
  // InOrder Traversal (LVR)
  public ArrayList<Integer> inOrderTraverse(TreeNode root, ArrayList<Integer> arr) {
    // empty tree / reach the end of the tree --> return the result
    if (root == null) {
      return arr;
    } 
    inOrderTraverse(root.left, arr);
    arr.add(root.val);
    inOrderTraverse(root.right, arr);
    return arr;
  }
}
```

