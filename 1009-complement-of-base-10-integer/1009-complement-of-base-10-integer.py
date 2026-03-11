class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bit=len(bin(n).replace("0b",""))
        ans=n^((2**bit)-1)
        return ans
        