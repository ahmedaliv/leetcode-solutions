from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)
        steps = 0

        for char in count_t:
            extra = count_t[char] - count_s.get(char, 0)
            if extra > 0:
                steps += extra

        return steps
