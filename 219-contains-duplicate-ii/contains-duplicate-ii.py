class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        h_set = set()
        for i in range(len(nums)):
            if nums[i] in h_set:
                return True

            h_set.add(nums[i])

            if len(h_set) > k :
                h_set.remove(nums[i-k])
        return False