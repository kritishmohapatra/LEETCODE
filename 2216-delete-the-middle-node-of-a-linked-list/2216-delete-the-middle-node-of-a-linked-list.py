# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None :
            return None
        fast_ptr=head
        slow_ptr=head
        fast_ptr=fast_ptr.next.next
        while(fast_ptr!=None and fast_ptr.next!=None):
            fast_ptr=fast_ptr.next.next
            slow_ptr=slow_ptr.next
        slow_ptr.next=slow_ptr.next.next
        return head