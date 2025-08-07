# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, csum):
            if node and not node.left and not node.right:
                return csum == targetSum
            left_result = dfs(node.left, csum + node.left.val) if node.left else False
            right_result = dfs(node.right, csum + node.right.val) if node.right else False
            return left_result or right_result

        if not root:
            return False
        return dfs(root, root.val)