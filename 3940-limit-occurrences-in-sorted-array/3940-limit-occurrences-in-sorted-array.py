class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        res=[]
        prev=None
        c=0
        for n in nums:
            if n!=prev:
                prev=n
                c=1
            else:
                c+=1
            if c<=k:
                res.append(n)
        return res
