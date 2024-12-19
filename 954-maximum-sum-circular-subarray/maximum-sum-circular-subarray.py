class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        arr_sum = sum(nums)
        best_max = self.maxSubArr(nums)
        best_min = float('inf')
        cur_sum = 0
        for num in nums:
            cur_sum += num
            best_min = min (best_min,cur_sum)
            if cur_sum > 0:
                cur_sum = 0
        
        if best_min == arr_sum:
            return best_max
        else:
            return max(best_max,arr_sum - best_min)
    def maxSubArr(self,nums):
        best_max = float('-inf')
        cur_sum = 0
        for num in nums:
            cur_sum += num
            best_max = max(best_max,cur_sum)
            if cur_sum < 0:
                cur_sum = 0
        return best_max