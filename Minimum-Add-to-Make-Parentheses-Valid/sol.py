class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        min_req = 0 
        open_p = 0
        for c in s:
            if c =="(":
                open_p+=1
            else:
                if open_p > 0:
                    open_p -= 1
                else:
                    min_req +=1
        return min_req + open_p        
