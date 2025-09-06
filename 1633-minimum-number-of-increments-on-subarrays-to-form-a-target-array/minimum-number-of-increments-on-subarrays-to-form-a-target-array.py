
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)
        ans = target[0]
        for i in range(1,n):
            ans += max(0,target[i]-target[i-1])
        return ans