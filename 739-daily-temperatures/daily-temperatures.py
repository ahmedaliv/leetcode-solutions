from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []  
        n = len(temperatures)
        ans = [0] * n 
        
        for i, t in enumerate(temperatures):
            while s and t > s[-1][0]:
                prev_temp, prev_index = s.pop()
                ans[prev_index] = i - prev_index
            s.append((t, i))
        
        return ans
