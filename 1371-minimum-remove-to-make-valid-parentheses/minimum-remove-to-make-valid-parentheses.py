class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_idxs = []
        close_idxs = []
        res = ""
        for i,c in enumerate(s):
            if c == "(":
                open_idxs.append(i)
            elif c == ")":
                if open_idxs:
                    open_idxs.pop()
                else:
                    close_idxs.append(i)
        ans = ""
        for i in range(len(s)):
            if i in open_idxs or i in close_idxs:
                continue
            ans += s[i]
        return ans
