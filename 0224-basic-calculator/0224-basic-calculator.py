class Solution:
    def calculate(self, s: str) -> int:
        res, sign, num=0, 1, 0
        stack=[sign]
        for char in s:
            if char.isdigit():
                num=num*10+int(char)
            elif char=="(":
                stack.append(sign)
            elif char==")":
                stack.pop()
            elif char=="+" or char=="-":
                res+=sign*num
                sign=(1 if char=="+" else -1)* stack[-1]
                num=0
        return res+sign*num