class Solution:
    def numSub(self, s: str) -> int:
        mod=10**9+7
        ans=0
        l=-1
        for i,ch in enumerate(s):
            if ch=="0":
                l=i
            else:
                ans=(ans+(i-l))%mod
        return ans