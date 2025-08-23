# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        def dfs(node, curSum, pathNodes):
            if node and not node.left and not node.right:
                if curSum == targetSum:
                    paths.append(pathNodes)
                return
            if node.left:
                dfs(node.left,curSum+node.left.val,pathNodes +[node.left.val])
            if node.right:
                dfs(node.right,curSum+node.right.val,pathNodes + [node.right.val])   
        
        if root:
            dfs(root,root.val,[root.val])
        return paths