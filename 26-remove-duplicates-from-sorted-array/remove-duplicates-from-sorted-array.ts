function removeDuplicates(nums: number[]): number {
    let map = new Map();
    let k = 0;

    for (let i = 0; i < nums.length; i++) {
        if (!map.has(nums[i])) {
            map.set(nums[i], true);
            nums[k] = nums[i];
            k++;
        }
    }
    
    return k;
}