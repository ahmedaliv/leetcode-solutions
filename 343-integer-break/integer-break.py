class Solution:
    def integerBreak(self, n: int) -> int:
        if n==2 or n==3:
            return n-1
        dp = [-1]* (n +1)
        def f(n):
            if n ==1:
                return n
            if dp[n] != -1:
                return dp[n]
            best = n
            for i in range(1,n):
                best = max(best,i*f(n-i))
            dp[n] = best
            return dp[n]
        return f(n)