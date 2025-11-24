# from heapq import heappop, heappush
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        dq = deque()
        for i,num in enumerate(nums):
            # remove out of bound
            # i-k+1 is the start of the window
            # let's say our start was 1 and we have k=3 and i=3
            # so that means 3-3+1 = 1 so anything below 1 should be removed
            while dq and dq[0] < i-k+1:
                dq.popleft()
            
            # remove anything smaller than the current element
            # because we want to always maintain the front to be the max, so we remove anything smaller from the back
            while dq and nums[dq[-1]] < num:
                dq.pop()
            dq.append(i)
            if i >= k-1:
                res.append(nums[dq[0]])
        return res