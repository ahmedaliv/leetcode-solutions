from heapq import heappop, heappush

class Solution:
    def maxSlidingWindow(self, nums, k: int):
        max_heap = []
        res = []
        
        for i in range(len(nums)):
            heappush(max_heap, (-nums[i], i))
            
            while max_heap[0][1] <= i - k:
                heappop(max_heap)

            if i >= k - 1:
                res.append(-max_heap[0][0])
        
        return res