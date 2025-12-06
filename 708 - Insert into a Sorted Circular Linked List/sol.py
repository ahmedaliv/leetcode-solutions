"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if head is None:
            node = Node(insertVal)
            node.next = node
            return node
        cur = head
        while True:
            nxt = cur.next
            # case 1: normal place between two sorted nodes
            if cur.val <= insertVal <= nxt.val:
              break
            # case 2: if we are at the flip point we have 2 cases to insert (30-10) we insert only if > 30 or < 10
            if cur.val > nxt.val:  # flip point
                if insertVal >= cur.val or insertVal <= nxt.val:
                    break
            # case 3: we completed a cycle without breaking, that means we are at the final case(all equal)
            if head == cur:
              break
        cur.next = Node(insertVal,cur.next)
        return head
        
