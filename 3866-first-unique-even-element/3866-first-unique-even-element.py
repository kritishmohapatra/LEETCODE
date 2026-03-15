class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        k=Counter(nums)
        for i in nums:
            if i%2==0 and k[i]==1:
                return i 
        return -1