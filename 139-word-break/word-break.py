class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [None] * len(s)
        def wb(pos):
            if(pos==len(s)):
                return True
            if(dp[pos] is not None):
                return dp[pos]
            
            for i in range(pos,len(s)):
                if(s[pos:i+1] in wordDict and wb(i+1)):
                    dp[pos] = True
                    return True
            dp[pos]= False
            return False
        wb(0)
        return dp[0]
        
        # Recursive (no memoization) -> gives TLE
        # def wb(pos):
        #     if (pos == len(s)):
        #         return True
            
            
        #     for i in range(pos,len(s)):
        #         if(s[pos:i+1] in wordDict  and wb(i+1)):
        #             return True
        #     return False
        # return wb(0)
            