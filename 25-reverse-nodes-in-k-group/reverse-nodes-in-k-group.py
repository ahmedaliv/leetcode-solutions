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
            stack = []
            temp = prev_group_end.next
            
            # Push k nodes onto the stack
            for _ in range(k):
                if not temp:
                    return dummy.next
                stack.append(temp)
                temp = temp.next
            
            # Pop nodes from stack to reverse them
            while stack:
                prev_group_end.next = stack.pop()
                prev_group_end = prev_group_end.next
            
            # Connect to the next part of the list
            prev_group_end.next = temp
        
        return dummy.next
