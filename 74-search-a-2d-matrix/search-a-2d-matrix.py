class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        # Binary Search
        l = 0 
        r = m*n -1
        while l<=r:
            mid = (l+r)//2

            #convert to a 2d index 
            row = mid // n
            col = mid % n 
            mid_value = matrix[row][col]
            
            if mid_value == target:
                return True
            elif mid_value > target:
                r = mid - 1 
            else:
                l = mid + 1
        return False