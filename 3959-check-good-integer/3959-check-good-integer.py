class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        d=0
        s=0
        x=n
        while x:
            r=x%10
            d+=r
            s+=r**2
            x//=10
        return s-d>=50
        