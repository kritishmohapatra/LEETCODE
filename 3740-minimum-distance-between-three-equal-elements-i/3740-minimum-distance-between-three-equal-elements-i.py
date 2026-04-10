class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        ans=inf
        n=len(nums)
        for i in range(n):
            for j in range(i):
                for k in range(j):
                    if nums[i]==nums[j] and nums[j]==nums[k]:
                        ans=min(ans,abs(i - j) + abs(j - k) + abs(k - i))
        if ans==inf:
            return -1
        else:
            return ans