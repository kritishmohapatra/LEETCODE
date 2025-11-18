class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        op={
            "+": lambda a,b: a+b,
            "-": lambda a,b: a-b,
            "*": lambda a,b: a*b,
            "/": lambda a,b: int(a/b)
        }
        for tk in tokens:
            if tk in op:
                b=st.pop()
                a=st.pop()
                st.append(op[tk](a,b))
            else:
                st.append(int(tk))
        return st.pop()
