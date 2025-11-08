class Solution:
    def simplifyPath(self, path: str) -> str:
        stk,tokens = [],path.split('/')
        for t in tokens:
            if t == '' or t == '.':
                continue
            
            if t == '..':
                if stk:
                    stk.pop()
            else:
                stk.append(t)
        

        return '/' + '/'.join(stk)
