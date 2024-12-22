class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        t = sum(nums) // 2
        dp = [[-1] * (t+1) for _ in range(len(nums))]
        def ps(i,s):
            if s < 0:
                return False
            if s == 0:
                return True
            
            if i == len(nums):
                return False
            if dp[i][s]!=-1:
                return dp[i][s]
            if(ps(i+1,s)):
                dp[i][s] = True
                return dp[i][s]
            dp[i][s]= ps(i+1,s-nums[i])
            return dp[i][s]
        return ps(0,t)

            