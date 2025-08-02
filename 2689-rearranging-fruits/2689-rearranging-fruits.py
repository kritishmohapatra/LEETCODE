from collections import Counter
class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        di=Counter()
        glob=float("inf")
        for a,b in zip(basket1, basket2):
            di[a]+=1
            di[b]-=1
            glob=min(glob, a, b)
        excess=[]
        for key, val in di.items():
            if val%2!=0:
                return -1
            excess+=[key]*(abs(val)//2)

        excess.sort()
        return sum(min(x, 2*glob) for x in excess[:len(excess)//2])