class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res=[]
        for num in range(left, right+1):
            x=num
            while x>0:
                d=x%10
                if d==0 or num%d!=0:
                    break
                x//=10
            if x==0:
                res.append(num)
        return res
            