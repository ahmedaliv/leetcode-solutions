from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Flattens the binary tree into a linked list in-place.
        """
        def f(node):
            if not node:
                return None

            left_tail = f(node.left)
            right_tail = f(node.right)

            if left_tail:
                left_tail.right = node.right
                node.right = node.left 
                node.left = None
            return right_tail or left_tail or node
        f(root)