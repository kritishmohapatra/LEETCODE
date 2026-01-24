class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxi=0
        for i in range(len(nums)//2):
            maxi=max(maxi, nums[i]+nums[len(nums)-1-i])
        return maxi
