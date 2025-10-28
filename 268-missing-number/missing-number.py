class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # using math formula -> sum of number from 0-> n is  n*(n+1) / 2
        # note that n*n may overflow if you're in another language like c++
        # n = len(nums)
        # return int((n*(n+1))/2-sum(nums)) 
        # xor based solution
        n = len(nums)
        res = n
        for i in range(n):
            res ^= i ^ nums[i]
        return res