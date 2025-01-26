# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def check_equiv(r1, r2):
            if not r1 and not r2:
                return True
            if not r1 or not r2 or r1.val != r2.val:
                return False
            
            if check_equiv(r1.left, r2.left) and check_equiv(r1.right, r2.right):
                return True
            
            if check_equiv(r1.left, r2.right) and check_equiv(r1.right, r2.left):
                return True
            
            return False
        
        return check_equiv(root1, root2)
