from collections import defaultdict

class Solution:
    def minDeletions(self, s: str) -> int:
        deletions = 0
        h_t = defaultdict(int)
    
        for c in s:
            h_t[c] += 1
        
        used = set() 
        
        for f in h_t.values():
            while f > 0 and f in used:
                f -= 1
                deletions += 1
            used.add(f)
        
        return deletions
