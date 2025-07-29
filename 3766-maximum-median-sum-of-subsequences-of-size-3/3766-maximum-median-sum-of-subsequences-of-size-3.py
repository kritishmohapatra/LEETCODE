class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        cnt, idx = 0, n-2
        for _ in range(n // 3):
            cnt += nums[idx]
            idx -= 2
        return cnt