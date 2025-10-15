class Solution:
    def toHex(self, num: int) -> str:
        if num==0:
            return "0"
        h="0123456789abcdef"
        res=[]
        if num<0:
            num+=2**32
        while num>0:
            d=num%16
            res.append(h[d])
            num//=16
        return "".join(res[::-1])
