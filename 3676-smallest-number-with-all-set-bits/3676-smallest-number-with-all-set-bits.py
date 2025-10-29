class Solution:
    def smallestNumber(self, n: int) -> int:
        for i in range(1, n+1):
                n|=i
                i<<=1
        return n
