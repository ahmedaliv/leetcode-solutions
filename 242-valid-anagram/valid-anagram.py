class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        for char in t:
            if freq.get(char, 0) == 0:
                return False
            freq[char] -= 1
        return True
