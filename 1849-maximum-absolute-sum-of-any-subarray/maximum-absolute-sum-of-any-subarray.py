class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        best_max = 0 
        cur_sum = 0
        for num in nums:
            cur_sum +=num
            best_max = max(best_max,cur_sum)
            if cur_sum < 0 :
                cur_sum = 0
        best_min = float('inf')
        cur_sum = 0
        for num in nums:
            cur_sum +=num
            best_min = min (best_min,cur_sum)
            if cur_sum > 0 :
                cur_sum = 0
        return max(abs(best_min),abs(best_max))