class Solution:
    def findMaxLength(self, nums):
        best = 0
        h_t = {}
        p_s = 0

        for i in range(len(nums)):
            if nums[i]:
                p_s+=1
            else:
                p_s-=1
            
            if p_s == 0:
                best = max(best,i+1)
            elif p_s in h_t:
                best = max(best,i-h_t[p_s])
            else:
                h_t[p_s] = i
        return best
                