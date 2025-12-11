import heapq
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        q=[]
        ans=[]
        for i in nums:
            heapq.heappush(q, -int(i))
        while k:
            ans.append(str(abs(heapq.heappop(q))))
            k-=1
        return ans[-1]