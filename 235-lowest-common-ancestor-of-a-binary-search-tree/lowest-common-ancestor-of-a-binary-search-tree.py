# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        p_val = p.val
        q_val = q.val
        cur = root
        while cur:
            cur_val = cur.val
            if p_val > cur_val and q_val > cur_val:
                cur = cur.right
            elif p_val < cur_val  and q_val < cur_val:
                cur = cur.left
            else:
                return cur