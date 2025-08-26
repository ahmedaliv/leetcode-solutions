from collections import defaultdict

class Solution:
    def minDeletions(self, s: str) -> int:
        deletions = 0
        lfs = float('inf')
        h_t = defaultdict(int)
        for c in s:
            h_t[c] += 1
        freq_values = sorted(h_t.values(), reverse=True)
        
        for f in freq_values:
            allowed = min(f,lfs-1)
            if allowed < 0:
                allowed = 0
            deletions += f - allowed
            lfs = allowed
        return deletions