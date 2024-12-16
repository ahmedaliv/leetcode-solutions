class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # a solution using the fixed sliding window approach
        hash_set = set()
        for i,num in enumerate(nums):
            if num in hash_set:
                return True
            hash_set.add(num)
            
            # remove the first one (kick it out of the k-window)
            if(len(hash_set)>k):
                hash_set.remove(nums[i-k])
        return False