# Trees (Binary Search Tree, BST)

## Definition of a Binary Tree Node
```java
// TreeNode Definition
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x;}
}
```

```java
// To Create a Tree as the images
root = TreeNode(1);
root.left = TreeNode(2);
root.right = TreeNode(3);
root.left.left = TreeNode(4);
root.left.left.right = TreeNode(5);
```
![image](imgs/TreeNode.png)


## Binary Search Tree


## Balanced Binary Tree


## Traversal
1. Preorder Traversal ()



2. Inorder Traversal (*Left-Root-Right Pattern*)
* Data is sorted when inorder is used.
```python
// In order Traversal with Recursion
def inOrder(root):
    if root is NULL, then return 
    inOrder(root.left)
    Process root
    inOrder(root.right)
```

1. Post Order

## How to create a BST


## Key to tree problems: Recursion

## Templates

### Single Root

### Two Root

