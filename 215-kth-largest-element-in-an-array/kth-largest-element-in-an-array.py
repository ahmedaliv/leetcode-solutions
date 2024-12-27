import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            if len(heap) <= k or num > heap[0]:
                heapq.heappush(heap,num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heapq.heappop(heap)