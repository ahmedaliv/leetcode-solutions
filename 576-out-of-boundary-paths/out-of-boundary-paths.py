class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        memo = {}

        def max_out(cur_r, cur_c, steps):
            if steps > maxMove:
                return 0
            if (cur_r, cur_c, steps) in memo:
                return memo[(cur_r, cur_c, steps)]
            if cur_r < 0 or cur_r >= m or cur_c < 0 or cur_c >= n:
                return 1
            
            # Try the 4 directions and apply modulo
            l = max_out(cur_r, cur_c - 1, steps + 1) % MOD
            u = max_out(cur_r - 1, cur_c, steps + 1) % MOD
            d = max_out(cur_r + 1, cur_c, steps + 1) % MOD
            r = max_out(cur_r, cur_c + 1, steps + 1) % MOD

            memo[(cur_r, cur_c, steps)] = (l + u + d + r) % MOD
            return memo[(cur_r, cur_c, steps)]

        return max_out(startRow, startColumn, 0)
