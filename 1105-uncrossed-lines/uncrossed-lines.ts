function maxUncrossedLines(nums1: number[], nums2: number[]): number {
    const memo: {[key: string]: number} = {}; 

    function maxLines(i: number, j: number): number {
        if (i === nums1.length || j === nums2.length) {
            return 0;
        }
        const key = `${i},${j}`; 
        if (key in memo) {
            return memo[key];
        }

        // check if a valid line
        if (nums1[i] === nums2[j]) {
            memo[key] = 1 + maxLines(i + 1, j + 1);
        } 
        // no ? then either move the first,second pointer 
        else {
            memo[key] = Math.max(maxLines(i + 1, j), maxLines(i, j + 1));
        }
        return memo[key];
    }

    return maxLines(0, 0);
}
