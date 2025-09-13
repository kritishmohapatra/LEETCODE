class Solution:
    def maxFreqSum(self, s: str) -> int:
        c=Counter(s)
        v="aeiou"
        cs,vs=0,0
        for i in c:
            if i in v:
                vs=max(vs, c[i])
            else:
                cs=max(cs, c[i])
        return vs+cs

    
        