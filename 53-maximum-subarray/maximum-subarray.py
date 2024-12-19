class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre_sum = 0
        max_sum = float('-inf')
        min_sum = float('inf')
        for i,num in enumerate(nums):
            pre_sum += num
            max_sum = max(max_sum,pre_sum)
            if i:
                max_sum = max(max_sum,pre_sum-min_sum)
            min_sum = min(min_sum,pre_sum)
        
        return max_sum