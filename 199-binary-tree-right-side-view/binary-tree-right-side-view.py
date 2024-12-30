# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):

    def rightSideView(self, root):


        res  = []
        # def dfs(root,level):
        #     if root==None:
        #         return
        #     if len(res) == level:
        #         res.append(root.val)
        #     dfs(root.right,level+1)
        #     dfs(root.left,level+1)
        # dfs(root,0)
        # return res
        
        if not root:
            return []
        queue = deque([root])
        while len(queue) != 0:
            level_len = len(queue)
            for i in range(level_len):
                front = queue.popleft()
                if i == 0:
                    res.append(front.val)
                if front.right:
                    queue.append(front.right)
                if front.left:
                    queue.append(front.left)
        return res