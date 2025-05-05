class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        total_nodes = 0
        cur = head
        while cur:
            total_nodes += 1
            cur = cur.next
        iters = total_nodes // k
        cur = head
        returned_head = None
        prev_tail = None
        for i in range(iters):
            group_tail = None
            prev = None
            for j in range(k):
                if not group_tail:
                    group_tail = cur
                next_node = cur.next
                cur.next = prev
                prev = cur
                cur = next_node
            if not returned_head:
                returned_head = prev
            if prev_tail:
                prev_tail.next = prev
            prev_tail = group_tail
            group_tail.next = cur
        return returned_head
