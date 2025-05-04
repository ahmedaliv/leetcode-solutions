class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next  # store next node
            curr.next = prev       # reverse pointer
            prev = curr            # move prev forward
            curr = next_node       # move curr forward

        return prev
