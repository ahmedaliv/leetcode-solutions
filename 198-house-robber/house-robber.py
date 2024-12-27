class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        def rb(i):
            if i < 0:
                return 0
            #np
            if dp[i]!=-1:
                return dp[i]
            np = rb(i-1)
            #p
            p = rb(i-2) + nums[i]

            dp[i] = max(p,np)
            return dp[i]
        return rb(len(nums)-1)