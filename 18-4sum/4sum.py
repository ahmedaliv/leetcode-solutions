class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = set()
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                l, r = j + 1, n - 1
                while l < r:
                    ans = nums[i] + nums[j] + nums[l] + nums[r]
                    if ans == target:
                        res.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
                    elif ans < target:
                        l += 1
                    else:
                        r -= 1
        return [list(q) for q in res]
