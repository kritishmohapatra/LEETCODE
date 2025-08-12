# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        curr_ptr=head
        next_ptr=0
        while(curr_ptr!=None):
            next_ptr=curr_ptr.next
            curr_ptr.next=prev
            prev=curr_ptr
            curr_ptr=next_ptr
        return prev
        