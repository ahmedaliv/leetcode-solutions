# from heapq import heappush,heappop
from collections import deque
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        dq = deque()
        ans = float('-inf')
        for x,y in points:
            # remove invalid entires
            while dq and x - dq[0][1] > k:
                dq.popleft()
            # maximize on the answer
            if dq:
                ans = max(ans,dq[0][0] + x + y)
            # remove anything smaller than us 
            while dq and dq[-1][0] < y-x:
                dq.pop()
            dq.append(((y-x),x))
        return ans