class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        m=prices[0]
        pr=0
        for p in prices:
            m=min(m, p)
            pr=max(pr,p-m)
        return pr
            