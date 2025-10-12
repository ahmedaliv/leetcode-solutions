class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # TRY BRUTE FORCE
        # O(N^2)
        # best = float('-inf')
        # for start in range(len(nums)):
        #     cur_sum = 0
        #     for end in range(start,len(nums)):
        #         cur_sum += nums[end]
        #         best = max(cur_sum,best)
        # return best
        # but here we're doing some reduandant work 
        # [-2,1,-3,4,-1,2,1,-5,4]
        # -2 + 1 + -3 now we at 4 , u will see that 4 is bigger than all of these prev. elements so start from there
        # prefix sum approach
        # why prefix sum is doable here ? because range cancellation can be applied here
        # best = float('-inf')
        # prefix_sum = 0
        # min_prefix_sum_so_far = float('inf')
        # for i in range(len(nums)):
        #     prefix_sum += nums[i]
        #     # the whole window
        #     best = max(best,prefix_sum)
        #     if i:
        #         # window between min prev prefix sum and cur. prefix sum
        #         best = max(best,prefix_sum-min_prefix_sum_so_far)
            
        #     min_prefix_sum_so_far = min(prefix_sum,min_prefix_sum_so_far)
        # return best
        best = float('-inf')

        # start = 0 
        sum_so_far = 0
        for end in range(len(nums)):
            sum_so_far = max(nums[end],sum_so_far+nums[end])
            # if empty subarray is allowed 
            # sum_so_far = max(0,sum_so_far+nums[end]) 
            best = max(best,sum_so_far)
        return best