class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        s=sorted(list(set(nums)))[::-1]
        if len(s)<k:
            return s
        return s[:k]