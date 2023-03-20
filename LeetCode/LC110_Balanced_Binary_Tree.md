# 110. Balanced Binary Tree

## Content

* Given a binary tree, determine if it is **height-balanced**
* Height-balanced: The height of left-subtree == The height of right-subtree
* That means if height of left-subtree minus height of right-subtree is equal to 0, it is height-balanced. Otherwise, it is not height-balanced

```text
Input: root = [3,9,20,null,null,15,7]
Output: true
```

```
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
```

```
Input: root = []
Output: true
```



## Approach 1: DFS (Depth-First Search)

1. Traverse the tree, and get the height of left and right subtree
2. Minus the heights obtained in step 1. Determine it is equal to 0 or not.
3. If it (the height) is 0, return True. Otherwise, return False. 



* PseudoCode

```
is Balanced(root):
	if (root == NULL):
		return True
	if (abs(height(root.left) - height(root.right)) > 1):
		return False
	else:
		return isBalanced(root.left) && isBalanced(root.right)
```



## Approach 1: Code

```java
package leetcode.editor.en;
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) {this.val = val;}
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution110 {
    public boolean isBalanced(TreeNode root) {
        if (root == null) {
            return true;
        } else if (Math.abs(height(root.left) - height(root.right)) > 1) return false;
        else return isBalanced(root.left) && isBalanced(root.right);
    }

    public static int height(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int leftSubTree = height(root.left);
        int rightSubTree = height(root.right);
        return Math.max(leftSubTree, rightSubTree) + 1;
    }
}

```

* Time Complexity: O(n log n)
* Space Complexity: O(n), where n is the length of the node