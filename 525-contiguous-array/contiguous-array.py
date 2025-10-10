class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_table = defaultdict(int)
        # we store first occurence 
        prefix_table[0] = -1 
        prefix_sum = res =0
        for i in range(len(nums)):
            # convert to zeroes to -1 (to know where sum 0  happen ( to be able to use prefix sum))
            prefix_sum += nums[i] if nums[i] else -1
            # keep earliest index
            if prefix_sum not in prefix_table:
                prefix_table[prefix_sum] = i 
            else:
            # Whenever we see a prefix_sum again, the subarray between first occurrence and current index has equal number of 0s and 1s
                res = max(res,i- prefix_table[prefix_sum])
        return res