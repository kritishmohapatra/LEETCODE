class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x>0:
            num=x
            s=0
            while num>0:
                r=num%10
                s=s*10+r
                num//=10
            if s==x:
                return True
            else:
                return False
        if x==0:
            return True
        else:
            return False