class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        c=Counter(nums)
        s=0
        for key, v in c.items():
            if v%k==0:
                s+=key*v
        return s
