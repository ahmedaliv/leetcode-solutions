# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        output = []
        level = 0
        while q:
            sz = len(q)
            current_level_nodes = []
            for _ in range(sz):
                node = q.popleft()
                current_level_nodes.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if level % 2 == 1:
                current_level_nodes.reverse()
            output.append(current_level_nodes)
            level +=1
        return output