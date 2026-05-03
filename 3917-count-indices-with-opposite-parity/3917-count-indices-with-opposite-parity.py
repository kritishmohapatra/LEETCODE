class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        e=sum(1 for x in nums if x%2==0)
        o=len(nums)-e
        res=[]
        for x in nums:
            if x%2==0:
                e-=1
                res.append(o)
            else:
                o-=1
                res.append(e)
        return res