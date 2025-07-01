class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans=[]
        seen=None
        for i in word:
            if i!=seen:
                ans.append(1)
                seen=i
            else:
                ans[-1]+=1
        return 1+sum([value-1 for value in ans if value>1])
        