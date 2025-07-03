class Solution:
    def rec(self,l, k):
        if len(l)>k:
            return l
        nxt=[]
        for c in l:
            nxt.append(chr((ord(c)-ord("a")+1)%26+ord("a")))
        l.extend(nxt)
    def kthCharacter(self, k: int) -> str:
        s=["a"]
        while len(s)<=k:
            self.rec(s, k)
        return s[k-1]
        
        
