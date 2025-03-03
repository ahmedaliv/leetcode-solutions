from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        
        def f(sc, sr, ec, er):
            if sr > er or sc > ec:
                return

            for i in range(sc, ec + 1):
                result.append(matrix[sr][i])
            
            for i in range(sr + 1, er + 1):
                result.append(matrix[i][ec])

            if sr < er:
                for i in range(ec - 1, sc - 1, -1):
                    result.append(matrix[er][i])
            
            if sc < ec:
                for i in range(er - 1, sr, -1):
                    result.append(matrix[i][sc])
            
            f(sc + 1, sr + 1, ec - 1, er - 1)

        if matrix:
            f(0, 0, len(matrix[0]) - 1, len(matrix) - 1)
        
        return result
