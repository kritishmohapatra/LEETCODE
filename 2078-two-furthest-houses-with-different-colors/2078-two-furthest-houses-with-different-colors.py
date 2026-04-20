class Solution:
    def maxDistance(self, a: List[int]) -> int:
        return max(j-i for i in range(len(a)) for j in range(i+1,len(a)) if a[i]!=a[j])