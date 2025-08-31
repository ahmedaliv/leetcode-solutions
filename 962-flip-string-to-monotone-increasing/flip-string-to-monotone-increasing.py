class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        prefixOnes = [0] * (n + 1)   # +1 to handle prefixOnes[0] = 0

        for i in range(1, n + 1):
            prefixOnes[i] = prefixOnes[i-1] + (1 if s[i-1] == '1' else 0)
        suffixZeros = [0] * (n + 1)  # +1 to handle suffixZeros[n] = 0
        for i in range(n-1,-1,-1):
            suffixZeros[i] = suffixZeros[i+1] + (1 if s[i] == '0' else 0)

        flips = float('inf')
        for i in range(n+1):
            flips = min(flips,prefixOnes[i]+suffixZeros[i])
        return flips