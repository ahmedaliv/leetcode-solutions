class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        i = l - 2
        while i>=0 and nums[i] >= nums[i+1]:
            i -= 1
        # if not the whole array (because in this case we just return the original one(sorted))
        # first perm
        if i >= 0 :
            # find the successor of the parent to the perm. we found
            j = l -1 
            while nums[j] <= nums[i]:
                j -= 1
            nums[i],nums[j] = nums[j],nums[i]
        nums[i + 1:] = reversed(nums[i + 1:])