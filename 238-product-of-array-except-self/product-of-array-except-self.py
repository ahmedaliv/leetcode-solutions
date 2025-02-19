class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_m = nums[0]
        n = len(nums)
        ans =[1]*n
        for i in range(1,n):
            ans[i] = pre_m
            pre_m *= nums[i]
        suf_m = nums[n-1]
        for i in range(n-2,-1,-1):
            ans[i] *= suf_m
            suf_m *= nums[i]
        return ans