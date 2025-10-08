# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d=ListNode(-1)
        t=d
        c=0
        while (l1!=None or l2!=None) or c:
            s=0
            if l1!=None:
                s+=l1.val
                l1=l1.next
            if l2!=None:
                s+=l2.val
                l2=l2.next
            s+=c
            c=s//10
            node=ListNode(s%10)
            t.next=node
            t=t.next
        return d.next
        