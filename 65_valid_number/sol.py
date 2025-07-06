class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        seen_digit = False
        seen_dot = False
        seen_e = False
        digit_after_e = True  
        

        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
                if seen_e:
                    digit_after_e = True
            elif char in ['E','e']:
                if seen_e or not seen_digit:
                    return False
                seen_e = True
                digit_after_e = False
            elif char == '.':
                if seen_dot or seen_e:
                    return False
                seen_dot = True
            elif char in ['+','-']:
                if i > 0 and s[i-1] not in ['e','E']:
                    return False
            else:
                return False
        return seen_digit and digit_after_e
