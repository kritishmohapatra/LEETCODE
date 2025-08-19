class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res=0
        n=len(nums)
        curr=0
        for i in range(n):
            if nums[i]==0:
                curr+=1
            else:
                res+=(curr*(curr+1))//2
                curr=0
        res+=(curr*(curr+1))//2
        return res