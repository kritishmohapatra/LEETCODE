class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        c=Counter(nums)
        for k, v in c.items():
            if v>2:
                return False
        return True
        