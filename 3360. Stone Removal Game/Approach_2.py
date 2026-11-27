class Solution:
    def canAliceWin(self, n: int) -> bool:
        k=1
        m=10
        while n>=m:
            n-=m
            k*=-1
            m-=1
        return k!=1
        