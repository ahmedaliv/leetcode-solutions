# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_so_far = float('-inf')
        def max_sum_starting_from_node(root):
            nonlocal max_so_far
            if not root:
                return 0
            l = max_sum_starting_from_node(root.left)
            r = max_sum_starting_from_node(root.right)

            max_so_far=max(max_so_far,root.val,root.val+l+r,root.val+l,root.val+r)
            
            # 3 cases for max sum starting with this root
            return root.val + max(0,l,r)
        max_sum_starting_from_node(root)
        return max_so_far