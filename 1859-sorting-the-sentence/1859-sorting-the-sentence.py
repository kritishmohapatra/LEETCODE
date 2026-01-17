class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split()
        n=len(s)
        a=[0]*n
        for i in s:
            ind=int(i[-1])
            a[ind-1]=i[:-1]
        return " ".join(a)