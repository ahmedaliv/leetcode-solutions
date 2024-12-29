class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        lds_dp = [-1] * n
        lis_dp = [-1] * n
        
        def lds(i):
            if lds_dp[i] != -1:
                return lds_dp[i]
            lds_dp[i] = 0
            for j in range(i + 1, n):
                if nums[j] < nums[i]:
                    lds_dp[i] = max(lds_dp[i], lds(j))
            lds_dp[i] += 1
            return lds_dp[i]
        
        def lis(i):
            if lis_dp[i] != -1:
                return lis_dp[i]
            lis_dp[i] = 0 
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    lis_dp[i] = max(lis_dp[i], lis(j))
            lis_dp[i] += 1
            return lis_dp[i]
        
        best = 0
        for i in range(0, n):
            i_lis, i_lds = lis(i), lds(i)
            if i_lis == 1 or i_lds == 1:  # Mountain must have at least one increasing and decreasing segment
                continue
            # -1 is for the common peak element
            cur = i_lis + i_lds - 1
            best = max(best, cur)
        
        return n - best
