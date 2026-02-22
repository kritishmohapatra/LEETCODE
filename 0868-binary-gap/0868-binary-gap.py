class Solution:
    def binaryGap(self, n: int) -> int:
        ind=0
        ans=0
        k=bin(n).replace("0b","")
        for i in range(len(k)):
            if k[i]=="1":
                ans=max(ans, i-ind)
                ind=i
        return ans

