class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x>0:
            num=x
            s=0
            while num>0:
                rem=num%10
                s=s*10+rem
                num=num//10
            if s==x:
                return True
            else:
                return False
        elif x==0:
            return True
        else:
            return False

        