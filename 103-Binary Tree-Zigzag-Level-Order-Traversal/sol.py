# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        # the root is the first l-t-r 
        queue = deque()
        queue.appendleft((root,0))
        output = []
        while queue:
            level_size = len(queue)
            level_nodes = deque()

            for _ in range(level_size):
                cur_node, cur_level = queue.popleft()

                if cur_level % 2 == 0 :
                    level_nodes.append(cur_node.val)
                else:
                    level_nodes.appendleft(cur_node.val)
                
                if cur_node.left:
                    queue.append((cur_node.left,cur_level+1))
                if cur_node.right:
                    queue.append((cur_node.right,cur_level+1))

            output.append(list(level_nodes))
        return output
