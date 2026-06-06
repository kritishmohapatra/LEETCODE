class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        r=sum(nums)
        l=0
        re=[]
        for n in nums:
            r-=n
            re.append(abs(l-r))
            l+=n
        return re