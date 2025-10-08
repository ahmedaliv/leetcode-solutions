class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float('-inf')
        max_so_far = nums[n-1]
        for i in range(n-2,-1,-1):
            if max_so_far > nums[i]:
                ans = max(ans,max_so_far-nums[i])
            max_so_far = max(max_so_far,nums[i])
        return ans if ans != float('-inf') else -1
