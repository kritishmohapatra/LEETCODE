class Solution:
    def firstnotnine(self, s):
        for i, c in enumerate(s):
            if c!="9":
                return i 
        return 0
    def minMaxDifference(self, num: int) -> int:
        s=str(num)
        t_9=s[self.firstnotnine(s)]
        t_0=s[0]
        return int(s.replace(t_9, "9"))-int(s.replace(t_0, "0"))