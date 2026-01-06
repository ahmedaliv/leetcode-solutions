class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum_end_i = 0
        max_sum = float('-inf')
        for i in range(len(nums)):
            max_sum_end_i = max(nums[i],max_sum_end_i+nums[i])
            max_sum = max(max_sum,max_sum_end_i)
        return max_sum