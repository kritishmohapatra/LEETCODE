class Solution:
    def intersection(self, a: List[int], b: List[int]) -> List[int]:
        ans=[]
        a.sort()
        b.sort()
        i, j=0, 0
        while i<len(a) and j<len(b):
            if a[i]<b[j]:
                i+=1
            elif a[i]>b[j]:
                j+=1
            else:
                if not ans or ans[-1]!=a[i]:
                    ans.append(a[i])
                i+=1
                j+=1
        return ans