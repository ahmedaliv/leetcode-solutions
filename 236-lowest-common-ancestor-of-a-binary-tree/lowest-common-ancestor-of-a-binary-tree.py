# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:

    def lowestCommonAncestor(self,root, p, q):


        if not root:
            return None

        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        # diff. subtrees
        if left and right:
            return root
        #one of them is the root
        if p == root or q==root:
            return root
        # both in one subtree so we return it 
        # keep in mind that this propgates to the top, so you would have the LCA
        return left or right