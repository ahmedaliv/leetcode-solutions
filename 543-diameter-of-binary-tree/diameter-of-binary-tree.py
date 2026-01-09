# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0
        def get_dm(root):
            nonlocal best
            if not root:
                return 0 
            l = get_dm(root.left)
            r = get_dm(root.right)
            best = max(best,l+r)
            return 1 + max(l,r)
        get_dm(root)
        return best
