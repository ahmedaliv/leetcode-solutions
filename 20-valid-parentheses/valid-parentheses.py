class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        par_mapping = {'(':')','[':']','{':'}'}
        
        for c in s:
            if c in par_mapping:
                stk.append(c)
            else:
                if not stk or par_mapping[stk.pop()] != c:
                    return False
        
        return not stk