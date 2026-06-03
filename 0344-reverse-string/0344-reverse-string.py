class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        st=0
        e=len(s)-1
        while st<e:
            s[st], s[e]=s[e], s[st]
            st+=1
            e-=1
        return s
            
        