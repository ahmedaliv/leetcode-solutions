# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        def in_order(root):
            if not root:
                return
            in_order(root.left)
            arr.append(root.val)
            in_order(root.right)
        in_order(root)
        def balance_tree(arr):
            if not arr:
                return None
            mid = len(arr) // 2
            root = TreeNode(arr[mid])
            root.left = balance_tree(arr[:mid])
            root.right = balance_tree(arr[mid+1:])
            return root
        return balance_tree(arr)