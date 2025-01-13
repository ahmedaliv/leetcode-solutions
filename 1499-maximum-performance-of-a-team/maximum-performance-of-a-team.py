from heapq import heappush, heappop
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        eng = []
        for i in range(len(speed)):
            eng.append([efficiency[i], speed[i]])
        eng.sort(reverse=True)
        
        best_team = []
        ans = 0
        cur_sum = 0
        
        for e, s in eng:
            cur_sum += s
            heappush(best_team, s)
            
            if len(best_team) > k:
                cur_sum -= heappop(best_team)
            
            ans = max(ans, cur_sum * e)
        
        return ans % (10**9 + 7)
