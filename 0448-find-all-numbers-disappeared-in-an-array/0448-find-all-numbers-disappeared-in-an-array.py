class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s=set(nums)
        m=[]
        for i in range(1, len(nums)+1):
            if i not in s:
                m.append(i)
        return m