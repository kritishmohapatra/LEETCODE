class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        c=nums
        
        s={}
        min_dist=float("inf")
        for j, val in enumerate(c):
           
            if val in s:
                i=s[val]
                d=abs(i-j)
                if d<min_dist:
                    min_dist=d
                
            r=int(str(val)[::-1])
           
            s[r]=j
        return min_dist if min_dist!=float("inf") else -1