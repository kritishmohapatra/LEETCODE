class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        good = [False] * n
        good[-1] = True

        for i in range(n - 2, -1, -1):
            good[i] = good[i + 1] and nums[i] < nums[i + 1]

        for i in range(n):
            if good[i]:
                return i

        return n