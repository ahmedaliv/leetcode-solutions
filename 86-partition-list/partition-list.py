class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None

        less = []
        greater = []

        cur = head
        while cur:
            if cur.val < x:
                less.append(cur)
            else:
                greater.append(cur)
            cur = cur.next

        for node in less:
            node.next = None
        for node in greater:
            node.next = None

        dummy = ListNode()
        tail = dummy
        
        for node in less:
            tail.next = node
            tail = tail.next

        for node in greater:
            tail.next = node
            tail = tail.next

        return dummy.next
