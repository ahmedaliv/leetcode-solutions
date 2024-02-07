function findTargetSumWays(nums: number[], S: number): number {
 const dp = {};

 function backtrack(curIndex:number,curSum:number){
     const key = `${curIndex},${curSum}`;
     if(key in dp){
         return dp[key];
     }
     // base case: tried all the array
     if(curIndex === nums.length){
         return curSum === S ? 1 : 0 ;
     }
     // trying all possibilites 
    const add =  backtrack(curIndex + 1, curSum + nums[curIndex] );
    const sub =  backtrack(curIndex + 1, curSum - nums[curIndex] );
    // memoizing 
    return dp[key]  = add + sub ;
    
 }
 return backtrack(0,0);

}