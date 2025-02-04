# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self,headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        # we created a cycle
        tail = headA
        while tail.next:
            tail = tail.next
        tail.next = headA 

        # now go from headb to get the intersection ( apply fast,slow algorithm tortoise and hare )
    
        fast,slow = headB,headB
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow==fast:
                break
        else:
            tail.next = None
            return None
        slow = headB
        while fast != slow:
            fast = fast.next
            slow = slow.next
        tail.next = None
        return slow