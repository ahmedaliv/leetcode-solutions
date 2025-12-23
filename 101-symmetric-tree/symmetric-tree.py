# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def parenthesize_l_r(root):
            if not root:
                return '()'
            left = parenthesize_l_r(root.left)
            right = parenthesize_l_r(root.right)
            return f'{root.val}{left}{right}'

        def parenthesize_r_l(root):
            if not root:
                return '()'
            right = parenthesize_r_l(root.right)
            left = parenthesize_r_l(root.left)
            return f'{root.val}{right}{left}'
        left_sub = parenthesize_l_r(root.left)
        right_sub = parenthesize_r_l(root.right)
        return left_sub == right_sub
