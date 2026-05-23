class Solution:
    def check(self, nums: List[int]) -> bool:
        k=0
        n=len(nums)
        for i in range(0, n):
            if nums[i]>nums[(i+1)%n]:
                k+=1
        if k>1:
            return False
        else:
            return True
    
        