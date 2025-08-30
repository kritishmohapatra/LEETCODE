class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        s=Counter(str(n))
        mini=min(s.values())
        ans=float("inf")
        for k, v in s.items():
            if v==mini:
                ans=min(int(k), ans)
        return ans
            
        