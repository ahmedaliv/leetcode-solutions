class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def f(r,c):
            if r==m-1 and c==n-1:
                return 1
            if r>=m or c>=n:
                return 0
            if (r,c) in memo:
                return memo[r,c]
            
            down = f(r+1,c)
            right = f(r,c+1)
            memo[r,c] = down+right
            return memo[r,c]
        return f(0,0)