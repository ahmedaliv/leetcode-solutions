# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        dq = deque()
        h_t = {}
        h_t[root]=None
        def build_parent(root):
            if not root:
                return
            if root.left:
                h_t[root.left]=root
                build_parent(root.left)
            if root.right:
                h_t[root.right]=root
                build_parent(root.right)
        build_parent(root)
        p_ancestors = set()
        while p:
            p_ancestors.add(p)
            p = h_t[p]
        while q:
            if q in p_ancestors:
                break
            q = h_t[q]
        return q
            