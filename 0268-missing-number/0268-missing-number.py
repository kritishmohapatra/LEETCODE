class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        org=(n*(n+1))//2
        now=sum(nums)
        return org-now
        