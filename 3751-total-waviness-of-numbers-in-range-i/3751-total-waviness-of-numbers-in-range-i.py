class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        p=(num1, num2)
        def w(n):
            s=str(n)
            if len(s)<3:
                return 0
            c=0
            for i in range(1, len(s)-1):
                if s[i]>s[i-1] and s[i]>s[i+1]:
                    c+=1
                elif s[i]<s[i-1] and s[i]<s[i+1]:
                    c+=1
            return c
        t=0
        for n in range(num1,num2+1):
            t+=w(n)
        return t
                