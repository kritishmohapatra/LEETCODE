class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s=sum(nums)
        if s>k:
            return s%k
        elif s%k==0:
            return 0
        elif s<k:
            return s
        