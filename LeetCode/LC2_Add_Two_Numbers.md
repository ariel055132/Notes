# 2. Add Two Numbers

* You are given two non-empty linked lists representing two non-negative integers.
* The digits are stored in reverse order, each of their nodes contains a single digit.
* Add the two numbers and return the sum as a linked list

```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```

```
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```



## Solution 1: Simulation

* Simulate digits-by-digits sum calculation from the head of the list.
* Keep track of the carry using a variable.

### Pseudocode

- Initialize current node to dummy head of the returning list.
- Initialize carry to 00.
- Loop through lists l1 and l2 until you reach both ends and carry is 0.
  - Set x to node l1*l*1's value. If l1 has reached the end of l1, set to 0.
  - Set y to node l2*l*2's value. If l2 has reached the end of l2, set to 0.
  - Set sum = x + y + carry
  - Update carry = sum / 10.
  - Create a new node with the digit value of (sum mod 10) and set it to current node's next, then advance current node to next.
  - Advance both l1 and l2.
- Return dummy head's next node.

```java
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;
        int sum = 0;
        int carry = 0;
        while (l1 != null || l2 != null || carry != 0) {
            int l1_val = 0;
            int l2_val = 0;
            if (l1 != null) {
                l1_val = l1.val;
            } else if (l1 == null) {
                l1_val = 0;
            }
            if (l2 != null) {
                l2_val = l2.val;
            } else if (l2 == null) {
                l2_val = 0;
            }
            sum = l1_val + l2_val + carry;
            carry = sum / 10;
            int digit_num = sum % 10;
            curr.next = new ListNode(digit_num);
            curr = curr.next;
            if (l1 != null) {
                l1 = l1.next;
            } 
            if (l2 != null) {
                l2 = l2.next;
            }
        }
        
        return dummy.next;
    }
}
```

