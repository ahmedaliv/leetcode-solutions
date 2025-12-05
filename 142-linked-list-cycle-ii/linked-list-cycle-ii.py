# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def get_intersection(node):
            if not node:
                return None

            fast = slow = node
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
                if slow == fast:
                    return fast
            return None

        int_point = get_intersection(head)
        if not int_point:
            return None
        while head != int_point:
            head = head.next
            int_point = int_point.next
        return int_point