import heapq
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        pq=[]
        events.sort(key=lambda x: x[0])
        day=0
        ind=0
        n=len(events)
        res=0
        while len(pq)!=0 or ind<n:
            if len(pq)==0:
                day=events[ind][0]
            while ind<n and events[ind][0]<=day:
                heapq.heappush(pq, events[ind][1])
                ind+=1
            heapq.heappop(pq)
            day+=1
            res+=1
            while len(pq)!=0 and pq[0]<day:
                heapq.heappop(pq)
        return res
        