function countSubIslands(grid1: number[][], grid2: number[][]): number {
    const r = grid1.length;
    const c = grid1[0].length;

    function dfs(row: number, col: number): boolean {
        let isSubIsland = true;
        if (0 <= row && row < r && 0 <= col && col < c && grid2[row][col] === 1) {
            if (grid1[row][col] !== 1) return false;
            grid2[row][col] = -1;
            // for (let [dx, dy] of [[0, 1], [1, 0], [-1, 0], [0, -1]]) {
            //     isSubIsland = isSubIsland && dfs(row + dx, col + dy);
            // }
            let up = dfs(row-1,col);
            let down = dfs(row+1,col);
            let left = dfs(row,col-1);
            let right = dfs(row,col+1);
            return up && down && left && right && grid1[row][col] == 1;
        }
        return isSubIsland;
    }

    let subIslands = 0;

    for (let i = 0; i < r; i++) {
        for (let j = 0; j < c; j++) {
            if (grid2[i][j] === 1 && dfs(i, j)) {
                subIslands++;
            }
        }
    }

    return subIslands;
}
