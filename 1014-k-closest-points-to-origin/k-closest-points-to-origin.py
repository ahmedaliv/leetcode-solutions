import math
from heapq import heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for point in points:
            dist = (point[0] ** 2) + (point[1] ** 2)
            heappush(heap, (dist, point))
        
        res = []
        for _ in range(k):
            res.append(heappop(heap)[1])
        
        return res
