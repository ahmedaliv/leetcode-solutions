class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        best_len = float('inf')
        l = 0
        cur_sum = 0
        for r in range(len(nums)):
            cur_sum += nums[r]
            while cur_sum >= target:
                best_len = min(best_len,r-l+1)
                cur_sum -= nums[l]
                l+=1

        return best_len if best_len != float('inf') else 0
