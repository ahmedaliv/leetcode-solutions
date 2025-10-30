class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr_s = ptr_t = 0
        n = len(s)
        m = len(t)
        while ptr_s < n and ptr_t < m:
            if s[ptr_s] == t[ptr_t]:
                ptr_s+=1
                ptr_t+=1
            else:
                ptr_t+=1
        return True if ptr_s == n else False