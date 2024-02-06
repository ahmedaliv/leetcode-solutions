// key idea is to use a hashmap to store the difference between the array elements and the target 
// and as we traverse the rest of the array we check our hashmap to check if the complement exists
function twoSum(nums: number[], target: number): number[] {
    let hash: { [key: number]: number } = {};
    for(let i = 0; i<nums.length;i++){
        let diff = target-nums[i]
        if(diff in hash){
            return [hash[diff],i]
        } else {
            hash[nums[i]] = i;
        }
    }
};