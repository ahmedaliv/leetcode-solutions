class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        flips = 0
        onesCount = 0

        for c in s:
            if c == '0':
                if onesCount == 0:
                    continue
                else:
                    flips = min(flips+1,onesCount)
            else:
                onesCount +=1
        return flips
