class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d=Counter(nums)
        for i in range(1,101):
            d[i]+=d[i-1]
        return [0 if n==0 else d[n-1] for n in nums]