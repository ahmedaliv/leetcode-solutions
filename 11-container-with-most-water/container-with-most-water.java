class Solution {
    public static int maxArea(int[] height) {
        int maxArea = 0;
        int left = 0;
        int right = height.length - 1;
        while (left < right) {
        int width = right - left;
        int currentArea = Math.min(height[left], height[right]) * width;
        maxArea = Math.max(maxArea, currentArea);
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
        }
        return maxArea;
    }
}