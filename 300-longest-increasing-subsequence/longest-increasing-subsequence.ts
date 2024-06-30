function lengthOfLIS(nums: number[]): number {
    const dp = Array(nums.length).fill(null).map(()=>Array(nums.length +1).fill(-1));
    function getMaxLen(i,prev){
        if(i===nums.length){
            return 0;
        }
        if(dp[i][prev+1]!==-1){
            return dp[i][prev+1];
        }
        let notTake = getMaxLen(i+1,prev);
        let take =0;
        if (prev < 0 || nums[i] > nums[prev]) {
            take = 1 + getMaxLen(i+1,i);
        }
        dp[i][prev+1] = Math.max(take,notTake);
        return Math.max(take,notTake);
    }
    return getMaxLen(0,-1);
};