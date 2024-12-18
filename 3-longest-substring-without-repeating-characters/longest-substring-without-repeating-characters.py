class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0 

        substr = ''
        start = 0
        char_index = {} # to keep track of where the char last appeared
        for end in range(len(s)):
            if s[end] in char_index and char_index[s[end]] >= start:
                start = char_index[s[end]] + 1
            char_index[s[end]] = end
            best = max(best,end-start+1)
        return best