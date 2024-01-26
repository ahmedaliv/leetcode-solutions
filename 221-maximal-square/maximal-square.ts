// the key note here is to notice the repeated work being done while checking for valid squares
// on on each matrix cell
// when noting this, u would go from a regular brute-force  solution to an efficient DP solution
function maximalSquare(matrix: string[][]): number {
    
    const n:number = matrix.length;
    const m: number = matrix[0].length;
    const dp:number[][]=[];
    for (let i = 0; i < n; i++) {
        dp[i] = new Array(m).fill(0);
    }
    let maxSize = 0;

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (i === 0 || j === 0) {
                dp[i][j] = matrix[i][j] === "1" ? 1 : 0;
            } else if (matrix[i][j] === "1") {
                dp[i][j] = 1 + Math.min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]);
            }

            maxSize = Math.max(maxSize, dp[i][j]);
        }
    }

    return maxSize * maxSize;  
};