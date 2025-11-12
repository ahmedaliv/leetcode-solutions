class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #Brute Force O(N^2)
        # best = 0
        # n = len(heights)
        # for i in range(n):
        #     min_height = heights[i]
        #     for j in range(i,n):
        #         min_height = min(min_height,heights[j])
        #         best = max(best, min_height * (j - i + 1))
        # return best
        n = len(heights)
        nx = self.next_lower_idx(heights)
        pv = self.prev_lower_idx(heights)
        best = 0
        for i in range(n):
            l = pv[i] + 1 
            r = nx[i] - 1
            best = max(best,heights[i]*(r-l+1))
        return best
    def next_lower_idx(self, arr):
        n = len(arr)
        stk = []
        res = [n] * n
        for i in range(n):
            while stk and arr[stk[-1]] > arr[i]:
                res[stk[-1]] = i 
                stk.pop()
            stk.append(i)
        return res
    def prev_lower_idx(self,arr):
        res = arr[::]
        res.reverse()
        res = self.next_lower_idx(res)
        res.reverse()
        n = len(res)
        for i in range(n):
            res[i] = n - res[i] - 1
        return res