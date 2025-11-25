from heapq import heappush,heappop
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        pq = []
        ans = float('-inf')
        for x,y in points:
            while pq and x - pq[0][1]>k:
                heappop(pq)
            if pq:
                ans = max(ans,-pq[0][0] + x + y)

            heappush(pq,(-(y-x),x))
        return ans