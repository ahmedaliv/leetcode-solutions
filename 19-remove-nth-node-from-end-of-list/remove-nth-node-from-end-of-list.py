# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        d_head = ListNode(-1,head)
        f,s=d_head,d_head
        for _ in range(n+1):
            # if not f:
            #     return None
            f= f.next
        while f:
            f=f.next
            s=s.next
        s.next=s.next.next
        return d_head.next