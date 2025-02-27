import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        h_m = collections.defaultdict(int)
        m = len(t)
        for c in t:
            h_m[c] += 1
        
        best = float('inf')
        st, en, ss, start = 0, 0, 0, 0
        
        while en < len(s):
            if s[en] in h_m:
                if h_m[s[en]] > 0:
                    ss += 1
                h_m[s[en]] -= 1
            
            while ss == m:
                if en - st + 1 < best:
                    best = en - st + 1
                    start = st
                
                if s[st] in h_m:
                    h_m[s[st]] += 1
                    if h_m[s[st]] > 0:
                        ss -= 1
                st += 1
            
            en += 1
        
        if best == float('inf'):
            return ""
        return s[start:start + best]
