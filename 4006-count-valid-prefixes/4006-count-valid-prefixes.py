class Solution:
    def countValidPrefixes(self, s: str) -> int:
        v=0
        z=0
        o=0
        for i in s:
            if i=="0":
                z+=1
            else:
                o+=1
            if abs(z-o)<=1:
                v+=1
        return v