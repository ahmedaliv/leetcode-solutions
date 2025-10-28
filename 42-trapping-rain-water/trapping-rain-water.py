class Solution:
    def trap(self, height: List[int]) -> int:
        def get_left_max():
            left_max = height[:]
            for i in range(1,len(height)):
                left_max[i] = max(left_max[i-1],height[i]) 
            return left_max
        left_max = get_left_max()
        def get_right_max():
            right_max = height[:]
            for i in range(len(height)-2,-1,-1):
                right_max[i] = max(right_max[i+1],height[i])
            return right_max
        right_max = get_right_max()
        trapped = 0
        for i in range(len(height)):
            trapped += min(left_max[i],right_max[i]) - height[i]
        return trapped