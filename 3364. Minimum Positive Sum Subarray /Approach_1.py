class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n=len(nums)
        m=float("inf")
        f=False
        for size in range(l , r+1):
            curr=0
            for i in range(0, size):
                curr+=nums[i]
            if curr>0:
                m=min(m, curr)
                f=True
            for i in range(size,n):
                curr+=nums[i]-nums[i-size]
                if curr>0:
                    m=min(m, curr)
                    f=True
        return m if f else -1
                
        