class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        best_max = float('-inf')
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum = max(0,cur_sum+nums[i])  
            best_max = max(best_max,cur_sum)
        best_min = float('inf')
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum = min(0,cur_sum+nums[i])  
            best_min = min(best_min,cur_sum)
        return max(-best_min,best_max)