class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod=(10**9+7)
        ans=0
        for i in range(n+1):
            k=i
            p=0
            while k>0:
                k=k//2
                p+=1
            ans=((ans<<p)+i)%mod
        return ans%mod