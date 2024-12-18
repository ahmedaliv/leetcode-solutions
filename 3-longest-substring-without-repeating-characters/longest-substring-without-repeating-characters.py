class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0 

        substr = ''
        for start in range(len(s)):
            for end in range(start,len(s)):
                if s[end] not in substr:
                    substr += s[end]
                else:
                    substr=''
                    break
                best = max(best,len(substr))
        return best