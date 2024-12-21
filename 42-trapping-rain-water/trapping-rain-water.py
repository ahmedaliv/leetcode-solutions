class Solution:
    def trap(self, height: List[int]) -> int:
        
        l,r =0,len(height)-1
        l_m,r_m = 0 , 0
        trapped_water =0
        while l< r:
            if height[l] > l_m:
                l_m = height[l]
            else:
                trapped_water += l_m - height[l]        
            if height[r] > r_m:
                r_m = height[r]
            else:
                trapped_water += r_m - height[r]
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1  
        return trapped_water