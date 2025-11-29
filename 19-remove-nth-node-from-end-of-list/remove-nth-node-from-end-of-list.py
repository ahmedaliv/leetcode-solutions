# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def get_len(node):
            dummy_head = node
            i = 0
            while dummy_head:
                dummy_head = dummy_head.next
                i+=1
            return i
        k = get_len(head)

        dummy = ListNode(-1,head)
        cur = dummy

        for _ in range(k-n): 
            cur = cur.next

        cur.next = cur.next.next
        return dummy.next
