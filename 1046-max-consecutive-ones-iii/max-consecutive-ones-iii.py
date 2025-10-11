class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        best = 0 
        zeroes = 0
        for end in range(len(nums)):
            if not nums[end]:
                zeroes += 1
                
                while zeroes > k:
                    zeroes -= (nums[start] == 0) 
                    start += 1
            best = max(best,end-start+1)

        return best