class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_ptr = 0
        for cur_ptr in range(len(nums)):
            if nums[cur_ptr] == 0:
                continue
            else:
                nums[cur_ptr],nums[zero_ptr] = nums[zero_ptr],nums[cur_ptr]
                zero_ptr += 1
        