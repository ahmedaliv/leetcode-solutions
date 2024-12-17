class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        best = 0 
        zeros = 0
        start = 0 
        for end in range(len(nums)):
            if nums[end] == 0:
                zeros += 1
                while(zeros > k):
                    zeros -= (nums[start] == 0)
                    start += 1
            best = max(best,end-start+1)
        return best