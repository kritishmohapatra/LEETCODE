class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        t=sum(nums)
        l=0
        c=0
        for i in range(len(nums)-1):
            l+=nums[i]
            t-=nums[i]
            if abs(t-l)%2==0:
                c+=1
        return c

            
        