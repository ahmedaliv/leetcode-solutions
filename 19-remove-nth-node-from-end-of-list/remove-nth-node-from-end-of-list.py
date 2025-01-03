# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        d_head = ListNode(-1,head)
        first,second = d_head,d_head
        for i in range(n+1):
            if not first:
                return None
            first = first.next
        while first:
            first = first.next
            second = second.next
        second.next= second.next.next
        return d_head.next
        