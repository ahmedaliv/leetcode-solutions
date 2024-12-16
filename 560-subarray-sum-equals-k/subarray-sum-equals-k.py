class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0 
        hash_map = {0:1}
        pre_sum = 0
        for num in nums:
            pre_sum += num
            # is there any subarray that by removing it we can get our target ?
            # and if there's , how many ? (add the number to the answer)
            if(pre_sum - k) in hash_map:
                res += hash_map[pre_sum-k]
            hash_map[pre_sum] = hash_map.get(pre_sum, 0) + 1
        return res