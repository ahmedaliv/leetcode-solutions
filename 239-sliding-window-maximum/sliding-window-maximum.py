from heapq import heappop, heappush
# from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        max_heap = []
        for i,num in enumerate(nums):
            heappush(max_heap,(-nums[i],i))

            # remove all elements outside the window
            while max_heap[0][1] <= i-k:
                heappop(max_heap)
            # if we're done with the window
            if i >= k-1:
                res.append(-max_heap[0][0])
        return res