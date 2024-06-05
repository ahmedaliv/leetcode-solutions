class Solution(object):
    def minPathSum(self, grid):
        rows, cols = len(grid), len(grid[0])
        memo = [[-1 for _ in range(cols)] for _ in range(rows)]
        
        def minP(i, j):
            if i >= rows or j >= cols:
                return float('inf')
            
            if i == rows - 1 and j == cols - 1:
                return grid[i][j]
            
            if memo[i][j] != -1:
                return memo[i][j]
            
            memo[i][j] = grid[i][j] + min(minP(i, j + 1), minP(i + 1, j))
            return memo[i][j]
        
        
        return minP(0, 0)
