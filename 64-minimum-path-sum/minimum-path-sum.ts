function minPathSum(grid: number[][]): number {
    let r = grid.length;
    let c = grid[0].length;
    if (r === 1 && c === 1) {
        return grid[0][0];
    }
    const memo = Array.from({length:r},()=> Array(c).fill(-1));
    function getMinPathSum(i:number,j:number){
        if(i==0 && j==0){
            return grid[0][0];
        }
        if(i<0 || j<0){
            return Infinity
        }
        if(memo[i][j]!==-1){
            return memo[i][j]
        }
        let up = getMinPathSum(i-1,j);
        let left = getMinPathSum(i,j-1);
        return memo[i][j] = grid[i][j]+ Math.min(up,left);
    }
    getMinPathSum(r-1,c-1);
    return memo[r-1][c-1];
};