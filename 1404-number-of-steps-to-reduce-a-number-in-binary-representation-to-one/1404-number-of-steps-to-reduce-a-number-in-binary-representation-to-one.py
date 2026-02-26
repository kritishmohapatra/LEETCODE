class Solution:
    def numSteps(self, s: str) -> int:
        ans=0
        carry=0
        for i in range(len(s)-1,0,-1):
            if (int(s[i])+carry)%2==1:
              ans+=2
              carry=1
            else:
                ans+=1
        return ans+carry
           