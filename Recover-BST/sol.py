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
        #O(1) space
        cur_mn,cur_mx = None,None
        def update(mn,mx):
            nonlocal cur_mn,cur_mx
            if not cur_mn or mn.val < cur_mn.val:
                cur_mn = mn
            if not cur_mx or mx.val > cur_mx.val:
                cur_mx = mx
            
        
        def dfs(root,mn=None,mx=None):
            if not root:
                return
            if mn and mn.val > root.val:
                update(root,mn)
            if mx and mx.val <root.val:
                update(mx,root)
            dfs(root.left,mn,root)
            dfs(root.right,root,mx)
        dfs(root)
        cur_mx.val,cur_mn.val = cur_mn.val,cur_mx.val
        


