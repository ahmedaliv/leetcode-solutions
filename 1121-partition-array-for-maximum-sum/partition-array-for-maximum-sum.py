class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [-1]* len(arr)
        def f (i):
            if i == len(arr):
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = float('-inf')
            mx = float('-inf')
            for idx in range(i,i+k):
                if idx == len(arr):
                    break
                mx = max(mx,arr[idx])
                l = idx - i +1
                dp[i] = max(dp[i],l*mx + f(idx+1) )
            return dp[i]
        return f(0)
                