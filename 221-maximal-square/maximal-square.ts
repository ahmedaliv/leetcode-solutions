// the key note here is to notice the repeated work being done while checking for valid squares
// on on each matrix cell
// when noting this, u would go from a regualr brute-force  solution to an efficient DP solution
function maximalSquare(matrix: string[][]): number {
    
    const n:number = matrix.length;
    const m: number = matrix[0].length;
    const dp:number[][]=[];
    for (let i = 0; i < n; i++) {
        dp[i] = new Array(m).fill(0);
    }
    function countSquares(r:number,c:number):number {
        if(r>=n || c>=m){
            return 0;
        }
        if (dp[r][c] !== 0) {
            return dp[r][c];
        }
        let right = countSquares(r,c+1);
        let down = countSquares(r+1,c);
        let diagonal = countSquares(r+1,c+1);
        if(matrix[r][c]=="1"){
            // min because if any of the cells are 0 then we cannot make a square.
            dp[r][c]= 1 + Math.min(right,down,diagonal);
        }
        return dp[r][c];
    }
    countSquares(0,0);
    let maxSize = 0;

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            maxSize = Math.max(maxSize, countSquares(i, j));
        }
    }

    return maxSize * maxSize; 
};