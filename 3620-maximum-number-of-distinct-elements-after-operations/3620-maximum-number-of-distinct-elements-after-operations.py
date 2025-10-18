class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        ans = 0
        occupied = -math.inf

        for num in sorted(nums):
            if occupied < num + k:
                occupied = max(occupied + 1, num - k)
                ans += 1

        return ans