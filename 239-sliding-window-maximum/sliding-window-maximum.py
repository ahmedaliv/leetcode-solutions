from heapq import heappop, heappush

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        res = []

        for i in range(len(nums)):
            heappush(max_heap,(-nums[i],i))
            # if the max element now in the heap (out of our window) remove it
            while max_heap[0][1] <= i -k:
                heappop(max_heap)
            # if we finished the current window, append the max. to the result
            # for k=3 the window is 0,1,2 so we do not append untill we at 2 (or 3 or 4 for the next windows) 
            if i >= k - 1:
                res.append(-max_heap[0][0])
        return res

