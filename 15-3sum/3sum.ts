function threeSum(nums: number[]): number[][] {
    nums.sort((a, b) => a - b); 

    const results: number[][] = [];
    for (let i = 0; i < nums.length - 2; i++) {
        // Skip duplicate elements to avoid duplicate triplets
        if (i > 0 && nums[i] === nums[i - 1]) {
            continue;
        }
        
        let l = i + 1;
        let r = nums.length - 1;
        
        while (l < r) {
            const total = nums[i] + nums[l] + nums[r];
            if (total === 0) {
                results.push([nums[i], nums[l], nums[r]]);
                
                // skipping duplicates , same as above
                while (l < r && nums[l] === nums[l + 1]) {
                    l++;
                }
                while (l < r && nums[r] === nums[r - 1]) {
                    r--;
                }
                l++;
                r--;
            } else if (total < 0) {
                l++;
            } else {
                r--;
            }
        }
    }
    return results;
}
