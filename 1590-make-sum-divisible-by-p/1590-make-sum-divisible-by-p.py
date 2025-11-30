class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total=sum(nums)
        re=total%p
        if re==0:
            return 0
        res=len(nums)
        curr=0
        has={0:-1}
        for i , n in enumerate(nums):
            curr=(curr+n)%p
            prefix=(curr-re+p)%p
            if prefix in has:
                length=i-has[prefix]
                res=min(res, length)
            has[curr]=i
        return -1 if res==len(nums) else res


        