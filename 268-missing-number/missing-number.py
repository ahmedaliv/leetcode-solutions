class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # using math formula -> sum of number from 0-> n is  n*(n+1) / 2
        n = len(nums)
        return int((n*(n+1))/2-sum(nums)) 