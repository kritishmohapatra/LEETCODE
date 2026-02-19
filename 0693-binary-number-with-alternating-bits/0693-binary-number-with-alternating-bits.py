class Solution:
    def hasAlternatingBits(self, v: int) -> bool:
        return (q:=v>>1^v)&q+1==0