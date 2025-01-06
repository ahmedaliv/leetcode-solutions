class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hs_t = {}
        ht_s = {}
        for i in range(len(s)):
            if (s[i] in hs_t and hs_t[s[i]] != t[i]) or (t[i] in ht_s and ht_s[t[i]] != s[i]):
                return False
            hs_t[s[i]] = t[i]
            ht_s[t[i]] = s[i]
        return True
