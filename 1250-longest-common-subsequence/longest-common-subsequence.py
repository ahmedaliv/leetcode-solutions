class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1] * len(text2) for _ in range(len(text1))]
        def lcs(i,j):
            if i<0 or j<0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if text1[i] == text2[j]:
                dp[i][j] = 1 + lcs(i-1,j-1)
                return dp[i][j]
            # pick from t1 only
            p1 = lcs(i-1,j)
            #pick from t2 only
            p2 = lcs(i,j-1)

            dp[i][j] = max(p1,p2)
            return dp[i][j]
        return lcs(len(text1)-1,len(text2)-1)