class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ans = 0
        for s in num_set:
            if s-1 in num_set:
                continue
            ln = 0
            while s in num_set:
                s+=1
                ln+=1
            ans = max(ans,ln)
        return ans