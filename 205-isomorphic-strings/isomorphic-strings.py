class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp1 = collections.defaultdict(int)
        mp2= collections.defaultdict(int)
        n = len(s)
        m = len(t)
        if n!=m:
            return False
            
        for i in range(n):
            ch1 = s[i]
            ch2 = t[i]
            if mp1[ch1] and  mp1[ch1]!=ch2:
                return False
            if mp2[ch2] and  mp2[ch2]!=ch1:
                return False
            mp1[ch1]=ch2
            mp2[ch2]=ch1
        return True