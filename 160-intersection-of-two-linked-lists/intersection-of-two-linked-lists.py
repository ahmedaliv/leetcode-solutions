# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        h_t = {}
        p1 = headA
        while p1:
            h_t[p1] = True
            p1 = p1.next
        p2 = headB
        while p2:
            if p2 in h_t:
                return p2
            p2 = p2.next
        return None