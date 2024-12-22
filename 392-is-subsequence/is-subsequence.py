class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        i,j = 0 , 0
        while i < len(s) and j < len(t):
            if s[i]==t[j]:
                i += 1
                j +=1
            else:
                j += 1
        if i == len(s):
            return True
        else:
            return False
