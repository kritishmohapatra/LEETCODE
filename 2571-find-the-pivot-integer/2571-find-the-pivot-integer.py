class Solution:
    def pivotInteger(self, n: int) -> int:
        k=(n*(n+1))//2
        leftsum=0
        for i in range(1, n+1):
            rightsum=k-leftsum
            if rightsum==leftsum+i:
                return i
            leftsum+=i
        return -1
        