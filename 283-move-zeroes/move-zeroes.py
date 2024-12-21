class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zero_pointer = 0  
        non_zero_pointer = 0  

        while non_zero_pointer < n:
            if nums[zero_pointer] == 0 and nums[non_zero_pointer] != 0:
                nums[zero_pointer], nums[non_zero_pointer] = nums[non_zero_pointer], nums[zero_pointer]
                zero_pointer += 1 
            if nums[zero_pointer] != 0:
                zero_pointer += 1
            non_zero_pointer += 1

        return nums