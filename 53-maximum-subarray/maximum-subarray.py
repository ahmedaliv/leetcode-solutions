class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = float('-inf')
        def max_starting(arr,i):
            nonlocal max_so_far
            if i == len(arr)-1:
                max_so_far = max(max_so_far,arr[i])
                return arr[i]
            max_sum_start_i_p_1 = max_starting(arr,i+1)
            max_sum_start_i = max(arr[i],max_sum_start_i_p_1+arr[i])

            max_so_far = max(max_sum_start_i,max_so_far)
            
            return max_sum_start_i
        max_starting(nums,0)
        return max_so_far
