# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        cur_a = headA
        cur_b = headB
        while cur_a !=cur_b:
            if not cur_a:
                cur_a = headB
            else:
                cur_a = cur_a.next
            if not cur_b:
                cur_b = headA
            else:
                cur_b = cur_b.next
        return cur_a 