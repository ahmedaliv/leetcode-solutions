# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:

    def lowestCommonAncestor(self,root, p, q):
        if not root:
            return None

        parent_map = {root: None}
        queue = deque([root])

        while p not in parent_map or q not in parent_map:
            node = queue.popleft()

            if node.left:
                parent_map[node.left] = node
                queue.append(node.left)
            if node.right:
                parent_map[node.right] = node
                queue.append(node.right)

        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent_map[p]

        while q not in ancestors:
            q = parent_map[q]

        return q
