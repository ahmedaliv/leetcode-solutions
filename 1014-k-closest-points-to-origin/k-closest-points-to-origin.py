from heapq import heappop,heappush
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            dist = -((p[0] ** 2) + (p[1] ** 2))
            heappush(heap,(dist,p))

            if len(heap) > k :
                heappop(heap)
        res = []
        for _ in range(k):
            res.append(heappop(heap)[-1])
        return res