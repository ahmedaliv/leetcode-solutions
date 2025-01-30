from functools import lru_cache
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
 
        
        memo = {}
        R,C = len(matrix),len(matrix[0])
        def dp(r,c):
            if r < 0 or r >= R or c<0 or c>=C:
                return 0

            if (r,c) in memo:
                return memo[(r,c)]
            down = dp(r+1,c)
            diagonal = dp(r+1,c+1)
            right = dp(r,c+1)
            best = 1 if matrix[r][c] == "1" else 0
            if best:
                best+= min(down,diagonal,right)
            memo[(r,c)] = best
            return memo[(r,c)]
        dp(0,0)
        return(max(memo.values())) ** 2