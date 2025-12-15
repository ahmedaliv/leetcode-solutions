# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = {root: None}
        depth = {root: 0}

        # build parent and depth
        stack = [root]
        while stack:
            node = stack.pop()

            if node.left:
                parent[node.left] = node
                depth[node.left] = depth[node] + 1
                stack.append(node.left)

            if node.right:
                parent[node.right] = node
                depth[node.right] = depth[node] + 1
                stack.append(node.right)

        # align depths
        while depth[p] > depth[q]:
            p = parent[p]

        while depth[q] > depth[p]:
            q = parent[q]

        # move up together
        while p != q:
            p = parent[p]
            q = parent[q]

        return p