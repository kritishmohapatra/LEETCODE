from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d=Counter(arr)
        maxi=-1
        for key, val in d.items():
            if key==val:
                maxi=max(maxi, key)
        return -1 if maxi==-1 else maxi