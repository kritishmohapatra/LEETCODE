from collections import defaultdict

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        bbx=defaultdict(list)
        bby=defaultdict(list)
        for x,y in buildings:
            bbx[x].append(y)
            bby[y].append(x)
        for x in bbx:
            bbx[x].sort()
        for y in bby:
            bby[y].sort()
        c=0
        for x,y in buildings:
            yc=bbx[x]
            xc=bby[y]
            if xc[0]<x<xc[-1] and yc[0]<y<yc[-1]:
                c+=1
        return c