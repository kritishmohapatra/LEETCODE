class Solution:
    def makeFancyString(self, s: str) -> str:
        res=[]
        for c in s:
            if len(res)<2 or res[-1]!=c or res[-2]!=c:
                res.append(c)
        return "".join(res)