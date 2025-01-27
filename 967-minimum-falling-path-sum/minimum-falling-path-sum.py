class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        memo = {}
        def f(r,c):
            # base cases
            if (r,c) in memo:
                return memo[(r,c)]
            if  c < 0  or c> cols-1:
                return float('inf')
            if r == rows-1:
                return matrix[r][c]
                
            d = f(r+1,c)
            dl =  f(r+1,c-1)
            dr = f(r+1,c+1)

            # return min
            memo[(r,c)] = matrix[r][c]+ min(d,dl,dr)
            return memo[(r,c)]
        return min(f(0,c) for c in range(cols))