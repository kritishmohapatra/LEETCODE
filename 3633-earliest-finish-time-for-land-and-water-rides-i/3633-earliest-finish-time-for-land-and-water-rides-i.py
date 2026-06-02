class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n = len(landStartTime)
        m = len(waterStartTime)
        ans = float("inf")
        for i in range(n):
            for j in range(m):
                ans = min(ans,max(landStartTime[i]+landDuration[i],waterStartTime[j])+waterDuration[j])
                ans = min(ans,max((waterStartTime[j]+waterDuration[j]),landStartTime[i])+landDuration[i])
        return ans