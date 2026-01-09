class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(10000) 
        a=int(num1)
        b=int(num2)
        c=a+b
        d=str(c)
        return d