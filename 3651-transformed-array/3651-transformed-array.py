class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n
        for i, x in enumerate(nums):
            res[i]=nums[(i+x)%n]
        return res