class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[[-1 for _ in range(2)] for _ in range (3)] for _ in range(len(prices))]
        def mx(i, lt, hs):
            if i == len(prices):
                return 0
            if dp[i][lt][hs] != -1:
                return dp[i][lt][hs]

            buy,sell,no_action =0,0,0
            if hs:
                no_action = mx(i + 1, 0, hs)
                sell = prices[i] + mx(i + 1, 1, 0)
                dp[i][lt][hs] =  max(sell, no_action)
            else:
                no_action = mx(i + 1, 0, hs)
                if lt != 1:
                    buy = -prices[i] + mx(i + 1, 2, 1)
                    dp[i][lt][hs] = max(buy, no_action)
                dp[i][lt][hs] = max(dp[i][lt][hs],no_action)
            return dp[i][lt][hs]
        return mx(0, 0, 0)
