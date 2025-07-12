class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        actual_sum=(n*(n+1))//2
        unique_sum=sum(set(nums))
        curr_sum=sum(nums)
        return [curr_sum-unique_sum, actual_sum-unique_sum ]

        