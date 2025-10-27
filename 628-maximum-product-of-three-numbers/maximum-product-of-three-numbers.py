class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        c1 = nums[n-1] * nums[n-2] * nums[n-3]
        c2 = nums[n-1] * nums[0] * nums[1]
        return max(c1,c2)