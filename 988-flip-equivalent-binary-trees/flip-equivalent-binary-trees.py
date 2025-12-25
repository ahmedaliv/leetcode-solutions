# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def parethesize(root):
            if not root:
                return '()'
            left = parethesize(root.left)
            right = parethesize(root.right)
            if left>right:
                left,right=right,left
            return f'{root.val},{left},{right}'
        canonical_1 = parethesize(root1)
        canonical_2 = parethesize(root2)
        return canonical_1 == canonical_2