function majorityElement(nums: number[]): number {
    const freqMap = new Map<number, number>();
    for (let i = 0; i < nums.length; i++) {
        if (freqMap.has(nums[i])) {
            let count = freqMap.get(nums[i])!;
            freqMap.set(nums[i], count + 1);
        } else {
            freqMap.set(nums[i], 1);
        }
    }

    let maxCount = 0;
    let majorityElement = nums[0];

    for (let [num, count] of freqMap) {
        if (count > maxCount) {
            maxCount = count;
            majorityElement = num;
        }
    }

    return majorityElement;
}
