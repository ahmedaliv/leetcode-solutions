# from heapq import heappop, heappush
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        # max_heap = []
        # for i in range(len(nums)):
        #     heappush(max_heap,(-nums[i],i))
        #     # if the max element now in the heap (out of our window) remove it
        #     while max_heap[0][1] <= i -k:
        #         heappop(max_heap)
        #     # if we finished the current window, append the max. to the result
        #     # for k=3 the window is 0,1,2 so we do not append untill we at 2 (or 3 or 4 for the next windows) 
        #     if i >= k - 1:
        #         res.append(-max_heap[0][0])
        dq = deque()
        for i in range(len(nums)):
            # remove out of current window
            if dq and dq[0] < i-k+1:
                dq.popleft() 
            # All indices in dq are within the current window at this point.
            # Remove indices from the back whose values are smaller than nums[i]:
            #   - These elements cannot be the maximum in the current window,
            #     because nums[i] is larger and comes later (so it will dominate the window until it slides out).
            #   - They also cannot be the maximum in any future window that includes nums[i].
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            dq.append(i)

            # add the max to the result once the window is full
            if i >= k-1:
                res.append(nums[dq[0]])

        return res