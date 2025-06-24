class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n=len(nums)
        res=[]
        j=0
        for i in range(n):
            while j<n and (nums[j]!=key or j<i-k):
                j+=1
            if j==n:
                break 
            if abs(i-j)<=k:
                res.append(i)
        return res