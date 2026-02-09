import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def cal_hour(piles, hour):
            total=0
            for i in piles:
                total+=math.ceil(i/hour)
            return total 
        low=1
        high=max(piles)
        res=high
        while(low<=high):
            mid=(low+high)//2
            total_h=cal_hour(piles, mid)
            if total_h<=h:
                res=min(res, mid)
                high=mid-1
            else:
                low=mid+1
        return res
