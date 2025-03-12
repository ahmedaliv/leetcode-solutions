# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
import heapq
class Solution:

    def verticalTraversal(self,root):
        if not root:
            return []
        
        q = deque([(root, 0, 0)])  
        h_m = defaultdict(list)    
        
        while q:
            node, row, col = q.popleft()
            heapq.heappush(h_m[col], (row, node.val))  
            
            if node.left:
                q.append((node.left, row + 1, col - 1))
            if node.right:
                q.append((node.right, row + 1, col + 1))
        
        return [[val for _, val in sorted(h_m[col])] for col in sorted(h_m.keys())]
