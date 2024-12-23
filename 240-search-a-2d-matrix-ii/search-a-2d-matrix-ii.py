class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False 
        
        cols = len(matrix[0])
        row, col = 0, cols - 1  

        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True  
            elif matrix[row][col] < target:
                row += 1  
            else:
                col -= 1  

        return False 
