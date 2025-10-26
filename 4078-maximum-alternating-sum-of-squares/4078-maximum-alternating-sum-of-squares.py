class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squaranisqurure = [x * x for x in nums]
        sorted_squaranisqurure = sorted(squaranisqurure)
        k = len(nums) // 2
        sum_small = sum(sorted_squaranisqurure[:k])
        total = sum(squaranisqurure)
        return total - 2 * sum_small