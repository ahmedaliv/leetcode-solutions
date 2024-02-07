

function findTargetSumWays(nums: number[], S: number): number {

    function backtrack(nums: number[], target: number, index: number, currentSum: number, memo: {[key: string]: number}): number {
        // Check if we've already computed this combination
        const key = index + ',' + currentSum;
        if (key in memo) {
            return memo[key];
        }

        // Base case: if we have processed all elements in the array
        if (index === nums.length) {
            // Check if we've reached the target sum
            return currentSum === target ? 1 : 0;
        }

        // Explore both possibilities: adding the current number and subtracting it
        const add = backtrack(nums, target, index + 1, currentSum + nums[index], memo);
        const subtract = backtrack(nums, target, index + 1, currentSum - nums[index], memo);

        // Store the result in memo
        memo[key] = add + subtract;

        return memo[key];
    }

    return backtrack(nums, S, 0, 0, {});
}

