from heapq import heappush,heappop
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        """
        we would put a pointer in the start of each list 
        and then get the one that has the smallest value and then append it to the result
        and then advance 
        and so on
        
        """
        pointers = []
        for i,l in enumerate(lists):
            if l:
                heappush(pointers,(l.val,i,l))
        dummy = ListNode()
        res_tail = dummy
        while pointers:
            # get the pointer the points to the smallest value
            _,i,smol_pointer = heappop(pointers)
            res_tail.next = smol_pointer
            res_tail = res_tail.next
            if smol_pointer.next:
                heappush(pointers,(smol_pointer.next.val,i,smol_pointer.next))
            
        return dummy.next