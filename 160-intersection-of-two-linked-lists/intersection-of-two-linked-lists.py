# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def get_intersection(head):
            if not head:
                return None
            fast,slow = head,head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if fast==slow:
                    return fast
            return None
        # create cycle explicitly to make use of two pointer approach
        tailA = headA
        while tailA.next:
            tailA = tailA.next
        tailA.next = headA
        int_point = get_intersection(headB)
        if not int_point:
            tailA.next = None
            return None
        # now using math. if we started at head and int_point and moved one by one, we will meet at cycle beginning 
        dummy = headB
        while int_point!=dummy:
            dummy = dummy.next
            int_point = int_point.next
        tailA.next = None
        return int_point 

