class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans=1
        mini=nums[0]
        for i in range(1, len(nums)):
            if mini+k<nums[i]:
                ans+=1
                mini=nums[i]
        return ans
        