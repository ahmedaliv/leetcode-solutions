# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappush, heappop
from itertools import count


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pointers = []
        counter = count()
        for i,l in enumerate(lists):
            if l:
                heappush(pointers,(l.val,next(counter),l))
        dummy = ListNode(-1)
        tail = dummy
        while pointers:
            val,cnt,top = heappop(pointers)
            if top.next:
                heappush(pointers,(top.next.val,next(counter),top.next))
            tail.next = top
            tail = tail.next
        return dummy.next


