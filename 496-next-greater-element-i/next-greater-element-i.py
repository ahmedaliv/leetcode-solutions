class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        h_t = {}
        res = [-1]* len(nums1)
        for i in range(len(nums1)):
            h_t[nums1[i]] = i

        s = []
        for i in range(len(nums2)):
            while s and nums2[i] > s[-1]:
                tp = s.pop()
                if tp in h_t:
                    idx = h_t[tp]
                    res[idx] = nums2[i]
            s.append(nums2[i])
        return res
            
        