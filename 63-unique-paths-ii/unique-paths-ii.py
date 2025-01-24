class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        def is_valid(i,j):
            return i < m and j < n and not obstacleGrid[i][j] 
        memo = {}
        def get_paths(r,c):
            if (r,c) in memo:
                return memo[r,c]
            if is_valid(r,c):
                if r == m-1 and c==n-1:
                    return 1
                down = get_paths(r+1,c)
                right= get_paths(r,c+1)
                memo[r,c]=  down+right
                return memo[r,c]
            memo[r,c] = 0
            return memo[r,c]
        return get_paths(0,0)