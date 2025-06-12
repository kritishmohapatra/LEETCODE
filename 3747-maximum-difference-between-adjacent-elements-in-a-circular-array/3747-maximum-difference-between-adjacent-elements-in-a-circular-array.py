class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        maxi=float("-inf")
        for i in range(len(nums)):
            maxi=max(maxi, abs(nums[i]-nums[(i+1)%(len(nums))]))
        return maxi