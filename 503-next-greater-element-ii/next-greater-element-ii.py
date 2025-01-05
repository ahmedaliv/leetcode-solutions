class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        s = []
        res = [-1]*len(nums)
        for i in range(2*len(nums)):
            while s and nums[s[-1]] < nums[i%len(nums)]:
                res[s[-1]] = nums[i%len(nums)]
                s.pop()
            
            if i < len(nums):
                s.append(i)
        return res