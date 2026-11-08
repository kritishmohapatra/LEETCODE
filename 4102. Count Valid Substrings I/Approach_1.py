class Solution:
    def countValidSubstrings(self, s: str) -> int:
        l=0
        a=0
        for r in range(len(s)):
            if r>=2 and s[r-2: r+1]=="abc":
                l=r-1
            a+=r-l+1
        return a            