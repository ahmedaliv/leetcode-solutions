class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def p(x,n):
            if n==0:
                return 1
            res = p(x,n//2)
            res *= res
            if n %2 !=0:
                res *=x
            return res
        if n < 0 :
            return 1 / p(x,-n)
        return p(x,n)
             