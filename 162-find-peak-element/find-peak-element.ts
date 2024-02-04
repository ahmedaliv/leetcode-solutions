function findPeakElement(nums: number[]): number {
    let r = nums.length -1 ;
    let l = 0;

    while(l<r){
        let mid = l + Math.floor((r - l) / 2);
        if(nums[mid]>nums[mid+1]){
            r=mid;
        } else {
            l=mid+1
        }
    }
    return l;

};