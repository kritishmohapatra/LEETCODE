class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cons_max=0
        count=0
        for i in range(0, len(nums)):
            if nums[i]!=0:
                count+=1
            else:
                count=0
            cons_max=max(cons_max, count)
        return cons_max
    
        