"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        from collections import deque
        q = deque()
        q.append(root)

        while q:
            level_size = len(q)
            # important to reset for each level
            prevNode = None

            for _ in range(level_size):
                node = q.pop()
                node.next = prevNode
                prevNode = node

                if node.right:
                    q.appendleft(node.right)
                if node.left:
                    q.appendleft(node.left)
        return root