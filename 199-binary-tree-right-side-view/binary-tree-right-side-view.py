# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #simple BFS solution
        # we go level by level (but by adding nodes from right to left)
        # so the first node in each level is the first one to the right 
        if not root:
            return []
        res = []
        queue = deque([root])
        while len(queue):
            level_size = len(queue)
            for i in range(level_size):
                front = queue.popleft()
                if not i:
                    res.append(front.val) 
                if front.right:
                    queue.append(front.right)
                if front.left:
                    queue.append(front.left)    
        return res