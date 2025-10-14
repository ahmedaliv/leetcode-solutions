class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalized = ''.join(c.lower() for c in s if c.isalnum())
        l,r=0,len(normalized)-1
        while l<r:
            if normalized[l]==normalized[r]:
                r-=1
                l+=1
            else:
                return False
        return True