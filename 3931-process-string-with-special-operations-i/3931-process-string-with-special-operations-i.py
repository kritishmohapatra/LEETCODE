class Solution:
    def processStr(self, s: str) -> str:
        st=[]
        for c in s:
            if "a"<=c<="z":
                st.append(c)
            elif c=="*" and st:
                st=st[:-1]
            elif c=="#":
                st.extend(st[:])
            else:
                st=st[::-1]

        return "".join(st)

        