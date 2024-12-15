class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_e = nums[0]
        max_diff = -1
        for i in range (1,len(nums)):
            if(nums[i]>min_e):
                max_diff= max(nums[i]-min_e,max_diff)
            else:
                min_e = nums[i]
                
        return max_diff