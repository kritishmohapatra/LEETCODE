class Solution:
    def findLHS(self, nums: List[int]) -> int:
        hashmap=Counter(nums)
        ans=0
        for key, value in hashmap.items():
            if key+1 in hashmap:
                ans=max(ans, hashmap[key]+hashmap[key+1])
        return ans