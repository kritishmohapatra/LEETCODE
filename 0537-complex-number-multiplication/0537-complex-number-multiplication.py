class Solution:
    def getrealandimg(self, s):
        return int(s[:s.index("+")]), int(s[s.index("+")+1:-1])
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a0, a1=self.getrealandimg(num1)
        b0, b1=self.getrealandimg(num2)
        return str(a0*b0-b1*a1)+"+"+str(a0*b1+a1*b0)+"i"
        