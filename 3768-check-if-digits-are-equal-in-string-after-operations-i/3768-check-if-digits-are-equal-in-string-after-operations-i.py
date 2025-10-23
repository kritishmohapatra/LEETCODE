class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s)>2:
            p=""
            for i in range(0, len(s)-1):
                d1=int(s[i])
                d2=int(s[i+1])
                d3=(d1+d2)%10
                p+=str(d3)
            s=p
        return len(set(s))==1
                
        