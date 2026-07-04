class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        c=Counter(nums)
        return c[nums[(len(nums)//2)]]==1