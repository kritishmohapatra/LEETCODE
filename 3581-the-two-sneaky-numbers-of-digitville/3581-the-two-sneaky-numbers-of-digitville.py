from collections import Counter
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans=[]
        k=Counter(nums)
        for key, value in k.items():
            if value==2:
                ans.append(key)
        return ans

        