class Solution:
    def minimumDeletions(self, s: str) -> int:
        d=0
        cb=0
        for c in s:
            if c=="a":
                d=min(d+1 ,cb)
            else:
                cb+=1
        return d