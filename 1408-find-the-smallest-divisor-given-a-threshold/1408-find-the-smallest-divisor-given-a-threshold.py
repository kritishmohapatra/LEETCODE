class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def calci(nums, value):
            total=0
            for i in nums:
                total+=math.ceil(i/value)
            return total
        low=1
        high=max(nums)
        res=high
        while(low<=high):
            mid=(low+high)//2
            total=calci(nums, mid)
            if total<=threshold:
                res=min(res, mid)
                high=mid-1
            else:
                low=mid+1
        return res