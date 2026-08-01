class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        mx=0
        for i in nums:
            if i!=0:
                c+=1
            else:
                c=0
            mx=max(mx, c)
        return mx