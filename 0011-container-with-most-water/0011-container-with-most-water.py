class Solution:
    def rec(self, nums, low, high, area):
        if low>high:
            return area
        elif nums[low]<nums[high]:
            area=max(area, (high-low)*(min(nums[high], nums[low])))
            return self.rec(nums, low+1, high, area)
        else :
            area=max(area, (high-low)*(min(nums[high], nums[low])))
            return self.rec(nums, low, high-1,area)

    def maxArea(self, height: List[int]) -> int:
        ans=self.rec(height, 0, len(height)-1, 0)
        return ans
        