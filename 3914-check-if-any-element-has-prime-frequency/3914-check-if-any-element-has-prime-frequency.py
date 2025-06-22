from collections import Counter
class Solution:
    def isprime(self, num):
        c=0
        for i in range(1, int(math.sqrt(num))+1):
            if num%i==0:
                c+=1
                if num//i!=i:
                    c+=1
        return True if c==2 else False
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        c=Counter(nums)
        for key, value in c.items():
            if self.isprime(value):
                return True
        return False
        