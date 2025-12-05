# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h_t = {}
        cur = head
        while cur:
            if cur in h_t:
                return cur
            h_t [cur] = True
            cur = cur.next
        return None

        