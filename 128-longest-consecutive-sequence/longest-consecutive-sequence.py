class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h_t = set()
        for n in nums:
            h_t.add(n)
        best = 0
        for n in h_t:
            if n-1 in h_t:
                continue
            l = 0
            while n in h_t:
                n+=1
                l +=1
            best = max(best,l)
        return best
                
        