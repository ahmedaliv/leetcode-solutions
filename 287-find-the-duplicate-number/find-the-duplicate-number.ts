/*
key-idea: is to deal with the elements of the array as pointers not values 
and then apply tortoise and hare algorithm 
*/

function findDuplicate(nums: number[]): number {
    let slow = nums[0];
    let fast = nums[0];
    // detect intersection
    do {
        // move tortoise 1 step
        slow = nums[slow];
        // move hare 2 steps(nums[fast]->step 1 then  put inside another nums[] so this is 2 )
        fast = nums[nums[fast]];
    } while (slow !== fast);
    // return tortoise to the beginning and then we try to find the start of the cycle
    // which is the duplicate number here
    slow = nums[0];
    while (slow !== fast) {
        slow = nums[slow];
        fast = nums[fast];
    }
    // return any one of them as both will be at the start of the cycle
    return slow;
}

