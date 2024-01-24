class Solution {
public  int maxArea(int[] heights) {
  int maxArea = 0;
  int left = 0, right = heights.length - 1;
  while (left < right) {
    int area = Math.min(heights[left], heights[right]) * (right - left);
    maxArea = Math.max(maxArea, area);
    if (heights[left] < heights[right]) {
      left++;
    } else {
      right--;
    }
  }
  return maxArea;
}
}