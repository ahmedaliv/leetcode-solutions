# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def parenthesize(root):
            if not root:
                return '()'
            left = parenthesize(root.left)
            right = parenthesize(root.right)
            return f"({root.val}{left}{right}"
        parenthesized_root = parenthesize(root)
        parenthesized_subRoot = parenthesize(subRoot)
        return parenthesized_subRoot in parenthesized_root
