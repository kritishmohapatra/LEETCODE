class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s=str(n)
        ans=""
        sm=0
        m=False
        for i in s:
            if i!="0":
                ans+=i
                sm+=int(i)
        if ans=="":
            return 0
        else:
            return int(ans)*sm
            
