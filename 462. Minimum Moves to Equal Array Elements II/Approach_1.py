class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        med=nums[(len(nums))//2]
        mo=0
        for num in nums:
            mo+=abs(num-med)
        return mo