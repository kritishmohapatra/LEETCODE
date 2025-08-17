class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod=10**9+7
        for l, r, k, v in queries:
            i=l
            while i<=r:
                nums[i]*=v 
                nums[i]%=mod
                i+=k
        ans=0
        for a in nums:
            ans^=a
        return ans