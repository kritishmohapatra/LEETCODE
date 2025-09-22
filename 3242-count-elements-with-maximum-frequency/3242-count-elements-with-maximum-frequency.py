from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        k=Counter(nums)
        m=max(k.values())
        c=0
        for key , value in k.items():
            if value==m:
                c+=k[key]
        return c
        