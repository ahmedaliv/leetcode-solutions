import heapq
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        moduls = 10**9 + 7
        ans = 0 
        eng = sorted(zip(efficiency,speed),reverse=True)
        heap = []
        speedsum = 0
        for i in range(len(eng)):
            ef = eng[i][0]
            sp = eng[i][1]
            speedsum +=sp
            heapq.heappush(heap,sp)
            if len(heap) > k :
                speedsum -= heapq.heappop(heap)
                # ef = 
            ans = max(ans,speedsum*ef)
        return ans % moduls