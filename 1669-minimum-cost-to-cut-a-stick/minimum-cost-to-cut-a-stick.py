from typing import List

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.append(0)
        cuts.append(n)
        cuts.sort()
        memo = {}
        def f(i, j):
            if i > j:
                return 0
            if (i,j)  in memo:
                return memo[(i,j)]
            mc = float('inf')
            for idx in range(i, j + 1):
                cost = cuts[j + 1] - cuts[i - 1] + f(i, idx - 1) + f(idx + 1, j)
                mc = min(mc, cost)
            memo[(i,j)] = mc
            return mc
        
        return f(1, len(cuts) - 2)
