class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # this is gonna be solved using cyclic sort
        # so the algorithm is just loop over the numbers and then for each one
        # do cycles of -replacements or movements- to move it to its place
        # and after that check the number that's not in its correct place and return it  (or return n+1) if all in its place

        for i in range(n):
            #notice we only care about positive numbers
            while 0 < nums[i] <= n and nums[i] != nums[nums[i]-1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        for i in range(n):
            if nums[i] != i +1:
                return i+1
        return n + 1 