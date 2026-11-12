class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if costBoth>=(cost1+cost2):
            return (need1*cost1)+(need2*cost2)
        ov=min(need1, need2)
        t=ov*costBoth
        r1=need1-ov
        r2=need2-ov
        if r1>0:
            t+=r1*min(cost1, costBoth)
        elif r2>0:
            t+=r2*min(cost2, costBoth)
        return t