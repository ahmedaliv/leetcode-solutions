import heapq
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        #O(NlogN)
        # nums.sort()
        # n = len(nums)
        # c1 = nums[n-1] * nums[n-2] * nums[n-3]
        # c2 = nums[n-1] * nums[0] * nums[1]
        # return max(c1,c2)

        # can we get O(N)
        # yes by getting these 5 values ourselves
        # either by using heap or if/else inside the loop
        # let's go with heap (this o(n) because nlargest,nsmallest is O(NlogK) where k is the number of selected elements) -> it builds a heap with k elements and start iterating over the elements to check
        largest = heapq.nlargest(3,nums)
        smallest = heapq.nsmallest(2,nums)
        return max(largest[0]*largest[1]*largest[2],largest[0] * smallest[0]*smallest[1])