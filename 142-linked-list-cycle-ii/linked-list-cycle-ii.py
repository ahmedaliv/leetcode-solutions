# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def get_intersection(head):
            if not head:
                return None
            slow = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return slow
            return None
        intersection_node = get_intersection(head)
        if not intersection_node:
            return None
        dummy = head
        while intersection_node != dummy:
            intersection_node = intersection_node.next
            dummy = dummy.next
        return dummy