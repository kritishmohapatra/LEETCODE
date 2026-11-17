class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            ans=""
            for i in range(0, len(s), k):
                grp=s[i:i+k]
                total=sum(int(digit) for digit in grp)
                ans+=str(total)
            s=ans 
        return s
