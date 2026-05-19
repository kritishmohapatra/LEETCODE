class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        s=set()
        for n in nums1:
            s.add(n)
        res=-1
        for k in nums2:
            if k in s:
                res=k
                break
        return res

    