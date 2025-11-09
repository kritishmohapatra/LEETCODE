class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        def fun(a, b):
            if a==0 or b==0:
                return 0
            if a>=b:
                return 1+fun(a-b, b)
            else:
                return 1+fun(a, b-a)
        return fun(num1, num2)
        