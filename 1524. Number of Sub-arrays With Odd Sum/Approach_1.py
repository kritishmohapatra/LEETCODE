class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        m=10**9+7
        e=1
        o=0
        p=0
        a=0
        for n in arr:
            p+=n
            if p%2==0:
                a+=o 
                e+=1
            else:
                a+=e 
                o+=1
        return a%m
