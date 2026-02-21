class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        p=[2, 3, 5, 7, 11, 13, 17, 19]
        c=0
        for i in range(left, right+1):
            if bin(i).count("1") in p:
                c+=1
        return c