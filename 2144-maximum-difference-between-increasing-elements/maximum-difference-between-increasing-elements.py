class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = float('-inf')

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] > nums[i]:
                    ans = max(nums[j]-nums[i],ans)
                    
        return ans if ans != float('-inf') else -1
