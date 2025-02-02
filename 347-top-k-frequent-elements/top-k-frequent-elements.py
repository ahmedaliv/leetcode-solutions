from heapq import heappop,heappush
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        h_m = {}
        for num in nums:
            h_m[num] = h_m.get(num,0) + 1
        for num,freq in h_m.items():
            heappush(heap,(freq,num))
            if len(heap)>k:
                heappop(heap)
        res = []
        while heap:
            res.append(heappop(heap)[1])
        return res