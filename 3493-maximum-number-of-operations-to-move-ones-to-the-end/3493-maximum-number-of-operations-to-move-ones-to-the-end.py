class Solution:
    def maxOperations(self, s: str) -> int:
        k=list(s)
        ones=s.count("1")
        total=0
        for i in range(len(k)-1, -1, -1):
            if k[i]=="0" and (i+1==len(k) or k[i+1]=="1"):
                total+=ones
            elif k[i]=="1":
                ones-=1
        return total