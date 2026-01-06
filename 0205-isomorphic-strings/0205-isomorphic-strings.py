class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m1={}
        s2=set()
        for c1, c2 in zip(s, t):
            if c1 in m1:
                if m1[c1]!=c2:
                    return False
            else:
                if c2 in s2:
                    return False
            m1[c1]=c2
            s2.add(c2)
        return True