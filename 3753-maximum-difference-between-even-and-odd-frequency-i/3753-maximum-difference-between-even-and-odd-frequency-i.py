from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        k=Counter(s)
        max_od=float("-inf")
        min_ev=float("inf")
        for key, value in k.items():
            if value%2==1:
                max_od=max(max_od, value)
            else:
                min_ev=min(min_ev, value)
        return max_od-min_ev
                



        