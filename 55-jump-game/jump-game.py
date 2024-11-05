class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_reachable_index = 0
        for i in range(len(nums)):
            if i > last_reachable_index:
                return False

            last_reachable_index = max(last_reachable_index, i+nums[i])
            
            if(last_reachable_index>= (len(nums)-1)):
                return True