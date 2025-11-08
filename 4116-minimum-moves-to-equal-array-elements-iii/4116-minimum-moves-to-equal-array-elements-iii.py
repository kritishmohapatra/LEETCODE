class Solution:
    def minMoves(self, nums: List[int]) -> int:
        s=0
        m=max(nums)
        for i in nums:
            s+=m-i
        return s