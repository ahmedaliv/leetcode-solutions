class Solution:
    def minInsertions(self, s: str) -> int:
        dp = [[-1] * len(s) for _ in range(len(s))]
        def f(l,r):
            if l>=r:
                return 0
            if dp[l][r]!=-1:
                return dp[l][r]
            if s[l]==s[r]:
                return f(l+1,r-1)
            il = 1 + f(l,r-1)
            ir = 1 + f(l+1,r)
            dp[l][r] = min(il,ir)
            return dp[l][r]
        return f(0,len(s)-1)