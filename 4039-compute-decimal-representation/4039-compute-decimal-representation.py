class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        d=[int(c) for c in str(n)][::-1]
        res=[]
        for i, v in enumerate(d):
            if v:
                res.append(10**i*v)
        return res[::-1]