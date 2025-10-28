class Solution:
    def trap(self, height: List[int]) -> int:
        # the main idea is to compute the left_max,right_max for each index and minmize between them
        # then subtract the current height for that index to get the trapped water
        # def get_left_max():
        #     left_max = height[:]
        #     for i in range(1,len(height)):
        #         left_max[i] = max(left_max[i-1],height[i]) 
        #     return left_max
        # left_max = get_left_max()
        # def get_right_max():
        #     right_max = height[:]
        #     for i in range(len(height)-2,-1,-1):
        #         right_max[i] = max(right_max[i+1],height[i])
        #     return right_max
        # right_max = get_right_max()
        # trapped = 0
        # for i in range(len(height)):
        #     trapped += min(left_max[i],right_max[i]) - height[i]
        # return trapped
        #---------------------------
        #other idea is to split the array based on the max value idx
        # so that you always know the right_max for the first part and the left_max for the second part
        # and compute the trapped water for each split
        #-----------------
        # other idea is to use 2 pointers shrink style
        # you maintain cur_left_max,cur_right_max and 2 pointer left,right
        # the key part here that there will be unknown values in the middle, but you won't care
        # because for example the value at left index if it is 20 and the right_max is 70
        # 70 > 20 we don't care as now we are trapped by the 20 on the left side 
        # same thing for the right
        n = len(height)
        if n < 3:
            return 0 

        result, left, right = 0, 1, n-2
        left_max = height[0]
        right_max = height[n-1]

        while left <= right:
            if left_max <= right_max:
                left_max = max(left_max, height[left])
                result += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                result += right_max - height[right]
                right -= 1

        return result

