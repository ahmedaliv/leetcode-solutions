class Solution:
    def numSquares(self, n: int) -> int:
        dp = [-1]*(n+1)

        def ps(idx):
            if idx <=0:
                return 0

            if dp[idx]!=-1:
                return dp[idx]
            i = 1
            best = float('inf')
            while True:
                if i * i > idx:
                    break
                best = min(best,1+ps(idx-i*i))
                i +=1
            dp[idx] = best
            return dp[idx] 
        return ps(n)