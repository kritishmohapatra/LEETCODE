class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        path=[]
        def partition(index):
            if index==len(s):
                res.append(path[:])
                return 
            for i in range(index, len(s)):
                if palindrome(s, index, i):
                    path.append(s[index:i+1])
                    partition(i+1)
                    path.pop()
        def palindrome(s, st, en):
            return s[st:en+1]==s[st:en+1][::-1]
        partition(0)
        return res