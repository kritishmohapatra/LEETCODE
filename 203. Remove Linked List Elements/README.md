# 203. Remove Linked List Elements

### Difficulty: Easy

## Description
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

 
Example 1:


Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]


Example 2:


Input: head = [], val = 1
Output: []


Example 3:


Input: head = [7,7,7,7], val = 7
Output: []


 
Constraints:


	The number of nodes in the list is in the range [0, 104].
	1 <= Node.val <= 50
	0 <= val <= 50

## Submission Details
- **Status**: Accepted
- **Runtime**: 3
- **Memory**: 22620000
- **Language**: python3

## Code
```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        d=ListNode(0)
        d.next=head
        c=d
        while c.next:
            if c.next.val==val:
                c.next=c.next.next 
            else:
                c=c.next 
        return d.next

```
