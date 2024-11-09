class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        cache = [-1] * n

        def min_jumps_from_index(index):
            if index >= n - 1:
                return 0

            if cache[index] != -1:
                return cache[index]

            min_jumps = float('inf')
            max_jump = nums[index]
            for step in range(1, max_jump + 1):
                next_index = index + step
                jumps_needed = 1 + min_jumps_from_index(next_index)
                min_jumps = min(min_jumps, jumps_needed)

            cache[index] = min_jumps
            return min_jumps

        return min_jumps_from_index(0)