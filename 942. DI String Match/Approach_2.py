class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        l=0
        h=len(s)
        ans=[]
        for ch in s:
            if ch=="I":
                ans.append(l)
                l+=1
            else:
                ans.append(h)
                h-=1
        ans.append(l)
        return ans