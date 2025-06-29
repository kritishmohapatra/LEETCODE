class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        ans=0
        nums.sort()
        mod=10**9+7
        n=len(nums)
        l=0
        r=n-1
        while l<=r:
            if nums[l]+nums[r]<=target:
                ans+=pow(2, r-l, mod)
                l+=1
            else:
                r-=1
        return ans%mod
        