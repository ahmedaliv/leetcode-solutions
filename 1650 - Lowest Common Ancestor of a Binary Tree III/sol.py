"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def depth(node):
            depth = 0
            while node:
                node = node.parent
                depth +=1
            return depth
        pd,qd=depth(p),depth(q)
        if pd<qd:
          pd,qd=qd,pd
          p,q=q,p
        while pd>qd:
          p = p.parent
          pd-=1
        while p:
          if p == q:
            return p
          p = p.parent
          q = q.parent
        return None
