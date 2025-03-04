class Solution:

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        
        for i in range(len(nums) - 2):  
            # If the smallest possible sum is already worse, stop early
            min_sum = nums[i] + nums[i+1] + nums[i+2]
            if min_sum >= target + abs(target - closest_sum):
                return closest_sum
            
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                if current_sum > target:
                    right -= 1
                else:
                    left += 1
        
        return closest_sum
