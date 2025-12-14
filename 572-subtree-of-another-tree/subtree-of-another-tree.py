# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        SEEN = set()
        def dfs(root):
            if not root:
                return '#'

            left = dfs(root.left)
            right = dfs(root.right)

            h = f"{root.val},{left},{right}"
            SEEN.add(h)
            return h
        def dfs_sub(root):
            if not root:
                return '#'
            return f"{root.val},{dfs_sub(root.left)},{dfs_sub(root.right)}"
            
        dfs(root)
        return dfs_sub(subRoot) in SEEN