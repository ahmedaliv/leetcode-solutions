# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        predecessor = None
        mn = mx = None
        def select(pre,cur):
            nonlocal mn, mx

            if not mn:
                mn = cur
                mx = pre
            else:
                mn = cur


        def in_order(node):
            nonlocal predecessor

            if not node:
                return
            in_order(node.left)
            if predecessor and node.val < predecessor.val:
                select(predecessor,node)
            predecessor = node
            in_order(node.right)


        in_order(root)
        mn.val, mx.val = mx.val, mn.val
