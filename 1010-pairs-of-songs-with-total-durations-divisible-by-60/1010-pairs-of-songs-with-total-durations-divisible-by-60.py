class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans=0
        c=[0]*60
        for t in time:
            t%=60
            ans+=c[(60-t)%60]
            c[t]+=1
        return ans