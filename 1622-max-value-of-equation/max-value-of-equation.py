from heapq import heappush,heappop
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        heap = []

        best = float('-inf')
        heappush(heap,(-(points[0][1]-points[0][0]),points[0][0]))
        for i in range(1,len(points)):
            while heap and abs(heap[0][1] - points[i][0]) > k:
                heappop(heap)
            if heap:
                cur_val = points[i][0]+points[i][1]
                best = max(best,cur_val-heap[0][0])
            heappush(heap,(-(points[i][1]-points[i][0]),points[i][0]))
        return best