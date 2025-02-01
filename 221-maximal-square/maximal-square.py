from functools import lru_cache
class Solution:
    # def maximalSquare(self, matrix: List[List[str]]) -> int:
 
        
        # memo = {}
        # R,C = len(matrix),len(matrix[0])
        # def dp(r,c):
        #     if r < 0 or r >= R or c<0 or c>=C:
        #         return 0

        #     if (r,c) in memo:
        #         return memo[(r,c)]
        #     down = dp(r+1,c)
        #     diagonal = dp(r+1,c+1)
        #     right = dp(r,c+1)
        #     best = 1 if matrix[r][c] == "1" else 0
        #     if best:
        #         best+= min(down,diagonal,right)
        #     memo[(r,c)] = best
        #     return memo[(r,c)]
        # dp(0,0)
        # return(max(memo.values())) ** 2
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
            side = min(heights[i] ,(right - left + 1))
            best = max(best,side*side)
        
        return best
    
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        prefix = [[0] * cols for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    prefix[i][j] = prefix[i][j-1] + 1 if j > 0 else 1
                else:
                    prefix[i][j] = 0
        
        max_area = 0
        
        for j in range(cols):
            heights = [prefix[i][j] for i in range(rows)]
            max_area_col = self.largestRectangleArea(heights)
            max_area = max(max_area, max_area_col)
        
        return max_area