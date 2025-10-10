from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_table = defaultdict(int)
        prefix_table[0] = 1
        prefix_sum = res =0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            res += prefix_table[prefix_sum - k] 
            prefix_table[prefix_sum] += 1
        return res