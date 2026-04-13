import math
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        minval=math.inf
        for i in range(len(nums)):
            if nums[i]==target:
                minval=min(minval, abs(start-i))
        return minval