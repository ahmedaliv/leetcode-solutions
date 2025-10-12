class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        best_max = float('-inf')
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum = max(nums[i],cur_sum+nums[i])  
            best_max = max(best_max,cur_sum)
        best_min = float('inf')
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum = min(nums[i],cur_sum+nums[i])  
            best_min = min(best_min,cur_sum)
        ss = sum(nums)
        # special case if all elements are negative, just return the maximum element
        if ss == best_min:
            return best_max
        # normal: return the max between normal maximum subarray and whole array excluding the minmum array
        
        return max(best_max,ss-best_min)