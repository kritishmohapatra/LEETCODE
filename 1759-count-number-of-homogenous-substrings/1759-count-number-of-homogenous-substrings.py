class Solution:
    def countHomogenous(self, s: str) -> int:
        mod=10**9+7
        c=0
        ans=0
        cu="@"
        for i in s:
            c=c+1 if i==cu else 1
            cu=i
            ans+=c
            ans%=mod
        return ans