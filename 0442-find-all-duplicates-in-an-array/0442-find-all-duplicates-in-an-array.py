class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        c=Counter(nums)
        d=[]
        for k, v in c.items():
            if v>1:
                d.append(k)
        return d