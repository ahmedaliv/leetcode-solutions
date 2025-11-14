class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stk = []
        unmatched = 0
        for c in s:
            if c == '(':
                stk.append(c)
            else: 
                if stk:
                    stk.pop()
                else:
                    unmatched += 1
        return unmatched + len(stk)
