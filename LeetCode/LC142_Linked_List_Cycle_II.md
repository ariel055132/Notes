# 142. Linked List Cycle II

## Content

* Given the head of a linked list, return the node where the cycle begins. 
* If there is no cycle.
* Follow Up: Can you solve it using O(1) memory?

```text
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
Note that pos is not passed as a parameter
```

```text
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
```



## Solution 1: Hash Table

* We can keep track of the nodes that we have seen already in a set. 
* Traverse the list and return the first duplicated node (If the linked list is cyclic).
* Time Complexity: O(N)
* Space Complexity: O(N)

```java
public class Solution {
    public ListNode detectCycle(ListNode head) {
        Set<ListNode> visited = new HashSet<ListNode>();

        ListNode node = head;
        while (node != null) {
            if (visited.contains(node)) {
                return node;
            }
            visited.add(node);
            node = node.next;
        }

        return null;
    }
}
```



## Solution 2: Floyd Cycle Detection Algorithm

* Define two pointers slow and fast.
* Both start at head node, fast is twice as fast as slow.
* If fast reaches end, it means there is no cycle.
* Otherwise it will catch up to slow pointer eventually.

```java
public class Solution {
            public ListNode detectCycle(ListNode head) {
                ListNode slow = head;
                ListNode fast = head;
        
                while (fast!=null && fast.next!=null){
                    fast = fast.next.next;
                    slow = slow.next;
                    
                    if (fast == slow){
                        ListNode slow2 = head; 
                        while (slow2 != slow){
                            slow = slow.next;
                            slow2 = slow2.next;
                        }
                        return slow;
                    }
                }
                return null;
            }
        }
```

