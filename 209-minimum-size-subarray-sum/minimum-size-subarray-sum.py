class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # best_len = float('inf')
        # l = 0
        # cur_sum = 0
        # for r in range(len(nums)):
        #     cur_sum += nums[r]
        #     while cur_sum >= target:
        #         best_len = min(best_len,r-l+1)
        #         cur_sum -= nums[l]
        #         l+=1

        # return best_len if best_len != float('inf') else 0
        best_len = float('inf')
        n = len(nums)
        prefix_sum = [0]*n
        prefix_sum[0] = nums[0]
        for i in range(1,n):
            prefix_sum[i] = nums[i] + prefix_sum[i-1]
        # [2,5,6,7,11,14]

        for i in range(n):
            # sum of subarray nums[i..j] >= target
            # prefix_sum[j] - prefix_sum[i-1] >= target
            offset = prefix_sum[i-1] if i > 0 else 0
            target_sum = target + offset

            # find first j such that prefix_sum[j] >= target_sum
            j = bisect.bisect_left(prefix_sum, target_sum)
            if j < n:
                best_len = min(best_len, j - i + 1)
        return best_len if best_len != float('inf') else 0