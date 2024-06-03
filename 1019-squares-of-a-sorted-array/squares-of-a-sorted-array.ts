function sortedSquares(nums: number[]): number[] {
    const ans: number[] = new Array(nums.length);
    let p1 = 0, p2 = nums.length - 1;
    
    for (let i = nums.length - 1; i >= 0; i--) {
        if (Math.abs(nums[p1]) > Math.abs(nums[p2])) {
            ans[i] = nums[p1] * nums[p1];
            p1++;
        } else {
            ans[i] = nums[p2] * nums[p2];
            p2--;
        }
    }
    
    return ans;
}
