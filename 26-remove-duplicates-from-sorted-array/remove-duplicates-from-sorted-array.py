class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dup_ptr = 0
        for j in range(len(nums)):
            if nums[dup_ptr] == nums[j]:
                continue
            else:
                dup_ptr+=1
                nums[dup_ptr],nums[j] = nums[j],nums[dup_ptr]
        return dup_ptr +1