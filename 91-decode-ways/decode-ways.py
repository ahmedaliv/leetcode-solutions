class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def f(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            if i == len(s) -1 :
                return 1

            # decode 2 chars
            p2 = 0
            if i +1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                p2 =f(i+2)
            # decode 1 char
            p1 =f(i+1)
            memo[i] = p1+p2
            return p2 + p1
        return f(0)