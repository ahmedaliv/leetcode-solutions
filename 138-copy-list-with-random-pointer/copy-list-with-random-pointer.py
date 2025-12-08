"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        cur = head
        # create intermediate Nodes A,A',B,B'
        # and link the next pointer 
        while cur:
            orig_next = cur.next
            cur.next = Node(cur.val)
            cur.next.next = orig_next
            cur = cur.next.next
        
        new_head = head.next
        
        # assign random pointers 
        cur = head
        while cur:
            # connect the dash nodes to the dash randoms
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # split the two lists
        cur = head
        while cur:
            # dash node
            cp = cur.next
            #connect the original list again
            cur.next = cur.next.next
            if cp.next:
                cp.next = cp.next.next
            cur = cur.next
        return new_head
