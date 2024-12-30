class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        dp = [[-1]*len(word2) for _ in range(len(word1))]
        def dis(i,j):
            if i == -1  or j ==-1:
                return max(i,j) + 1
            if dp[i][j] != -1:
                return dp[i][j]

            if word1[i] == word2[j]:
                return dis(i-1,j-1)
            change = 1 + dis(i-1,j-1)
            delete = 1 + dis(i-1,j)
            insert = 1 + dis(i,j-1)
            dp[i][j] = min(change,delete,insert) 
            return dp[i][j]
        return dis(len(word1)-1,len(word2)-1)