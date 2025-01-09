# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if not root:
        #     return None
        # queue = deque([root])

        # while queue:
        #     node = queue.popleft()
        #     node.left,node.right = node.right,node.left
        #     if node.left:
        #         queue.append(node.left)
        #     if node.right:
        #         queue.append(node.right)
        # return root
        def dfs(node):
            if not node:
                return None
            node.left,node.right= node.right,node.left
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return root