class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans=[]
        for num in nums:
            if num==2:
                ans.append(-1)
            else:
                i=0
                while num>>i & 1:
                    i+=1
                ans.append(num-(1<<(i-1)))
        return ans
        