# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root or p == root or q==root:
            return root
        
        # check values to know where to search
        # if both are lower than root we go right if not we go left
        # or if not we search in both 
        left = None
        right = None
        if p.val < root.val and q.val < root.val:
            left = self.lowestCommonAncestor(root.left,p,q)
        elif p.val > root.val and q.val>root.val:
            right = self.lowestCommonAncestor(root.right,p,q)
        else:
            left = self.lowestCommonAncestor(root.left,p,q)
            right = self.lowestCommonAncestor(root.right,p,q)
        if not left:
            return right
        if not right:
            return left
        return root