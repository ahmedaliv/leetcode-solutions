class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <=1:
            return 0
        n = len(nums)
        start = 0 
        ans = 0
        total = 1
        for end in range(n):
            total *= nums[end]
            while total >= k:
                total //= nums[start]
                start+=1
            ans += end - start +1
        return ans