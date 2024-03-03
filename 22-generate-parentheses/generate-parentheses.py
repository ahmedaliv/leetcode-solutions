class Solution:
    def is_valid(self, s):
        balance = 0
        for char in s:
            if char == '(':
                balance += 1
            elif char == ')':
                balance -= 1
            if balance < 0:
                return False
        return balance == 0

    def generateParenthesis(self, n):
        def backtrack(s):
            if len(s) == 2 * n:
                if self.is_valid(s):
                    result.append(s)
                return
            
            backtrack(s + '(')
            backtrack(s + ')')
        
        result = []
        backtrack('')
        return result

