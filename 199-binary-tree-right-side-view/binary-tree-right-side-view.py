# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):

    def rightSideView(self, root):
        if not root:
            return []
        res  = []
        queue = deque([root])
        while len(queue) != 0:
            level_len = len(queue)
            for i in range(level_len):
                front = queue.popleft()
                if i == level_len -1:
                    res.append(front.val)
                if front.left:
                    queue.append(front.left)
                if front.right:
                    queue.append(front.right)
        return res