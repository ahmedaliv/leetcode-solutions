class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1]*len(cost)
        def f(i):
            if i >= len(cost):
                return 0
            if dp[i] != -1:
                return dp[i]
            #m1
            m1 = f(i+1) 
            #m2
            m2 = f(i+2) 
            dp[i]= min(m1,m2) + cost[i]
            return dp[i]
        return min(f(0),f(1))