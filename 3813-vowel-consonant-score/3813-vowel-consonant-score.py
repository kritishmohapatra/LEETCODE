class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        c, v=0,0
        for i in s:
            if "a"<=i<="z":
                if i in "aeiou":
                    v+=1
                else:
                    c+=1
        return 0 if not c else v//c