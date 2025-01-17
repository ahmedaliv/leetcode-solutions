class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def f(am):
            if am ==0:
                return 0
            if am in memo:
                return memo[am]
            best = float('inf')
            for c in coins:
                if am>=c:
                    best = min(best,f(am-c)+1)
            memo[am] = best
            return best
        ans = f(amount)
        return -1 if ans == float('inf') else ans