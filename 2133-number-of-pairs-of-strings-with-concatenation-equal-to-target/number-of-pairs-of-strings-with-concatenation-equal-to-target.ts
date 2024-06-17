function numOfPairs(nums: string[], target: string): number {
    const map: { [key: string]: number } = {};
    let count = 0;

    for (const num of nums) {
        map[num] = (map[num] || 0) + 1;
    }

    for (const num of nums) {
        const complement = target.substring(num.length);
        // to not count the prefix again as a suffix 
        // check the 3rd example in the problem description.
        if (target.startsWith(num) && map[complement] !== undefined) {
            if (num === complement) {
                count += map[complement] - 1;
            } else {
                count += map[complement];
            }
        }
    }

    return count;
}