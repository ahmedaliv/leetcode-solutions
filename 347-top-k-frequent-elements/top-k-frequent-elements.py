class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        h_m = defaultdict(int)
        for num in nums:
            h_m[num] += 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for num,freq in h_m.items():
            buckets[freq].append(num)
        
        res = []
        for i in range(len(buckets) -1,0,-1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res