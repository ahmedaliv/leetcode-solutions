# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy

        while True:
            kth_node = prev_group_end
            for _ in range(k):
                kth_node = kth_node.next
                if not kth_node:
                    return dummy.next

            prev = None
            cur = prev_group_end.next
            start_node = cur
            for _  in range(k):
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            start_node.next = cur
            prev_group_end.next = prev
            prev_group_end = start_node
        return dummy.next