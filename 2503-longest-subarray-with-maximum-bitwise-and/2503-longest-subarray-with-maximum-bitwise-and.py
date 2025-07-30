class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxi=max(nums)
        cnt=0
        ans=1
        for i in nums:
            if i==maxi:
                cnt+=1
            else:
                cnt=0
            ans=max(cnt, ans)
        return ans

        