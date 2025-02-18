# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_so_far = float('-inf')
        def mx(root):
            if not root:
                return 0
            # get max of my left and right  children
            left =  mx(root.left)
            right = mx(root.right)
            nonlocal max_so_far
            # 4 cases for maximization 
            # only me
            max_so_far = max(max_so_far,root.val)
            # me and my the left 
            max_so_far = max(max_so_far,root.val + left)
            # me and my right 
            max_so_far = max(max_so_far,root.val + right)
            # me and both my left and right
            max_so_far = max(max_so_far,root.val + left + right)

            # when returning, we can only return 3 cases (the ones that include the current node)
            return max(root.val,root.val + max(left,right))
        mx(root)
        return max_so_far