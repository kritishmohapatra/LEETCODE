class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        r=1%k
        for i in range(1, k+1):
            if r==0:
                return i
            r=(r*10+1)%k
        return -1