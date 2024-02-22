function numIslands(grid: string[][]): number {
    const n = grid.length;
    const m = grid[0].length;
    let visited: boolean[][] = Array(n);
    for (let i = 0; i < n; i++) {
        visited[i] = Array(m).fill(false);
    }

    function countSubislands(i: number, j: number): number {
        if (i >= 0 && i < n && j >= 0 && j < m && !visited[i][j] && grid[i][j] === '1') {
            visited[i][j] = true;
            const up = countSubislands(i - 1, j);
            const down = countSubislands(i + 1, j);
            const right = countSubislands(i, j + 1);
            const left = countSubislands(i, j - 1);

            return 1 + up + down + right + left;
        }
        return 0;
    }

    let res = 0;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (!visited[i][j] && grid[i][j] === '1')
                res += countSubislands(i, j) ? 1 : 0;
        }
    }
    return res;
};
