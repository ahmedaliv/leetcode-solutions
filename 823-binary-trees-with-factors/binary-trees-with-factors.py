class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        memo = {}
        def cnt_trees(x):
            if x in memo:
                return memo[x]
            total = 1
            for n in arr:
                if x % n == 0 and x // n in arr:
                    # count all the combinations 
                    # e.g if root is 10 and and subtrees are 5,2 so count as 5 the root and 2 as the root then multiply to get all the combinations ...
                    total += cnt_trees(n) * cnt_trees(x//n)
            memo[x] = total
            return total
        h_t = set()
        for n in arr:
            h_t.add(n)
        total = 0
        for n in h_t:
            total += cnt_trees(n)
        MOD = 10**9 + 7
        return total % MOD

 
