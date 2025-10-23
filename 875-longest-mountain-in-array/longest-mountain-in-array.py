class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        ups = downs = longest = 0
        for i in range(1,len(arr)):
            if (downs and arr[i-1]<arr[i]) or (arr[i]==arr[i-1]):
                downs = ups = 0 
            
            ups += arr[i] > arr[i-1]
            downs += arr[i]<arr[i-1]
            if ups and downs:
                longest = max(longest,ups+downs+1)
        return longest