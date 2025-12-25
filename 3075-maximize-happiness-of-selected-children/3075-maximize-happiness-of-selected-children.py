class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        ans=0
        d=0
        happiness.sort(reverse=True)
        for i in range(k):
            ans+=max(0, happiness[i]-d)
            d+=1
        return ans
