class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode(-1)
        dummy.next = head
        fast,slow = dummy,dummy
        while fast and fast.next:
            slow = slow.next
            fast=fast.next.next
            if slow == fast:
                return True
        return False