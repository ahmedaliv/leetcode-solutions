class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def dfs(node):
            if not node:
                return None
            
            left_tail = dfs(node.left)
            right_tail = dfs(node.right)

            if node.left:
                temp = node.right
                node.right = node.left
                node.left = None
                left_tail.right = temp

            return right_tail or left_tail or node

        dfs(root)
