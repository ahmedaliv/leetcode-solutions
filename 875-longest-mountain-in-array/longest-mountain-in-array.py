class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        best = 0 
        asec,desc = 0,0
        if len(arr) < 3:
            return 0
        for end in range(1,len(arr)):
            # when invalid reset (2 cases 1- we already had a mountain going down and now we reached an end 2- two consecutive equal values)
            if(desc > 0 and arr[end]>arr[end-1]) or arr[end]==arr[end-1]:
                asec,desc =0 ,0
            
            if arr[end]>arr[end-1]:
                asec +=1
            elif arr[end]<arr[end-1]:
                desc += 1
            
            if asec > 0 and desc > 0:
                best = max(best, asec + desc + 1)

        return best