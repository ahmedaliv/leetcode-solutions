class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def transpose(m):
            n = len(m)
            for r in range(n):
                for c in range(r+1,n):
                    m[r][c],m[c][r] = m[c][r],m[r][c]
        def reflect(m):
            n = len(m)
            for c in range(int(n/2)):
                for r in range(n):
                    m[r][c],m[r][n-c-1] = m[r][n-c-1],m[r][c]
        transpose(matrix)
        reflect(matrix)

