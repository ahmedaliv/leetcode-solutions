class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        best = 0
        stack.append(0)
        opened = 0
        for i,c in enumerate(s):
            if c == "(":
                stack.append(0)
                opened +=1
            else:
                if opened:
                    child = stack[-1] + 2
                    stack.pop()
                    parent = stack[-1] + child
                    stack.pop()
                    stack.append(parent)
                    opened -=1
                    best = max(best,parent)
                else:
                    stack.append(0)
                    opened = 0
        return best