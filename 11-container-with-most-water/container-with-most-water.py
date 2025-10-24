class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        best = 0
        while l<r:
            best = max(best,min(height[l],height[r])*(r-l))
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return best