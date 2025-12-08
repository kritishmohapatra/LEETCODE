class Solution:
    def countTriples(self, n: int) -> int:
        ans=0
        sq=set()
        for i in range(1, n+1):
            sq.add(i*i)
        for a in sq:
            for b in sq:
                if a+b in sq:
                    ans+=1
        return ans