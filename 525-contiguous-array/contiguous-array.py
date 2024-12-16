class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = 0 
        hash_map = {0:-1} # to handle subarrays starting from the start
        sum = 0

        for i,num in enumerate(nums):
            if num ==1:
                sum +=1
            else:
                sum -=1
            if sum in hash_map:
                res= max(res,i-hash_map[sum])
            else:
                hash_map[sum]=i
        return res