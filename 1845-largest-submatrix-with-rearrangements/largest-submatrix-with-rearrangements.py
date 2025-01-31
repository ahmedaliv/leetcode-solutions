class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        rows = len(matrix)
        cols = len(matrix[0])
        def next_lower(heights):
            n = len(heights)
            res = [n] * n
            s = []
            for i in range(n):
                while s and heights[s[-1]] > heights[i]:
                    res[s[-1]] = i
                    s.pop()
                s.append(i)
            return res
        
        def prev_lower(heights):
            n = len(heights)
            res = [-1] * n
            s = []
            for i in range(n-1, -1, -1):
                while s and heights[s[-1]] > heights[i]:
                    res[s[-1]] = i
                    s.pop()
                s.append(i)
            return res
        def largest_rect(heights):
            nl = next_lower(heights)
            pl = prev_lower(heights)
            n = len(heights)

            best = 0
            for i in range(n):
                left = pl[i] + 1
                right = nl[i] - 1
                best = max(best, heights[i] * (right - left + 1))
            
            return best
        # do prefix per column
        
        for c_idx in range(cols):
            for r_idx in range(1,rows):
                if matrix[r_idx][c_idx]:
                    matrix[r_idx][c_idx] += matrix[r_idx-1][c_idx]

        
        max_sub = 0
        for r_idx in range(rows):
            row = sorted(matrix[r_idx],reverse=True)
            max_sub = max(max_sub,largest_rect(row))
        return max_sub