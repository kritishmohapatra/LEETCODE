class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n=len(nums)
        nums.sort()
        maxi=0
        left=0
        for right in range(n):
            while nums[right]>nums[left]*k:
                left+=1
            maxi=max(maxi, right-left+1)
        return n-maxi