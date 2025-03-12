# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from sortedcontainers import SortedDict

class Solution:

    def verticalTraversal(self,root):
        if not root:
            return []

        node_map = SortedDict()
        queue = deque([(root, 0, 0)])

        while queue:
            node, row, col = queue.popleft()

            if col not in node_map:
                node_map[col] = []
            node_map[col].append((row, node.val))
            
            if node.left:
                queue.append((node.left, row + 1, col - 1))
            if node.right:
                queue.append((node.right, row + 1, col + 1))
        
        result = []
        for col in node_map:
            result.append([val for row, val in sorted(node_map[col])])

        return result