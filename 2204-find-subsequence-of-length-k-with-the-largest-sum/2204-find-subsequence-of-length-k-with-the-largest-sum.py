class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        res=[]
        thres=sorted(nums)[-k]
        larger=sum(n>thres for n in nums)
        eq=k-larger
        for n in nums:
            if n>thres:
                res.append(n)
            elif n==thres and eq:
                res.append(n)
                eq-=1
        return res