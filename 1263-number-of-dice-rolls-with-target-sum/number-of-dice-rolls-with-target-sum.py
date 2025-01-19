class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        memo = {}
        def f(idx,t):
            if t < 0 :
                return 0
            if idx == n:  # If we've used all dice
                return 1 if t == 0 else 0  # Only valid if target is exactly 0

            if (idx,t) in memo:
                return memo[(idx,t)]

            total =0 
            for j in range(1,k+1):
                total += f(idx+1,t-j) 
                total %= 10**9 + 7
            memo[(idx,t)] = total
            return total

        return f(0,target)