class Solution:
    def integerBreak(self, n: int) -> int:
        #special cases instead of handling it in the dp approach itself (becase of the constrain that it should be divided to <= 2 parts)
        # Complexity T-> O(N^2), M -> O(N)
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
