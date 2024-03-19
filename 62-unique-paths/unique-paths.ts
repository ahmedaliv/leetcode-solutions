/*
 * @lc app=leetcode id=62 lang=typescript
 *
 * [62] Unique Paths
 */

// @lc code=start
function uniquePaths(m: number, n: number): number {
    
    const memo = Array.from({length: m}, () => Array(n).fill(-1));
    function getUniquePath(i: number, j: number): number{
        // base cases
        if (i === 0 && j === 0) return memo[i][j]=1;
        if(i < 0 || j < 0) return 0;
        if(memo[i][j]!==-1) return memo[i][j];
        // move up or left
        return memo [i][j]=getUniquePath(i-1, j) + getUniquePath(i, j-1);
    }
    // start from the goal 
    getUniquePath(m - 1, n - 1);
    return memo[m - 1][n - 1];
};
// @lc code=end

