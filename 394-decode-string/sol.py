class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        cur_str = ""
        for char in s:
            if char.isdigit():
                num = num*10 + int(char)
            elif char == '[':
                stack.append((cur_str,num))
                cur_str,num = "",0
            elif char == ']':
                prev_str,rep_count = stack.pop()
                cur_str = prev_str + rep_count * cur_str
            else:
                cur_str+= char
        return cur_str
