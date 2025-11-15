class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stk = []
        remove = set()
        for i,c in enumerate(s):
            if c == '(':
                stk.append(i)
            elif c == ')':
                if stk:
                    stk.pop()
                else:
                    remove.add(i)
        remove = remove.union(set(stk))
        return ''.join(c for i,c in enumerate(s) if i not in remove)
