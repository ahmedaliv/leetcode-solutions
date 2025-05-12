from collections import defaultdict

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        col_table = defaultdict(list)

        def dfs(node, row, col):
            if not node:
                return
            col_table[col].append((row,node.val))
            dfs(node.left,row+1,col-1)
            dfs(node.right,row+1,col+1)
        
        dfs(root, 0, 0)

        result = []
        for col in sorted(col_table):
            col_table[col].sort()
            result.append([val for row, val in col_table[col]])
        return result
