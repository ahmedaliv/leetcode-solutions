# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def is_same(self,root,subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if root.val != subRoot.val:
            return False
        return self.is_same(root.left,subRoot.left) and self.is_same(root.right,subRoot.right)

        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # we have 3 cases, either the cur. root is the same as the target subtree
        # or the subtree on the left or in the right
        if not root and not subRoot:
            return True 
        if not root or not subRoot:
            return False
        if self.is_same(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)


