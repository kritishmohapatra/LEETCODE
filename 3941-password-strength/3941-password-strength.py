class Solution:
    def passwordStrength(self, password: str) -> int:
        org=set(password)
        sp="!@#$"
        s=0

        for c in org:
            if c.islower():
                s+=1
            elif c.isupper():
                s+=2
            elif c.isdigit():
                s+=3
            elif c in sp:
                s+=5
        return s