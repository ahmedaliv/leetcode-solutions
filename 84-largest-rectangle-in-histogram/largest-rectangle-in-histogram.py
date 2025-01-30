from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        
        def next_lower():
            res = [n] * n  
            s = []
            for i in range(n):
                while s and heights[s[-1]] > heights[i]:
                    res[s[-1]] = i
                    s.pop()
                s.append(i)
            return res
        
        def prev_lower():
            res = [-1] * n 
            s = []
            for i in range(n-1, -1, -1):
                while s and heights[s[-1]] > heights[i]:
                    res[s[-1]] = i
                    s.pop()
                s.append(i)
            return res
        
        nl = next_lower()
        pl = prev_lower()
        
        best = 0
        for i in range(n):
            left = pl[i] + 1
            right = nl[i] - 1
            best = max(best, heights[i] * (right - left + 1))
        
        return best