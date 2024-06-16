function kadane(nums: number[]): number {
    let maxSum = nums[0];
    let maxSoFar = nums[0];
    for (let i = 1; i < nums.length; i++) {
        maxSum = Math.max(nums[i], nums[i] + maxSum);
        maxSoFar = Math.max(maxSoFar, maxSum);
    }
    return maxSoFar;
}

function maxSubarraySumCircular(nums: number[]): number {
    let maxArr = kadane(nums);
    const totalSum = nums.reduce((acc,num)=> num+acc ,0)
    let negArr = nums.map(num=>-num);
    let minKadane = kadane(negArr);
    const maxCirc = totalSum + minKadane;

    if (maxCirc === 0) {
        return maxArr;
    }
    return Math.max(maxArr,maxCirc);
};