import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        h_m = collections.defaultdict(int)
        m = len(t)
        n = len(s)
        for c in t:
            h_m[c] += 1
        
        best = float('inf')
        start, end, ss, best_start = 0, 0, 0, 0

        while end < n:
            if s[end] in h_m:
                # this is to only max the sum for the characters we need to just any one in the h_m
                if h_m[s[end]] > 0 :
                    ss += 1
                h_m[s[end]] -= 1
            while ss == m:
                if end - start +1 < best:
                    best_start = start
                    best = end -  start + 1

                if s[start] in h_m:
                    h_m[s[start]] += 1
                    # only subtract from the sum if and only if it will make the window invalid
                    # o.w : keep minimizing 
                    if  h_m[s[start]] > 0:
                        ss -=1
                start +=1
            end +=1

        if best == float('inf'):
            return ""
        return s[best_start:best_start + best]
