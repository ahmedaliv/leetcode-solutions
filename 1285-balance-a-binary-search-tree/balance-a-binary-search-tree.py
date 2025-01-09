

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorderTraversal(node):
            if not node:
                return []
            return inorderTraversal(node.left) + [node.val] + inorderTraversal(node.right)
        
        sorted_values = inorderTraversal(root)
        
        def buildBalancedBST(values):
            if not values:
                return None
            mid = len(values) // 2
            root = TreeNode(values[mid])
            
            root.left = buildBalancedBST(values[:mid])
            
            root.right = buildBalancedBST(values[mid+1:])
            
            return root
        
        return buildBalancedBST(sorted_values)
